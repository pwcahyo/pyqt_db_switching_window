import sqlite3

def createDatabase():
	try:
		sqliteConnection = sqlite3.connect('Biodata.db')
		cursor = sqliteConnection.cursor()
		sqlite_create_table_query = '''CREATE TABLE TB_Biodata (
	                            nim INTEGER PRIMARY KEY UNIQUE,
	                            nama TEXT NOT NULL,
	                            prodi TEXT NOT NULL,
	                            hobi TEXT NOT NULL);'''

		print("Successfully Connected to SQLite")
		cursor.execute(sqlite_create_table_query)
		sqliteConnection.commit()
		print("SQLite table created")
		cursor.close()

	except sqlite3.Error as error:
	    print("Error while creating a sqlite table", error)
	finally:
	    if sqliteConnection:
	        sqliteConnection.close()
	        print("sqlite connection is closed")

def viewDataFromDB():
	try:
	    sqliteConnection = sqlite3.connect('Biodata.db')
	    cursor = sqliteConnection.cursor()
	    print("Successfully Connected to SQLite")

	    count = cursor.execute(""" SELECT * FROM TB_Biodata """)
	    rows = count.fetchall()

	    return rows

	    print("Get data success ", rows)
	    cursor.close()

	except sqlite3.Error as error:
	    print("Failed to get data into sqlite table", error)
	finally:
	    if sqliteConnection:
	        sqliteConnection.close()
	        print("The SQLite connection is closed")

def insertDatatoDB(*data):
	try:
	    sqliteConnection = sqlite3.connect('Biodata.db')
	    cursor = sqliteConnection.cursor()
	    print("Successfully Connected to SQLite")

	    count = cursor.execute("""INSERT INTO TB_Biodata
	                          (nim, nama, prodi, hobi) 
	                           VALUES 
	                          (?,?,?,?)""",
	                          (int(data[0]),data[1],data[2],data[3]))
	    sqliteConnection.commit()
	    print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
	    cursor.close()

	except sqlite3.Error as error:
	    print("Failed to insert data into sqlite table", error)
	finally:
	    if sqliteConnection:
	        sqliteConnection.close()
	        print("The SQLite connection is closed")

# def deleteDataFromDB(data):
# 	try:
# 	    sqliteConnection = sqlite3.connect('Biodata.db')
# 	    cursor = sqliteConnection.cursor()
# 	    print("Successfully Connected to SQLite")

# 	    count = cursor.execute("""DELETE FROM TB_Biodata
# 	                          WHERE nim=""",
# 	                          (int(data[0]),data[1],data[2],data[3]))
# 	    sqliteConnection.commit()
# 	    print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
# 	    cursor.close()

# 	except sqlite3.Error as error:
# 	    print("Failed to insert data into sqlite table", error)
# 	finally:
# 	    if sqliteConnection:
# 	        sqliteConnection.close()
# 	        print("The SQLite connection is closed")