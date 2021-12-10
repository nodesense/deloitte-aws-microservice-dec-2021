import pymysql.cursors

import pg8000.native
import pg8000 as dbapi
from pprint import pprint


def getconnection(database,host,port,user,password):
    conn= None
    try:
        conn=dbapi.connect(database=database,host=host, port=port,\
            user=user,password=password)
    except Exception as err:
        print(err)
    return conn


def runquery(conn, query):
    """
    Just run a query given a connection
    """
    curr=conn.cursor()
    curr.execute(query)
    for row in curr.fetchall():
        pprint(row)
    return None
    
def lambda_handler(event, context):  
    config={
        "database": "dev",
        "host": "endpoint",
        "port": 5439, # 5432 for postgres
        "user": 'postgres',
        "password": 'password'
    }

    conn = getconnection(config['database'],config['host'],\
            config['port'],config['user'],config['password'])
            
    print("Connected")
    
    runquery(conn,\
            '''
            select * from category
            ;
            ''' )
            
    return "done"
    
