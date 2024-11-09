Adding restrictions of domain. 

For instance, a one-to-many country-president relationship may be qualified to one-to-one given that in one moment of time there's only one president.

![[Constrained relationship.png]]

Also, a questionnaire may have many answered sections (1-many), but they are constrained by survey template section, hereby reducing this to one-to-one in scope of survey template section:
```php
public function getAnsweredSection(Section $s): AnsweredSection
{
	return $this->answeredSections
	    ->matching('section = :$s')
	    ->first();
}
```