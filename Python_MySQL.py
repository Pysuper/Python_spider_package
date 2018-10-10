### 连接数据库
import pymysql

sql = pymysql.connect(
    host='localhost',  # 主机名
    user='root',  # 用户名
    passwd='root',  # 密码
    db='DB',  # 数据库名
    port=3306,  # 端口
    charset='utf8'  # 编码
)

cursor = sql.cursor()
cursor.execute('select * from demo1')
print(cursor.fetchall())


### 输入提交数据库
import requests
import re
import pymysql

# 连接数据库
sql = pymysql.connect(
    host = 'localhost',     # 主机名
    user = 'root',          # 用户名
    password = 'root',      # 用户密码
    db = 'DB',              # 连接使用的数据库名
    port = 3306,            # 端口号
    charset = 'gbk'         # 编码方式
)

def getsql():

    # 获取网页源码
    url = ''
    get = requests.get(url)
    # print(get)

    #　使用正则表达式选择有用的代码
    re_get = r''
    re_get_text = re.findall(re_get)
    # print(re_get_text)

    # set 去重
    re_get_text = set(re_get_text)
    # print(re_get_text)

    # 使用for循环，取出列表中的数据
    for i in re_get_text:
        print(i)

    # 创建游标，写入SQL语句
    cursor = sql.cursor()
    cursor.execute('select * from demo1')

    # 显示写入SQL语句后的MySQL数据库
    print(cursor.fetchall())

    # 提交执行SQL语句
    sql.commit()

# 调用函数，执行函数内的代码
getsql()
