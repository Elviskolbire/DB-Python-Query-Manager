""" This is a program to connnect python to  mysql and run various types of queries in a local database server. Such as INSERT, DELETE, DROP, SELECT, SHOW, CREATE etc. These program is complete process of running any queries and handles every error checks in all areas making the code efficient and well rebust. """ 

import mysql.connector as con
import getpass
import logging

#getlogger
logger = logging.getLogger("localhost")

#create handler
file_handler = logging.FileHandler("bug.log_db")

#setlevel
file_handler.setLevel(logging.DEBUG)

#set formatter
formatter = logging.Formatter( "%(asctime)s - %(levelname)s - %(message)s", datefmt = "%m/%d/%y %H:%M:%S" )

#set a formatter file
file_handler.setFormatter(formatter)

#adding the file handler for every log
logger.addHandler(file_handler)

#The main function that request for the name of the host , user and their password to enable access to their database server.
def main():
    loop = False
    while (True): 
	    host = input("Enter host name: ").strip()
	    user = input("Enter user: ").strip()
	    password = getpass.getpass("Enter your password: ")
	    database = input("Enter the name of your database: ").strip()
	    connect = serverconnect(host, user, password, database)
	    while(True):
		    if connect.is_connected():
			    try:
			    	#This displays the list of options to chose from using a corresponding number
			    	choice = int(input("\n*****QUERY OPTIONS*****\n1. Create, Drop, Delete, Truncate, Update, Insert, Grant, Revoke\n2. Read, View, Show\n3. Log into a different user\n4. Exit: "))
			    	
			    except ValueError:
			    	print("\nInvalid input please enter a number: ")
			    	logger.error(f"{ValueError}")
			    	continue
			    if choice == 1:
			    	query = input("Enter your  query: ")
			    	execute(connect, query)
			    elif choice == 2:
			    	query = input("Enter your  query: ")
			    	view_tables(connect, query)
			    	
			    elif choice == 3:
			    	close(connect)
			    	break
			    	
			    elif choice == 4:
			    	print("\nQuiting!!!")
			    	close(connect)
			    	return
			    	
			    else:
			    	print("\nInvalid choice!!!")
			    	continue
			    	
			    if loop != True:
				    exit = ""
				    while(exit not in ["yes","no","y","n"]):
					    exit = ""
					    exit = input("\nDo you want to perform another query? 'yes' or 'no' ").lower()
					    
					    if exit == "yes" or exit == "y":
					    	pass
					    	
					    elif exit == "no" or  exit == "n":
					    	close(connect,)
					    	return
					    	
					    else:
			
					    	print("\nwrong key!")
			     

#These function implements all the logic to sucessfully connect to our server	
def serverconnect(host, user, password,database):
	connection = None
	try:
		connection = con.connect(
		host = host, 
		user = user,
		password = password,
		database = database,
		charset = "utf8mb4",
		collation = "utf8mb4_general_ci"
		)
		print ("Connection to server sucessful")
		
	except con.Error as err:
		 print(f"Was unable to connect to server due to the this error: \"{err}\"")
		 logger.error(f"Was unable to connect to server due to the this error: \"{err}\"")
	return connection

#The query is then executed and commited if data is been manipulated	 		 
def execute(connection1, query):
	cursor = None
	if connection1.is_connected():
		try:
			cursor = connection1.cursor()
			cursor.execute(query)
			#connection1.commit()
			print ("\nQuery has been executed sucessfully")
			
		except con.Error as err:
			connection1.rollback()
			print (f"\nQuery has fail to execute due to an error: \"{err}\"")
			logger.error(f"Query has fail to execute due to an error: \"{err}\"")
	return cursor


#Data is executed and read using this specific function
def view_tables(connection2, query):
	cursor = None
	if connection2.is_connected():
		try:
			cursor = connection2.cursor()
			cursor.execute(query)
			print(cursor.column_names)
			for i in cursor.fetchall():
				print (f"{i}\n")
			logger.info("Query is executed sucessfully ")
			
		except con.Error as view_error:
			print (f"\nAn error just ocurred  ERROR: {view_error}")
			logger.error(f"An error just ocurred  ERROR: {view_error}")
	return cursor

#All connections should use this function to close after every opened connection
def  close(connection):
		try:
			connection.close()
			print ("\nConnection to server and cursor object closed sucessfully")
			
		except con.Error as err:
			print (f"Error: {err}")
			logger.error(f"Error: {err}")

if __name__  ==  "__main__":
		main()
	