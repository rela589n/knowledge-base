The `prototype` folder contains index.html file:

```html
<html>

<head>
    <title>Centrifugo quick start</title>
</head>

<body>
<pre id="container">-</pre>
<script src="https://unpkg.com/centrifuge@5.0.1/dist/centrifuge.js"></script>
<script type="text/javascript">
    const container = document.getElementById('container');

    async function getToken()
    {
        return "<your_centrifugo_jwt_token>";
    }

    const centrifuge = new Centrifuge("ws://localhost:8008/connection/websocket", {
        getToken: getToken,
    });

    centrifuge.on('connecting', function (ctx) {
        console.log(`connecting: ${ctx.code}, ${ctx.reason}`);
    }).on('connected', function (ctx) {
        console.log(`connected over ${ctx.transport}`);
    }).on('disconnected', function (ctx) {
        console.log(`disconnected: ${ctx.code}, ${ctx.reason}`);
    }).connect();

    const userId = 123;

    const sub = centrifuge.newSubscription("user_events:general#"+ userId);

    sub.on('publication', function (ctx) {
        console.log(ctx.data)

        let eventName = ctx.data.event;

        if ('hello' === eventName) {
            alert(eventName);
        }

        document.title = eventName;
        container.innerHTML = JSON.stringify(ctx.data.data);
    }).on('subscribing', function (ctx) {
        console.log(`subscribing: ${ctx.code}, ${ctx.reason}`);
    }).on('subscribed', function (ctx) {
        console.log('subscribed', ctx);
    }).on('unsubscribed', function (ctx) {
        console.log(`unsubscribed: ${ctx.code}, ${ctx.reason}`);
    }).subscribe();
</script>
</body>
</html>
```