BEGIN;

-- Running upgrade 7359376f73ec -> b9e3d0d72ef1

ALTER TABLE users ADD COLUMN age INTEGER;

UPDATE alembic_version SET version_num='b9e3d0d72ef1' WHERE alembic_version.version_num = '7359376f73ec';

COMMIT;

