import pymysql


conn = pymysql.connect(
    host = '114.55.147.226',
    user = 'elifefp-dev',
    password = '45i76727r06h5bikj919f32bhh64a753',
    db = 'elife-fp',
)

try:
    with conn.cursor() as cursor:
        sql = 'select log.mobile , log.vcode from aliyun_send_sms_logs log where log.mobile = %s ORDER BY create_time desc limit 1'
        cursor.execute(sql , ('15123456789'))
        row1 = cursor.fetchone()
        print(row1)
        conn.commit()
finally:
    conn.close()