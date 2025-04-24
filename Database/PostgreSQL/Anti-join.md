```sql
-- must return the Fifth post of user 1 only, because it hasn't been yet viewed
select *
from posts
         inner join follower_relations on posts.author_id = follower_relations.followee_id
         left join viewed_posts
                   on viewed_posts.user_id = follower_relations.user_id
                       and viewed_posts.author_id = posts.author_id
                       and viewed_posts.start_id <= posts.id
                       and posts.id <= viewed_posts.end_id
where follower_relations.user_id = 123
  and viewed_posts.user_id is null
order by posts.id desc;

DROP TABLE posts;
CREATE TABLE posts
(
    id        SERIAL PRIMARY KEY,
    author_id INTEGER NOT NULL,
    content   TEXT
);

DROP TABLE follower_relations;
CREATE TABLE follower_relations
(
    id          SERIAL PRIMARY KEY,
    user_id     INTEGER NOT NULL,
    followee_id INTEGER NOT NULL,
    UNIQUE (user_id, followee_id)
);

DROP TABLE viewed_posts;
CREATE TABLE viewed_posts
(
    id        SERIAL PRIMARY KEY,
    user_id   INTEGER NOT NULL,
    author_id INTEGER NOT NULL,
    start_id  INTEGER NOT NULL,
    end_id    INTEGER NOT NULL,
    CONSTRAINT valid_date_range CHECK (start_id <= end_id)
);

TRUNCATE TABLE posts;
INSERT INTO posts (id, author_id, content)
VALUES (1, 1, 'First post by author 1'),
       (2, 1, 'Second post by author 1'),
       (3, 1, 'Third post by author 1'),
       (4, 1, 'Fourth post by author 1'),
       (5, 1, 'Fifth post by author 1'),

       (6, 2, 'First post by author 2'),
       (7, 2, 'Second post by author 2'),
       (8, 3, 'Post by author 3');

TRUNCATE follower_relations;
INSERT INTO follower_relations (user_id, followee_id)
VALUES (123, 1), -- User 123 follows author 1
       (123, 2), -- User 123 follows author 2
       (456, 1), -- User 456 follows author 1
       (789, 3); -- User 789 follows author 3

TRUNCATE viewed_posts;
INSERT INTO viewed_posts (user_id, author_id, start_id, end_id)
VALUES (123, 1, 1, 2), -- User 123 viewed author 1's posts: 1 through 2
       (123, 1, 3, 4), -- User 123 viewed author 1's posts 3 through 4
       (123, 2, 6, 7); -- User 123 viewed all author 2's posts
```