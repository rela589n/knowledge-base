The [[Monitoring tools|monitoring tool]] .

It allows you to get the insights about what happens in your application from the business perspective. For example, graphs representing count of registered users per hour, purchased orders over time, etc. The application metrics (total number of requests, disk usage) could be added as well.

It works by scrapping your endpoint response in [[OpenMetrics format]]. 

Basically, there are open-source solutions ([prometheus bundle](https://github.com/artprima/prometheus-metrics-bundle)) that provide tools for you to collect the metrics right away as the events happen (e.g. user gets registered) and store them into some external Redis/Apcu storage, exposing these from public endpoint later on.
