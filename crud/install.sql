CREATE TABLE to_do (
    id SERIAL PRIMARY KEY, --SERIAL creates a sequential interger IDs
    title = TEXT NOT NULL,  --TEXT gives your a similar item to VARCHAR, but it can only be text.
    is_completed BOOLEAN DEFAULT FALSE,
);

INSERT INTO tasks (title) VALUES ("Buy Milk");
INSERT INTO tasks (title) VALUES ("Walk Dog");
INSERT INTO tasks (title) VALUES ("Study");
INSERT INTO tasks (title) VALUES ("Buy Bitcoin");