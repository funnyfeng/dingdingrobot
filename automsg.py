#coding=utf-8
import json
import requests
import time
import pymysql
import pandas
def auto_reminder():
	urllist=['https://oapi.dingtalk.com/robot/send?access_token=cd21bda78f38abe8f048306069cb4de0ea7e3473af8f5a60bc81569008ad33d4',#测试群
	'https://oapi.dingtalk.com/robot/send?access_token=560ebb6ff479642d52d5154f9ad8c0a7542f2418cd37efd60b7b4d6436bd8a8d',#测试群
	'https://oapi.dingtalk.com/robot/send?access_token=9a9c38f7d2c5fbeee1d0dc96e617a331af508f4d7b9615819a76c1f887597947',#测试群
	'https://oapi.dingtalk.com/robot/send?access_token=21fff84b161792f6bb8c85c219f10ef6a7e0390e4c56ab626f52ef515d56dfb6'#PM群
	]
	print(type(urllist))
	con={"msgtype":"text","text":{"content":"请各PM检查今天的任务完成情况，10分钟后截止汇总发出，谢谢"}}
	print(type(con))
	jd=json.dumps(con)
	head={'Content-Type':'application/json','charset':'utf-8'}
	for x in urllist:
		r=requests.post(x,data=jd,headers=head)
		time.sleep(10)
	print(r.url)
	print(r.status_code,r.reason)
	print(r.content)


# def select_data():
# 	conn=pymysql.Connect(host='127.0.0.1',port=3306,user='root',passwd='',db='zentao',charset='utf8')
# 	cur=conn.cursor()
# 	sql='select zp.name,zt.name,zt.status,zt.eststarted,zt.deadline,zt.assignedto from `zt_task` as zt inner join `zt_project` as zp on zt.project=zp.id where zt.deadline<curdate() and zt.deadline>"0000-00-00"and zt.status in ("wait","doing","pause")'
# 	cur.execute(sql)
# 	row=cur.fetchall()
# 	# tasklist=pandas.read_sql(sql,conn)
# 	for dr in row:
# 		print(dr)
# 	print("query,ok")
# 	return row
if __name__ == '__main__':
	# select_data()
	auto_reminder()
