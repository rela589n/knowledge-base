This script sets up [[PostgreSQL Partitioning|PostgreSQL Partitions]] running on 256 parallel connections:

```php
#[AsCommand(name: 'app:accounting:account:setup-partitions', description: 'Setup partitions for accounting account transactions')]
final class SetupPartitionsConsoleCommand extends Command
{
    private const int CONNECTIONS = 256;

    protected function configure(): void
    {
        $this
            ->addArgument('source_table', InputArgument::REQUIRED, 'Source table with transactions data')
            ->addArgument('target_table', InputArgument::REQUIRED, 'Target table for partitions')
            ->addOption('connections', 'c', InputOption::VALUE_OPTIONAL, 'Number of concurrent connections', self::CONNECTIONS)
            ->setHelp(<<<'HELP'
The <info>%command.name%</info> command sets up partitions for accounting account transactions.

Usage example:
  <info>bin/console app:accounting:account:setup-partitions accounting_accounts_not_partitioned accounting_account_transactions -c 256 -vv</info>
HELP
            );
    }

    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $io = new SymfonyStyle($input, $output);
        $config = PostgresConfig::fromString("host=postgresql user=postgres db=project_db_test password=qwerty");

        $connections = (int)$input->getOption('connections');
        $pool = new PostgresConnectionPool($config, $connections);

        $sourceTable = $input->getArgument('source_table');
        $targetTable = $input->getArgument('target_table');

        $io->info(sprintf('Selecting %s...', $sourceTable));

        $results = $pool->execute(sprintf('SELECT sequence_id, id FROM %s ORDER BY sequence_id', $sourceTable));

        $io->info(sprintf('Creating partitions for %s...', $targetTable));

        $it = 0;
        $futures = [];
        foreach ($results as ['sequence_id' => $sequenceId, 'id' => $id]) {
            $futures[] = async(
                fn () => $pool->execute(sprintf(
                    <<<SQL
                CREATE TABLE
                    IF NOT EXISTS {$targetTable}_p%s
                    PARTITION OF {$targetTable} 
                        FOR VALUES IN ('%s');
                SQL,
                    $sequenceId,
                    $id,
                )),
            );

            ++$it;

            if ($it % $connections === 0) {
                try {
                    awaitAnyN(count($futures), $futures);
                } catch (CompositeException $e) {
                    $reasons = $e->getReasons();
                    $connectionException = reset($reasons);

                    if (!$connectionException instanceof SqlConnectionException) {
                        throw $connectionException;
                    }

                    throw $connectionException->getPrevious();
                }

                $io->info(sprintf('Created Partitions: %d', $it));
            }
        }

        if (!empty($futures)) {
            awaitAll($futures);
        }

        $io->info(sprintf('All partitions for %s created successfully.', $targetTable));

        return Command::SUCCESS;
    }
}
```