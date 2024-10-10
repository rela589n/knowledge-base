There's a special `objectGUID` filed that can be used in order to find the very particular item in the system by it's id. Though, in order to query by it, guid (like `{5cd3e73f-2c38-4079-b2a4-32d651db013b}`) must be converted into sequence of bytes in special format: `\3f\e7\d3\5c\38\2c\79\40\b2\a4\32\d6\51\db\01\3b`

Here's function that can convert guid int Microsoft-LDAP query format:

```php
function convertGuidToLdapFormat($guid) {  
    // Remove curly braces and hyphens from the GUID.  
    $guid = str_replace(['{', '}', '-'], '', $guid);  
  
    // Split the GUID into parts for reordering.  
    $data1 = substr($guid, 0, 8);  
    $data2 = substr($guid, 8, 4);  
    $data3 = substr($guid, 12, 4);  
    $data4 = substr($guid, 16, 4);  
    $data5 = substr($guid, 20);  
  
    // Convert to the little-endian format required by AD.  
    $data1 = implode('', array_reverse(str_split($data1, 2)));  
    $data2 = implode('', array_reverse(str_split($data2, 2)));  
    $data3 = implode('', array_reverse(str_split($data3, 2)));  
  
    // Concatenate all parts.  
    $binaryGuid = $data1 . $data2 . $data3 . $data4 . $data5;  
  
    // Format as a binary string for LDAP (each byte escaped).  
    $ldapGuid = '';  
    for ($i = 0; $i < strlen($binaryGuid); $i += 2) {  
        $ldapGuid .= '\\' . substr($binaryGuid, $i, 2);  
    }  
    return $ldapGuid;  
}
```

