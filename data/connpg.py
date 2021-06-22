import psycopg2
import re
from psycopg2 import extras as ex
import json

def pc():
    with open("./data.json", "r", encoding="utf8")as fp:
        json_data = json.load(fp)
        #print('这是文件中的json数据：', json_data)
        #print('这是读取到文件数据的数据类型：', type(json_data))
        return json_data


def insert1(x):
    # 获得连接
    conn = psycopg2.connect(database="university", user="postgres", password="123456", host="localhost", port="5432")
    # 获得游标对象
    cursor = conn.cursor()
    # 获取单条数据.
    print(x[1]['lineid'],x[2]['schoolname'])
    datalist = []
    for i in range(len(x)):
        v1 = v2 = v3 = v4 = False
        a = re.search('一流大学', x[i]['type'])
        b = re.search('一流学科', x[i]['type'])
        c = re.search('985', x[i]['type'])
        d = re.search('211', x[i]['type'])
        if a:
            v1 = True
        if b:
            v2 = True
        if c:
            v3 = True
        if d:
            v4 = True
        datalist.append((x[i]['lineid'],x[i]['lineid'],x[i]['code'],x[i]['schoolname'],x[i]['province'],x[i]['city'], x[i]['department'],x[i]['level'], x[i]['type'],v1, v2, v3, v4, False , x[i]['link']))
    sql = '''insert into school(school_id,school_serial,school_code,school_name,school_zone,school_city,school_department,school_level,school_type,is_firstuniversity,is_firstdiscipline,is_985,is_211,is_del,school_link)
             values %s'''

    ex.execute_values(cursor, sql, datalist, page_size=100)
    # 关闭数据库连接
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    a=pc()
    insert1(a)
