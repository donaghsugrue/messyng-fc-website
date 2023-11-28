DROP TABLE IF EXISTS friends;

CREATE TABLE friends
(
    name TEXT PRIMARY KEY,
    url TEXT NOT NULL,
    pfp TEXT NOT NULL
);

INSERT INTO friends (name, url, pfp)
VALUES
    (   "Post Punk Podge & The Technohippies",
        "https://www.facebook.com/PostPunkPodge/",
        "https://uploads.nialler9.com/wp-content/uploads/2018/09/14171727/post-punk-podge.jpg"
    )
;

SELECT * FROM friends;