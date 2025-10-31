There are two types of properties:
- **safety** - properties, which if not satisfied lead to system fault, which can't be undone automatically. The particular point in time may be determined when safety property was violated;
- **liveness** - any properties, which relate to [[Async Network|networks]], namely which contain "eventual" in the description. May not hold for some time, but there's hope 'll be satisfied in future.

**Safety properties** should be satisfied all the time.