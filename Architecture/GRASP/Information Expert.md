The principle that states that the logic must be implemented in the classes that have the data needed to fulfill that logic.

> This is similar to an expert in the real world. You (ui) need to build a house (business logic), you ask architect (Expert) to do the job, rather than doing it by yourself.

For example, having `Sale` and `LineItem` classes (`sale.lineItems` relationship), we'd want to put `getTotalPrice` method inside of `Sale` class (as it owns `lineItems`) rather than anywhere else.

Also, it makes sense to fulfill the responsibilities of [[Use Case]] inside of the actual [[Command]] that holds all the necessary data rather than any other external class. 
