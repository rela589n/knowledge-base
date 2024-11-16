Adding restrictions of domain. 

For instance, a one-to-many `Country - President` relationship could be qualified to `one-to-one` given that in one moment of time there's only one president.

![[Constrained relationship.png]]

Also, a questionnaire may have many answered sections (`one-to-many`), but they could be constrained by the template section, meaning `one-to-one` relationship in scope of the given section:
```php
public function getAnsweredSection(Section $s): AnsweredSection
{
	return $this->answeredSections
	    ->matching('section = :$s')
	    ->first();
}
```