# SQL

SQL engines are heavy-duty spreadsheets that can do a lot of complex things.

## Schema

- What are datatypes?
- What is schema?
- How do we use datatypes to create a database/table schema?

## Basic Operations

Connect

| Command | PostgreSQL | SQLite | MySQL |
|---|---|---|---|
| Connect | `psql -U $USER -h $HOST -W` | `sqlite3 $FILE` | `mysql -u $USER -h $HOST -p` |
| Change Database | `\c database_name` | `sqlite3 $FILE` | `USE $DATABASE` |

Discover
| Engine | Databases | Tables | Table Schemas |
|---|---|---|---|
| PostgreSQL | `\l` | `\dt` | `\d+ $TABLE` |
| SQLite | `file $FILE \| grep -i sqlite` | `.tables` | `.schema $TABLE` |
| MySQL | `SHOW DATABASES` | `SHOW TABLES` | `DESCRIBE $TABLE` |

Preferences
| Option | PostgreSQL | SQLite |
|---|---|---|
| Result Pagination | `\pset pager` | `-` |
| Tabular/Vertical Results | `\x` | `-` |

## CRUD

There are a lot of ways to use SQL. Most software applications use SQL by following the CRUD pattern. "CRUD" are the four basic operations of persistent data storage.

- Create
- Read
- Update
- Delete

## Create

| Operation | Command |
|---|---|
| Create a Database | `CREATE DATABASE my_database;` |
| Create a Table | `CREATE TABLE my_table ( id text PRIMARY KEY DEFAULT gen_random_uuid(), val text )` |
| Create a Row | `INSERT INTO my_table (id, val) VALUES ('my-new-id', 'my new value with text or numbers 1234!')` |

### Create a Database
This will create a basic database inside of an SQL environment. The database is the way the engine segments tables together.
```sql
CREATE DATABASE my_database;
```

### Create a Table
This will be a basic key-value storage table named `my_key_value`
It will have four columns
- A primary key, `id`
- A text value, `val`
- A timestamp indicating when the record was created, `created_at`
- A status, `status`
```sql
CREATE TABLE my_key_value (
	id text PRIMARY KEY DEFAULT gen_random_uuid(),
	val text NOT NULL,
	created_at timestamp DEFAULT now(),
	status integer NOT NULL DEFAULT 100
);

-- Copy a table
CREATE TABLE my_key_value_NEW FROM TEMPLATE my_key_value;
```

### Create a Row
This will create a row in the table.
```sql
INSERT INTO my_key_value (val, status) VALUES (
	'this is my new value, the value on the next line is what will go into the status column',
	202
)
```

## Read

| Operation | Command |
|---|---|
| Read all tables | See the "Discover" options in the [Basic Operations](#basic-operations) section |
| Read all rows | `SELECT * FROM my_table` |

Read a Row
```sql
-- Read all rows, no filter
SELECT * FROM my_key_value;

-- Filter Options:
-- Using `WHERE`
SELECT * FROM my_key_value WHERE id = 'my-new-id';
SELECT * FROM my_key_value WHERE status > 200;
SELECT * FROM my_key_value WHERE status = 202;
SELECT * FROM my_key_value WHERE status != 202;

-- Using `ORDER BY`, defaults to ASC (small to large, old to new)
SELECT * FROM my_key_value ORDER BY created_at DESC;

-- Using `LIMIT`
SELECT * FROM my_key_value LIMIT 1;

-- Using `GROUP BY` with an aggragate function, date_trunc
SELECT COUNT(id)
	, date_trunc(created_at, 'day') AS created_at
FROM my_key_value
GROUP BY created_at
ORDER BY created_at DESC;

-- Paginating results using `OFFSET` and `LIMIT`
SELECT * FROM my_key_value LIMIT 10 OFFSET  0;
SELECT * FROM my_key_value LIMIT 10 OFFSET 10;
SELECT * FROM my_key_value LIMIT 10 OFFSET 20;

-- Searching Text
-- Using `LIKE` (case-sensitive) and `ILIKE` (case-insensitive)
SELECT * FROM my_key_value WHERE val LIKE '%new%';
SELECT * FROM my_key_value WHERE val ILIKE '%NEW%';
```

## Update

Update a Database
```sql
ALTER DATABASE my_database RENAME TO my_new_database;
```

Update a Table
```sql
ALTER TABLE my_key_value RENAME TO my_new_key_value;
ALTER TABLE my_key_value ALTER COLUMN status SET DEFAULT 0;

ALTER TABLE my_key_value ADD COLUMN meta jsonb;
ALTER TABLE my_key_value ALTER COLUMN meta SET NOT NULL;
ALTER TABLE my_key_value DROP COLUMN meta;
```

Update a Row

## Delete

Delete a Database
```sql
DROP DATABASE my_database
```

Delete a Table
```sql
DROP TABLE my_key_value;
```

Delete a Row
```sql
DELETE FROM my_key_value WHERE id = 'my-new-id';

-- Using `WHERE`
-- This is valid, but often comes with unintended side effects.
-- Try to always use strict equality against the primary key for delete
-- The next best option is to use the `IN` operator
DELETE FROM my_key_value WHERE status > 200;

-- Using `IN`
-- Delete rows from a set of values
DELETE FROM my_key_value WHERE id IN ('my-new-id', 'my-other-id', 'oh-here-is-another-id');
-- This is the same as the folllowing 4 commands:
DELETE FROM my_key_value WHERE id = 'my-new-id';
DELETE FROM my_key_value WHERE id = 'my-other-id';
DELETE FROM my_key_value WHERE id = 'oh-here-is-another-id';

```