The principle that states that the responsibilities must be implemented in the classes that have the data needed to fulfill that responsibility.

> This is like an expert in real world. You (ui) need to build a house (business logic), you ask architect (Expert) to fulfill the task, rather than doing it by yourself.

For example, having `Sale` and `LineItem` classes, we'd want to put `getTotalPrice` method inside of `Sale` class (as it owns `lineItems`) rather than anywhere else.

Also, it makes sense to fulfill the responsibilities of [[Use Case]] inside of the actual [[Command]] that holds all the necessary data. 
