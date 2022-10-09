#coding=gbk

# importk可以正常运行但却显示报错的解决方法：
# 在当前存放脚本的文件夹右键，然后 “Mark Directory as” 为 “Sources Root”

from managerSystem import *

if __name__ == '__main__':
    student_manger = StudentManager()
    student_manger.run()