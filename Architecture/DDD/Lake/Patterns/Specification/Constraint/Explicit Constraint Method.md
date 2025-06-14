---
aliases:
  - Constraint Method
---
Implicit (bad):

```java
class Bucket {
	private float capacity;
	private float contents;

	public void pourIn(float addedVolume) {
		if (contents + addedVolume > capacity) {
			contents = capacity;
		} else {
			contents = contents + addedVolume;
		}
	}
}
```

Explicit (good) - you can say "Bucket's contents is constrained to capacity":

```java
class Bucket {
	private float capacity;
	private float contents;

	public void pourIn(float addedVolume)
	{
		float volumePresent = contents + addedVolume;
		contents = constrainedToCapacity(volumePresent);
	}

	private float constrainedToCapacity(float volumePlacedIn)
	{
		if (volumePlacedIn > capacity)
			return capacity;

		return volumePlacedIn;
	}
}
```

