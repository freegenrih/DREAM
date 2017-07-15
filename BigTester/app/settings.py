import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='GHRRich',
                             db='BigTester',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

