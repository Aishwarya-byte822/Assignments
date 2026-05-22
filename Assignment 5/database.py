# import sqlite3
# conn = sqlite3.connect("college.db")
# print("Database Created")
# conn.close()

# import sqlite3

# conn = sqlite3.connect("college.db")

# conn.execute("""
# CREATE TABLE student(
# st_id INTEGER PRIMARY KEY AUTOINCREMENT,
# st_name VARCHAR(50),
# st_class VARCHAR(20),
# st_email VARCHAR(80)
# )
# """)

# conn.execute("""
# CREATE TABLE teacher(
# t_id INTEGER PRIMARY KEY AUTOINCREMENT,
# t_name VARCHAR(50),
# subject VARCHAR(30)
# )
# """)

# conn.execute("""
# CREATE TABLE course(
# c_id INTEGER PRIMARY KEY AUTOINCREMENT,
# c_name VARCHAR(50),
# fees INTEGER
# )
# """)

# print("Tables Created")

# conn.close()


# import sqlite3

# conn = sqlite3.connect("college.db")

# # insert into student
# conn.execute("""
# INSERT INTO student(st_name, st_class, st_email)
# VALUES('Aish', 'BTech', 'aish@gmail.com')
# """)

# conn.execute("""
# INSERT INTO student(st_name, st_class, st_email)
# VALUES('Raj', 'BCA', 'raj@gmail.com')
# """)

# # insert into teacher
# conn.execute("""
# INSERT INTO teacher(t_name, subject)
# VALUES('Sharma Sir', 'Python')
# """)

# # insert into course
# conn.execute("""
# INSERT INTO course(c_name, fees)
# VALUES('Data Science', 50000)
# """)

# conn.commit()

# print("Records Inserted")

# conn.close()


# select all students
# import sqlite3
# conn=sqlite3.connect("college.db")
# data = conn.execute("select * from student")
# for row in data:
#     print(row)
# conn.close()
    

#  select specific columns
# import sqlite3

# conn = sqlite3.connect("college.db")
# data = conn.execute(
#     "select st_name, st_class from student"
# )
# for row in data:
#     print(row)
# conn.close()    


# order by
# import sqlite3

# conn = sqlite3.connect("college.db")
# data = conn.execute(
#     "select * from student order by st_name DESC"
# )
# for row in data:
#     print(row)

# conn.close()


# limit
# import sqlite3

# conn = sqlite3.connect("college.db")
# data = conn.execute(
#     "select * from student limit 1"
# )
# for row in data:
#     print(row)

# conn.close()


# where condition
# import sqlite3

# conn = sqlite3.connect("college.db")
# data = conn.execute(
#     "select * from student where st_name='Aish'"
# )
# for row in data:
#     print(row)

# conn.close()


# distinct
# import sqlite3

# conn = sqlite3.connect("college.db")
# data = conn.execute(
#     "select distinct st_class from student"
# )
# for row in data:
#     print(row)

# conn.close()



# update data
# import sqlite3

# conn = sqlite3.connect("college.db")

# conn.execute("""
# update student
# set st_name='Aishwarya'
# where st_id=1
# """)

# conn.commit()

# print("Record Updated")

# conn.close()


# delete data
import sqlite3

conn = sqlite3.connect("college.db")

conn.execute("""
delete from student
where st_id=2
""")

conn.commit()

print("Record Deleted")

conn.close()