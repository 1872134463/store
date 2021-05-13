import pymysql
# 连接的四大参数，写死
host="localhost"
user="root"
password="root"
database="bank"
class DBUtils:
# 专门针对于增，删，改
    def update(self,sql,param):
        # 2. 获取连接
        con = pymysql.connect(host=host,user=user,password=password,database=database)
        # 3. 创建游标
        cursor = con.cursor()
        # 4.执行sql
        cursor.execute(sql,param)
        # 5.提交
        con.commit()
        # 6.关闭
        cursor.close()
        con.close()

    # 专门针对于查询
    def select(self,sql,param):
        # 2. 获取连接
        con = pymysql.connect(host=host, user=user, password=password, database=database)
        # 3. 创建游标
        cursor = con.cursor()
        # 4.执行sql
        cursor.execute(sql, param)
        # 5.提交
        con.commit()
        #6.返回数据
        return cursor.fetchall()
        # 6.关闭
        cursor.close()
        con.close()
