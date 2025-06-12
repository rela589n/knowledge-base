For example:
`/customers/{customerId}/invoices/{invoiceId}`

You'd want to make sure that Invoice of `invoiceId` belongs to customer, and if it doesn't - thrown an exception (probably 404).

If that's the case, then Customer must be [[Aggregate Root]], and Invoice - subsidiary entity. Use [[Association]] to find one.
