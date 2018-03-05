#coding:utf-8
import csv

# my_file = "D:\\PythonProject\\selenium\\userinfo.csv"
my_file = open('userinfo.csv','rt',encoding='gbk')
data = csv.reader(my_file)
user =[user for user in data]
print(user[0])