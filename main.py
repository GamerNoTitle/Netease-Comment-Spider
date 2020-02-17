import requests as r
import json as js
import csv
import os
import datetime
from array import array
import time
start_Pro=datetime.datetime.now()
def create_csv(path):
    with open(path,"w+",newline="",encoding='utf8') as file:    # 打开文件，也相当于一个回车，避免覆盖文档
        csv_file = csv.writer(file)
        head = heads # 创建csv表头
        csv_file.writerow(head)
def append_csv(path):
    with open(path,"a+",newline='',encoding="utf8") as file:
        csv_file = csv.writer(file)
        data = [inputs]
        csv_file.writerows(data)
def read_config():
    with open("config.json") as json_file:
        config = js.load(json_file)
    return config
conf = read_config()
path = conf['path'] # 设定输出路径/文件
num = int(conf["times"])    # 设定抓取次数
delay = int(conf["delay"])  # 设定抓取后延迟
timeout = int(conf['timeout'])  # 设定超时时间
heads = []
if(conf['song_id']): heads.append('song_id')
heads.append('title')
heads.append('author')
if(conf['album']): heads.append('album')
if(conf['description']): heads.append('description')
if(conf['pub_date']): heads.append('pub_date')
heads.append('comment_id')
heads.append('comment_username')
heads.append('content')
if(conf['comment_user_id']): heads.append('comment_user_id')
if(conf['comment_pub_date']): heads.append('comment_pub_date')
# 检测config.json文件并设定表头
# ========================================
create_csv(path)    # 创建csv文件
temp=array('i',[0]) # 去重复用的临时列表
i = 1
while True:
    if(i==num+1): break
    time.sleep(delay)
    print("---------------------------------------------------")
    print("正在调用api……")
    res = r.get("https://www.mouse123.cn/api/163/api.php",timeout=timeout)  # 调用api
    data = res.json()   # 转化为json字符串
    temp_minus=len(temp)-1     # 获取temp中的元素数量，因为定义的时候给了一个元素，所以要剪掉这个元素
    if temp_minus!=0:
        t=1
        print("正在检测是否抓取过结果……")
        for t in range(len(temp)):
            if(int(data["comment_id"])==temp[t]):
                print("发现已经抓取到的结果，正在丢弃……")
                break
            elif(t==len(temp)-1):
                print("未抓取过的结果，正在存入文件……")
                inputs = []
                if(conf['song_id']): inputs.append(data['song_id'])
                inputs.append(data['title'].encode('gbk'))
                inputs.append(data['author'].encode('gbk'))
                if(conf['album']): inputs.append(data['album'].encode('gbk'))
                if(conf['description']): inputs.append(data['description'].encode('gbk'))
                if(conf['pub_date']): inputs.append(data['pub_date'])
                inputs.append(data['comment_id'])
                inputs.append(data["comment_nickname"].encode('gbk'))
                inputs.append(data['comment_content'].encode('gbk'))
                if(conf['comment_user_id']): inputs.append(data['comment_user_id'])
                if(conf['comment_pub_date']): inputs.append(data['comment_pub_date'])
                append_csv(path)
                temp.append(int(data["comment_id"]))
                end_Pro=datetime.datetime.now()
                print("已完成数量："+str(i)+'，已经用时：'+str(end_Pro-start_Pro))
                i=i+1
                break
    else:
        inputs = []
        if(conf['song_id']): inputs.append(data['song_id'])
        inputs.append(data['title'].encode('gbk'))
        inputs.append(data['author'].encode('gbk'))
        if(conf['album']): inputs.append(data['album'].encode('gbk'))
        if(conf['description']): inputs.append(data['description'].encode('gbk'))
        if(conf['pub_date']): inputs.append(data['pub_date'])
        inputs.append(data['comment_id'])
        inputs.append(data["comment_nickname"].encode('gbk'))
        inputs.append(data['comment_content'].encode('gbk'))
        if(conf['comment_user_id']): inputs.append(data['comment_user_id'])
        if(conf['comment_pub_date']): inputs.append(data['comment_pub_date'])
        append_csv(path)
        temp.append(int(data["comment_id"]))
        end_Pro=datetime.datetime.now()
        print("已完成数量："+str(i)+'，已经用时：'+str(end_Pro-start_Pro))
        i=i+1

