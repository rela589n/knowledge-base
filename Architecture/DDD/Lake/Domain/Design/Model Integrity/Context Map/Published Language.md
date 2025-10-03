**Published Language** - [[Context Integration Strategies|Relationship]] between parties with equal right, when **intermediary language** is created *for* their **integration**.

Sometimes when integrating two [[Domain|Businesses]] to exchange data, 
we **don't** want to **choose one [[Domain Model|Model]]** over the other, 
***lest*** [[Domain Model|Model]] would **remain bound** to this communication protocol (being especially bad for bad models).

Instead, a more generic **[[Published Language]]** is introduced.
It's **documented** and publicly exposed (api doc). 
The underlying [[Domain Model|Model]] doesn't really need to match.

>**Example**: [[DQL]]. 
>Slight changes could potentially be translated over different Databases.

**XML** allows formal definition of the domain language (WSDL), in which the data may be translated. Schema definitions create shared [[Published Language]] definitions for the [[Domain|Domains]]. 
CML (chemical markup language) both extended and benefited from XML for chemistry.

There are also **[[Binary data formats|Binary Protocols]]**, where schema interpretation is separate, and it provides better development over time (schema names aren't bound).