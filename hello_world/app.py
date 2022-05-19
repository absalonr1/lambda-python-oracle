import json
import os
import cx_Oracle


print("conectando con BD")

connection = cx_Oracle.connect(user=str(os.environ['DB_USER']), password=str(os.environ['DB_PASS']),
                               dsn=os.environ['DB_HOST']+":"+str(os.environ['DB_PORT'])+"/"+os.environ['DB_SID'],
                               encoding="UTF-8")



def lambda_handler(event, context):
    print("Entrando en handler")
    cursor = connection.cursor()
    for result in cursor.execute("select nvl(max(last_call_et),0) tiempo from v$session where sql_id='0a47jdg2ta8zm' and status='ACTIVE'"):
        print("result SQL: "+str(result))

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world-6"
        }),
    }
