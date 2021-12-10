import pymysql.cursors

def lambda_handler(event, context):   
    try:
        connection = pymysql.connect(host='endpoint here',
                                user='admin',
                                password='password here',
                                database='dev',
                                cursorclass=pymysql.cursors.DictCursor)
        print("Connected")
        with connection:
            with connection.cursor() as cursor:
                # Read a single record
                print("read orders")
                sql = "SELECT  1 + 2 as result"
                cursor.execute(sql, ())
                result = cursor.fetchone()
                print(result)
    except Exception as e:
        print("Error while connecting ", e)

    return "Working"
