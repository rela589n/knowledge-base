[[Centrifugo]]

```json
{
    "token_hmac_secret_key": "36d87dea-5441-443c-b564-93396b3a42d3",
    "api_key": "33d6cec4-c52a-40de-b949-160fef590899",
    "allowed_origins": [
        "http://localhost:3003"
    ],
    "admin": true,
    "admin_password": "Dth&bg-.#js$Vj,aafu{2",
    "admin_secret": "42b526b0-8905-4d67-ab69-47b2aaa0a145",
    "health": true,
    "namespaces": [
        {
            "name": "user_events",
            "history_size": 100,
            "history_ttl": "600s",
            "force_positioning": true,
            "force_recovery": true,
            "allow_user_limited_channels": true,
            "allow_history_for_subscriber": true
        }
    ]
}
```