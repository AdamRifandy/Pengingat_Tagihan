import _mysql_connector

def get_db_connection():
    connection = _mysql_connector.connect(
        host="localhost",
        user="root",
        password="",
        database="test_db"
    )
    return connection
