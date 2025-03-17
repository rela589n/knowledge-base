The principle that states that the logic must be implemented in the conceptually right classes for it (that, that have data needed to fulfill that logic).

> This is similar to an expert in the real world. You (ui) need to build a house (business logic), you ask architect (Expert) to do the job, rather than doing it by yourself.

For example, having `Sale` and `LineItem` classes (`sale.lineItems` relationship), we'd want to put `getTotalPrice` method inside of `Sale` class (since it's the owner of `lineItems` relationship), rather than anywhere else.

Also, it makes sense to fulfill the responsibilities of [[Use Case]] inside of the actual [[Command]] that holds input data needed to process the [[Use Case]], rather than putting it anywhere else and using [[Command]] as a slave. 
