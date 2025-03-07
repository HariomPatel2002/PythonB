BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 7359376f73ec

CREATE TABLE users (
    id SERIAL NOT NULL, 
    name VARCHAR(100), 
    email VARCHAR(100), 
    PRIMARY KEY (id)
);

CREATE UNIQUE INDEX ix_users_email ON users (email);

CREATE INDEX ix_users_id ON users (id);

DROP TABLE amity;

DROP TABLE bitkraft;

INSERT INTO alembic_version (version_num) VALUES ('7359376f73ec') RETURNING alembic_version.version_num;

COMMIT;

