The `tokens` directive is invaluable for debugging.

```vespa
	document-summary debug-tokens {
		summary url {}
		summary url-tokens {
			source: url
			tokens
		}
		from-disk
	}
```

If search isn't matching what you expect,
  check how Vespa actually tokenized your content.

Often the issue is in tokenization mismatch between query and document.