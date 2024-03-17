0x0F. Python - Object-relational mapping

In this project, we will link two amazing worlds: Databases and Python!

In the first part, we will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, we will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

**Without ORM**
```python3
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

**with ORM**
```python3
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```
