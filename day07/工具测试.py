from DBUtils import update  # 导入方法
from DBUtils import select
# 增、删、改测试
sql = "insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
param = ["s002","旺财","798946","印度","南京","幸福大街","s002",8900.3,"2021-09-07","日本花旗银行"]


# 查询测试
sql1 = "select * from user  where username = %s"
param1 = ["旺财"]

data = select(sql1,param1)
print(data)
