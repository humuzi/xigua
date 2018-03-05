# coding=utf-8
import time
import threading

def chihuoguo(people):
    print("%s 吃火锅的小伙伴：%s"%(time.ctime(),people))
    time.sleep(1)
    print("%s 吃火锅的小伙伴：%s"%(time.ctime(),people))

class MyThread(threading.Thread):
    def __init__(self,people,name):
        threading.Thread.__init__(self)
        self.people = people
        self.name = name

    def run(self):     # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print("开始线程"+ self.name)
        chihuoguo(self.people)    # 执行任务
        print("结束线程"+self.name)

# 设置线程组
threads=[]

# 创建新线程
thread1 = MyThread("xiaoming","Thread-1")
thread2 = MyThread("xiaozhang","Thread-2")

# 添加到线程组
threads.append(thread1)
threads.append(thread2)

# # 守护线程setDaemon(True),必须在start之前
# # 主线程结束时，子线程强制一起结束
# thread1.setDaemon(True)
# thread2.setDaemon(True)

# 开启线程
for thread in threads:
    thread.start()

# 阻塞主线程，等待子线程结束
for thread in threads:
    thread.join()

time.sleep(0.5)
print("退出主线程")