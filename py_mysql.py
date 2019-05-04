#!/usr/bin/python3
 
import pymysql
db = pymysql.connect("localhost","root","password","learn_mysql" )
cursor = db.cursor()
sql = '''
  SELECT * 
  FROM  tbl_student_score
  '''
try:
    # 执行SQL语句
    print("sql = ")
    print(sql)
    cursor.execute(sql)
    # 获取所有记录列表
    rows = cursor.fetchall()
    print("rows = ")
    print(rows)

    dict_data = { }  
    for row in rows:
      name = row[1]
      dict_data[name] = [0,0]  # { 'Jane':[0,0],  'micheal':[0,0] ... }

    for row in rows:
        name = row[1]
        cource = row[2]
        score = row[3]
        if cource == 'math':
          dict_data[name][0] = score
        if cource == 'english':
          dict_data[name][1] = score
    print("dict_data = ")
    print(dict_data)


    for key in dict_data:
      if dict_data[key][0]>dict_data[key][1]:
        print(key)
        
except Exception as e:
   print(e)
 
# 关闭数据库连接
db.close()
