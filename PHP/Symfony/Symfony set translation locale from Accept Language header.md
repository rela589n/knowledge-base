```yaml
framework:
    default_locale: en
    enabled_locales: [ uk ]

    set_locale_from_accept_language: true
    set_content_language_from_locale: true

    translator:
        default_path: '%kernel.project_dir%/translations'
        fallbacks:
            - en
        providers:

when@dev:
    framework:
        enabled_locales: [ uk, en ]

when@test:
    framework:
        enabled_locales: [ uk, en ]
```
