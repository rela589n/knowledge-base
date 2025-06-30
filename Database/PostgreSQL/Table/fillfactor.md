[Article](https://habr.com/ru/companies/otus/articles/905882/)

default: 100

Each insert packs table [[Page|Pages]] up to this fill-factor value (by default, 100, e.g. full). Specifying it with value less than 100 will leave the room for updates.

> For a table whose entries are never updated, complete packing is the best choice, but in heavily updated tables smaller fillfactors are appropriate.

When there's no enough room on the same [[Page]], it's [[Page Split|Split]].
