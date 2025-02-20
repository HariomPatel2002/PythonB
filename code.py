import psycopg2 

try:
    conn = psycopg2.connect(
        dbname = "hari",
        user = "postgres",
        password = "Hariom",
        host = "localhost",
        port = "5432"
    )
    print("Database connected successfully!")

except Exception as e:
    print("error", e)

cur = conn.cursor()

# cur.execute('''
#     CREATE TABLE users(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100),
#     email VARCHAR(100) UNIQUE
#     )
# ''')

# conn.commit()
# cur.close()
# print("Table created successfully!")


# cur.execute("""INSERT INTO users (name ,email) VALUES(%s, %s)
# """,("John Doe", "john@example.com"))
# conn.commit()
# cur.close()
# print("Data inserted successfully!")

# cur.execute("SELECT *from users")
# rows = cur.fetchall()

# for row in rows:
#     print(row)
# cur.close()



# Updating Data 
# cur.execute("UPDATE users SET email = %s WHERE  name = %s",
# ("john.doe@example.com","John Dow"))
# conn.commit()
# cur.close()
# print("Data updated successfully")


# cur.execute("DELETE FROM users WHERE name = %s",('John Doe',))
# conn.commit()
# cur.close()
# print("Data deleted successfully")

conn.commit()
print("Database connection closed")
