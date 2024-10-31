Note that when running application with [[RoadRunner]] or [[Swoole]], it's absolutely necessary to make your services stateless. 

Otherwise one processed request could lead to the unexpected outcome in the other request.

