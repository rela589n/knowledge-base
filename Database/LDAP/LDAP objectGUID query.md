There's a special `objectGUID` filed that can be used in order to find the very particular item in the system by it's id. Though, in order to query by it, guid (like `{5cd3e73f-2c38-4079-b2a4-32d651db013b}`) must be converted into sequence of bytes in special format: `\3f\e7\d3\5c\38\2c\79\40\b2\a4\32\d6\51\db\01\3b`

Here's a `LdapGuid` class that could convert guid into Microsoft-LDAP query format and back:

```php
final readonly class LdapGuid
{
    public function __construct(
        private Uuid $uuid,
    ) {
    }

    public static function fromUuidString(string $uuidString): self
    {
        return new self(Uuid::fromString($uuidString));
    }

    public static function fromUuidStringOrNull(?string $uuidString): ?self
    {
        if (null === $uuidString) {
            return null;
        }

        return self::fromUuidString($uuidString);
    }

    /**
     * Create from an LDAP-compatible binary format.
     *
     * @param string $ldapGuid The LDAP-compatible format (e.g., '3fe7d35c382c7940b2a432d651db013b').
     */
    public static function fromLdapHexString(string $ldapGuid): self
    {
        // Split the binary GUID into parts
        $part1 = substr($ldapGuid, 0, 8);
        $part2 = substr($ldapGuid, 8, 4);
        $part3 = substr($ldapGuid, 12, 4);
        $part4 = substr($ldapGuid, 16, 4);
        $part5 = substr($ldapGuid, 20);

        // Convert from little-endian to big-endian
        $part1 = implode('', array_reverse(str_split($part1, 2)));
        $part2 = implode('', array_reverse(str_split($part2, 2)));
        $part3 = implode('', array_reverse(str_split($part3, 2)));

        // Concatenate all parts to form the original GUID
        $guid = sprintf('%s-%s-%s-%s-%s', $part1, $part2, $part3, $part4, $part5);

        return new self(Uuid::fromString($guid));
    }

    /** Convert a standard GUID to an LDAP-compatible hex format. */
    public function toLdapHexString(): string
    {
        // Remove curly braces and hyphens from the GUID.
        $guidHex = str_replace('-', '', $this->uuid->toRfc4122());

        // Split the GUID into parts for reordering.
        $part1 = substr($guidHex, 0, 8);
        $part2 = substr($guidHex, 8, 4);
        $part3 = substr($guidHex, 12, 4);
        $part4 = substr($guidHex, 16, 4);
        $part5 = substr($guidHex, 20);

        // Convert to the little-endian format required by AD.
        $part1 = implode('', array_reverse(str_split($part1, 2)));
        $part2 = implode('', array_reverse(str_split($part2, 2)));
        $part3 = implode('', array_reverse(str_split($part3, 2)));

        return $part1.$part2.$part3.$part4.$part5;
    }

    public function toLdapQueryFormat(): string
    {
        $hexString = $this->toLdapHexString();

        // Format as a binary string for LDAP (each byte escaped).
        $ldapGuid = '';

        for ($i = 0, $iMax = strlen($hexString); $i < $iMax; $i += 2) {
            $ldapGuid .= '\\'.substr($hexString, $i, 2);
        }

        return $ldapGuid;
    }

    public function equals(?self $id): bool
    {
        return null !== $id && $this->uuid->equals($id->uuid);
    }

    public function getUuid(): Uuid
    {
        return $this->uuid;
    }
}
```

That's how it works:

```php
#[CoversClass(LdapGuid::class)]
final class LdapGuidUnitTest extends TestCase
{
    public function testCreateGuidFromLdapHexString(): void
    {
        $ldapGuid = LdapGuid::fromLdapHexString('59059217f967f94db2594d15229ea661');

        self::assertSame('17920559-67f9-4df9-b259-4d15229ea661', $ldapGuid->getUuid()->toRfc4122());
    }

    public function testConvertGuidToLdapFormat(): void
    {
        $ldapGuid = new LdapGuid(Uuid::fromString('17920559-67f9-4df9-b259-4d15229ea661'));

        self::assertSame('59059217f967f94db2594d15229ea661', $ldapGuid->toLdapHexString());
        self::assertSame('\59\05\92\17\f9\67\f9\4d\b2\59\4d\15\22\9e\a6\61', $ldapGuid->toLdapQueryFormat());
    }
}
```