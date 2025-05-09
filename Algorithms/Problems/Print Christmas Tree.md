Task: print Christmas Tree into console

```php
class ChristmasTree
{
    public function __construct(private readonly int $deep)
    {
    }

    public function print(): void
    {
        for ($i = 0; $i < $this->deep; $i++) {
            $this->printSpaces($i);
            $this->printStars($i);
            echo PHP_EOL;
        }
    }

    private function printSpaces(int $level): void
    {
        echo str_repeat(' ', $this->deep - $level);
    }

    private function printStars(int $level): void
    {
        // 2 is the star difference between levels
        echo str_repeat('*', $level * 2 + 1);
    }
}

$tree = new ChristmasTree(20);
$tree->print();

/*

x * 2 + 1 stars

0 => 1       *              |              |  14 spaces
1 => 3      ***             |             |  13
2 => 5     *****            |            |  12
3 => 7    *******           |           |
         *********          |          |
        ***********         |         |
       *************        |        |
      ***************       |       |
     *****************      |      |
    *******************     |     |
   *********************    |    |
  ***********************   |   |
 *************************  |  |
*************************** | |

DEEP: 14
```