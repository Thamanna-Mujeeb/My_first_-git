import pymysql

connection = pymysql.connect(
     host = 'localhost',
     user = 'python_app_new',
     password = 'python@123',
     database = 'camerin_students_2',
     port = 3306
)

def get_data():
        query = """
            SELECT * FROM students
            WHERE student_id = 102 
        """ 
        cursor.execute(query) 
        print("== Orginal Data ==") 
        return (cursor.fetchone()) 

try:
     with connection.cursor() as cursor:
        
        print('==original data==')
        print(get_data())

        cursor.execute("""
        UPDATE students SET city = %s
        where student_id = %s
        """, ('Delhi', 102))
        print('==after update==(before commit)==')
        print(get_data())
        connection.commit()
        print('==after commit==')
        print(get_data())

        # cursor.execute("""
        # UPDATE students SET city = %s
        # where student_id = %s
        # """, ('Thrissur', 102))
        # print('==after second update==(before rollback)==')
        # print(get_data())
        # connection.rollback()
        # print('==after rollback==')
        # print(get_data())

except Exception as e:
    print(f"error: {e}")
finally:
    connection.close()
    print("operation completed")


# except Exception as e:
#      print(f"Error : {e}") 
# finally:
#      connection.close() 
#      print("Operations completed")   python -m 