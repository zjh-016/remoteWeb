import pymysql


class db_config:
    host = 'rm-cn-rno49osne0006pno.rwlb.rds.aliyuncs.com'
    port = 3306
    user = 'root'
    password = 'Tenxigou74@'
    db = 'remotedatabase'
    cursorclass = pymysql.cursors.DictCursor
    charset = 'utf8mb4'

def getDbConnection():
    conn = pymysql.connect(db=db_config.db,host=db_config.host,port=db_config.port,
                           user=db_config.user,password=db_config.password, cursorclass=db_config.cursorclass,
                           charset=db_config.charset)
    return conn