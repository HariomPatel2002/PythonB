BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> ebe73c35ab17

CREATE TABLE users (
    id SERIAL NOT NULL, 
    name VARCHAR(100), 
    email VARCHAR(100), 
    age INTEGER, 
    PRIMARY KEY (id)
);

CREATE UNIQUE INDEX ix_users_email ON users (email);

CREATE INDEX ix_users_id ON users (id);

INSERT INTO alembic_version (version_num) VALUES ('ebe73c35ab17') RETURNING alembic_version.version_num;

-- Running upgrade ebe73c35ab17 -> 9ddde3c77625

CREATE TABLE orders (
    id SERIAL NOT NULL, 
    description VARCHAR(100), 
    user_id INTEGER, 
    PRIMARY KEY (id), 
    FOREIGN KEY(user_id) REFERENCES users (id)
);

CREATE INDEX ix_orders_id ON orders (id);

UPDATE alembic_version SET version_num='9ddde3c77625' WHERE alembic_version.version_num = 'ebe73c35ab17';

COMMIT;

