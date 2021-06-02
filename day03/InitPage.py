'''

只准备页面的操作数据


'''
class InitPageData:
    success_data=[
    {"username":"jason","password":"admin","expect":"Student Login"}
    ]
    password_error_data=[
        {
         "username":"jason",
            "password":"admin1",
            "expect":"账户名错误或密码错误!别瞎弄!"
            }
    ]