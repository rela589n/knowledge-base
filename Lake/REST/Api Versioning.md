`/api/v1.0/entities/{id}/action`

[[Api Versioning.excalidraw]]

The benefit of this approach is that ideally, we would open api documentation for the particular point in time and we would be able to see the behavior of all the endpoints for that particular version.

Behind the scenes, backend might use the same code but check the version running.

Each particular endpoint change might introduce a bump in api version.

### Version 1

`/api/v1.0/users`

```json
[
	{
	  "name": "John",
	  "age": 25
	}
]
```

#### Code reading old data

```php
type User = {
  name: string;
  age: number;
};

async function fetchUsers(): Promise<User[]> {
  const response = await fetch("/api/v1.0/users");

  return response.json();
}
```
### Version 2

`/api/v1.1/users`

```json
{
	"results": [
		{
		  "name": "John",
		  "age": 25
		}
	],
	"metadata": {
		"total": 200,
		"limit": 1,
		"offset": 10
	}
}
```

