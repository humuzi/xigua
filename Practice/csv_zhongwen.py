# coding=utf-8
import csv

with open("test.csv","w",newline="") as f:
    writer=csv.writer(f)

data = [u"客户名称","电话","行业"]
writer.writerow(data)

