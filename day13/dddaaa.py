from DBUtils import DBUtils
import xlwt
import xlrd
DB = DBUtils()
class DBorExcel:
    tableName = ""
    excelName = ""

    def Db_to_excel(self,tableName,excelName):
        sql = "select * from "+tableName

        data = DB.Select(sql,[])
        # 创建工作表对象
        workbook = xlwt.Workbook(encoding=True)
        # 设置表名
        sheet = workbook.add_sheet(tableName)
        # 写入数据
        num = 0
        num1 = 0
        # 写入表中
        for i in data:
            num = num +1
            for j in i:
                num1 = num1 + 1
                sheet.write(num-1,num1 - 1,j)
            num1 = 0
        workbook.save(excelName)


    def Excel_to_db(self,excelAdress,excelName,tableName):
        #获取工作簿
        wb = xlrd.open_workbook(filename=excelAdress,encoding_override= True)

        # 通过wb获取选项卡
        sheet = wb.sheet_by_name(excelName)

        # 获取行列数据
        rows = sheet.nrows
        ncols = sheet.ncols
        # 获取每行数据
        for i in range(1,rows):
            data = sheet.row_values(i)
            new_data = ["'{}'".format(i) for i in data]
            sql = "insert into {} values({})".format(tableName,','.join(new_data))
            DB.update(sql,[])

c= DBorExcel()
a= c.Excel_to_db(excelAdress="E:\pythonProject1\day13/nb.xlsx",excelName="nb",tableName="users")








































#
# from DBUtils import DBUtils
# import  xlrd
# import xlwt
# db=DBUtils()
# param=[]
# class dddaaa:
#     tablename = ""
#     excelname = " "
#     def  Db_to_excel(self,tablename,excelname) :
#         sql="select * from"+tablename
#         data=db.select(sql,[])
#         hb =xlwt.Workbook(encoding=True)
#         sheet=hb.add_sheet(tablename)
#         num=0
#         num1=0
#         for i in data:
#            num=num+1
#            for j in i:
#             num1=num1+1
#             sheet.write(num-1,num1-1,j)
#            num1=0
#         hb.save(excelname)
#     def Excel_to_db(self,exceladress,excelname,tablename):
#         #获取工作簿
#         wb = xlrd.open_workbook(filename=exceladress,encoding_override= True)
#
#         # 通过wb获取选项卡
#         sheet = wb.sheet_by_name(excelname)
#
#         # 获取行列数据
#         rows = sheet.nrows
#         ncols = sheet.ncols
#         # 获取每行数据
#         for i in range(1,rows):
#             data = sheet.row_values(i)
#             new_data = ["'{}'".format(i) for i in data]
#             sql = "insert into {} values({})".format(tablename,','.join(new_data))
#             db.update(sql,[])
#
#
# c= dddaaa()
# a= c.Excel_to_db(exceladress="E:\pythonProject1\day13/nb.xlsx",excelname="excelname",tablename="users")
