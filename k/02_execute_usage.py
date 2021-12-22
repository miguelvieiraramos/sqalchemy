from engine_usage import get_conn, engine
from sqlalchemy import text

connection = get_conn()
stmt = text("select id, name, last_name from person where id=:id")
result = connection.execute(stmt, {"id": 1})
# row = result.first()
# print(row)

for id, name, last_name in result:
    print(id, name, last_name)


result = connection.execute(text("select id, name, last_name from person"))
for id, name, last_name in result.all():
    print(id, name, last_name)

connection.close()

# best way
with engine.connect() as connection:
    stmt = text("select id, name, last_name from person where id=:id")
    result = connection.execute(stmt, {"id": 2})
    for id, name, last_name in result:
        print(id, name, last_name)

#insert
with engine.connect() as connection:
    stmt = text("insert into person(name, last_name) values(:name, :last_name)")
    connection.execute(stmt, {"name": "Foo", "last_name": "Bar"})
    connection.commit() #necessario

#dessa forma não é necessário dar o commit
with engine.begin() as connection:
    stmt = text("insert into person(name, last_name) values(:name, :last_name)")
    connection.execute(stmt, {"name": "Foo", "last_name": "Bar"})
    connection.execute(stmt, {"name": "Naruto", "last_name": "Uzumaki"})