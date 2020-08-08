db_connection = sqlite3.connect("HulkPage.db")
cursor = db_connection.cursor()

cursor.execute(
    '''
          CREATE TABLE tasks
          (id INTEGER PRIMARY KEY ASC,
	     title text NOT NULL,
         description text NOT NULL,
         assign text NOT NULL,
         staff text NOT NULL,
         start text NOT NULL,
         end text NOT NULL,
         status text NOT NULL,
         notes text NOT NULL)
          ''' )

db_connection.close()
