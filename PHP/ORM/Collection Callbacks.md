Consider that we have following relationship:

```php
private PostCollection $posts {  
    set => $value->ofOwner($this->id);
}
```

Now if we'd like to define the invariant that user can have up to 10 posts created within the period of day.

We can subscribe to the event when new `Post` is added to the main `PostCollection`, and run custom logic:

```php
// this is executed before post is added to the collection
$value->ofOwner($this->id)->onAdd(function() {
    if ($this->posts->ofLastDay()->count() + 1 >= 10) {
	    throw new PostLimitException();
    }
})
```