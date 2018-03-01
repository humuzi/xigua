# coding =utf-8
import os

def get_file(path="D:\\xxx",rule=".py"):
    all =[]
    for dirpath,dirname,filename in os.walk(path):  #os.walk()获得所有的目录
        for f in filename:
            fs = os.path.join(dirpath,f)   #获得所有文件的名称
            if fs.endswith(rule):
                all.append(fs)
    return all

if __name__ == '__main__':
    b=get_file(r"D:\\Python")
    for i in b:
        print(i)