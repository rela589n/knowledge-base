**Published Language** - [[Bounded Context Relationships|Relationship]] between parties with equal right, when **intermediary language** is used for their integration.

Sometimes when integrating two [[Domain|Businesses]] to exchange data, we **don't choose one [[Domain Model|Model]]** or the other. Doing so would imply that it'll **remain chained** to this communication protocol (especially bad for bad models).

Instead, a more generic **[[Published Language]]** can be introduced that's **documented** and publicly exposed (api doc). The underlying [[Domain Model|Model]] doesn't necessarily need to match.

**XML** allows formal definition of the domain language (WSDL), wherein the data may be translated. Schema definitions create shared [[Published Language]] definitions for the [[Domain|Domains]].

There are also **[[Binary data formats|Binary Protocols]]**, where schema interpretation is separate, and it provides better development over time (schema names aren't bound).
