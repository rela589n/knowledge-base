**Published Language** - [[Bounded Context Relationships|Relationship]] between parties with equal right, when **intermediary language** is used for their integration.

Sometimes when integrating two [[Domain|Businesses]] to exchange data, we can't choose one [[Domain Model|Model]] over the other. Doing so would imply that it'll remain chained to this communication protocol.

As a solution, a more generic [[Published Language]] can be introduced that's documented and publicly exposed (api doc). The underlying [[Domain Model|Model]] don't necessarily need to match.

XML allows formal definition of the domain language, wherein the data may be translated.

There are also [[Binary data formats|Binary Protocols]], where schema interpretation is separate, and it provides better progression over time.


