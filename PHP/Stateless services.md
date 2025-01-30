Note that when running application with [[RoadRunner]] or [[Swoole]], it's *absolutely necessary* to make your services stateless. 

Otherwise one processed request could lead to the unexpected outcome in the other request.

Any shared global state must be avoided. And this rule includes `vendor/` folder as well 👀. 

For example, problems could arise when adding request id to the headers/logs. If one uses `#[CurrentUser]`, - it must not be used in the constructor.