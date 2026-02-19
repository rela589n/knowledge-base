---
aliases:
  - grammar
---
A [[userInput()|userInput()]] annotation that controls how Vespa parses user input into query terms.

```
{defaultIndex:"title", grammar:"all"}userInput(@user-query)
```

## Options

| Grammar      | `"red running shoes"` becomes        | Meaning                                          |
| ------------ | ------------------------------------ | ------------------------------------------------ |
| `"weakAnd"`  | weakAnd(red, running, shoes)         | Soft AND — prefers all, allows partial (default) |
| `"all"`      | `red AND running AND shoes`          | All words must match                             |
| `"any"`      | `red OR running OR shoes`            | Any word can match                               |
| `"tokenize"` | [red, running, shoes] (no operators) | Just splits into tokens                          |
| `"segment"`  | treats as a single segment           | For CJK / unsegmented languages                  |
| `"raw"`      | `"red running shoes"` as-is          | No parsing at all                                |
