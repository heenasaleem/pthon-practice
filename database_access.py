import pymysql

db = pymysql.connect("localhost", "root", "root", "python")
    

def create_table():
    
    cursor = db.cursor()
    
    sql = """CREATE TABLE Details (
    FIRST_NAME  TEXT NOT NULL,
    LAST_NAME  TEXT,
    AGE INT )"""
    cursor.execute(sql)
    
def insert_table():
    
    cursor = db.cursor()

    sql = """INSERT INTO Details(FIRST_NAME,
       LAST_NAME, AGE)
       VALUES ('Heena', 'Saleem', 24)"""
    try:

        cursor.execute(sql)

        db.commit()
    except:

        db.rollback()

    
def read_table():
    

    cursor = db.cursor()

    sql = '''SELECT * FROM Details'''
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)

    except:
        print("Error: unable to fetch data")
        
def update_table():
    

    cursor = db.cursor()

    sql = """UPDATE Profile SET AGE = AGE -3
                              WHERE First_name = 'Heena'"""
    try:

        cursor.execute(sql)

        db.commit()
    except:

        db.rollback()


create_table()
insert_table()
read_table()
update_table()

db.close()

