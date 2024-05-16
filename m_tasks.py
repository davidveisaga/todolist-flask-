import pymysql
#connection
connection = pymysql.connect(host="localhost", user="usr-flask", passwd="Userflask#123", database="db_flask_todo")
cursor = connection.cursor()

#insert
def add_task(texto_tareas):
    cursor.execute("INSERT INTO tasks(id, task) VALUES (DEFAULT, %s)", (texto_tareas))
    connection.commit()
    return 1
# select
def get_task():
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()    
    return rows

