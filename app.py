import pymysql

connection = pymysql.connect(
     host = 'localhost',
     user = 'python_app_new',
     password = 'python@123',
     database = 'camerin_students_2',
     port = 3306
)
print("MySQL connection sucessful")

# print(connection.__dict__)

# try:
     # cursor = connection.cursor()  
    #  with connection.cursor() as cursor:
        #cursor.execute("SELECT * FROM students") 
        #records = cursor.fetchall() 
        #print(records)
        #for record in records:
        #print(records)  

        # query = f"""SELECT * 
        #         FROM students 
        #         WHERE city = 'kochi' 
        #         """ 
        # user_input = "' OR '1'= '1" 
        # query = f"""SELECT * FROM students 
        # WHERE s_name = '{user_input}' """ 
          
        # cursor.execute(query)  
        # result = cursor.fetchall() 
        # print(result) 
     
       #username = input() 
       #password = input() 

       #query = f""" 
       #        SELECT * FROM users 
       #       WHERE username = %s
       #        AND password = %s """   

#      query = """ 
#           INSERT INTO students 
#           VALUES (%s,%s,%s,%s) 
#       """ 
#      values = (108,"Akhil","akhil@gmail.com","kochi",)
#      cursor.execute(query,values) 
#      connection.commit()     


# except Exception as e:
#     print("Error : {e}") 
# finally:
#     connection.close()
#     print("Operations completed") 

# try:
#    with connection.cursor() as cursor:
#       query = """ 
#           ALTER TABLE students 
#           ADD COLUMN phone VARCHAR(15) NOT NULL DEFAULT '111' 
#     """ 
#       cursor.execute(query) 
#       connection.commit() 
#       print("Coloumn created succesfully...") 

#       query = "DESC students" 
#       cursor.execute(query) 

#       result = cursor.fetchall() 
#       for col in result:
#        print(col)

# except Exception as e:
#    print(f"Error : {e}") 
# finally:
#    connection.close() 
#    print("Operations completed")                        

# try:
#    with connection.cursor() as cursor:
#       query = """ 
#           ALTER TABLE students 
#           MODIFY phone INT DEFAULT 1111111
#        """   
#       cursor.execute(query) 
#       connection.commit() 
#       print("Coloumn created succesfully...") 

#       query = "DESC students" 
#       cursor.execute(query) 

#       result = cursor.fetchall() 
#       for col in result:
#         print(col)

# except Exception as e:
#    print(f"Error : {e}") 
# finally:
#    connection.close() 
#    print("Operations completed")                                               

try:
   with connection.cursor() as cursor:
      query = """ 
          ALTER TABLE students 
          RENAME COLUMN phone TO contact_number
       """   
      cursor.execute(query) 
      connection.commit() 
      print("Coloumn created succesfully...") 

      query = "DESC students" 
      cursor.execute(query) 

      result = cursor.fetchall() 
      for col in result:
        print(col)

except Exception as e:
   print(f"Error : {e}") 
finally:
   connection.close() 
   print("Operations completed")                        