#coding=gbk

class Student(object):
    # 在python中方法名如果是__xxxx__()的，那么就有特殊的功能，因此叫做“魔法”方法
    def __init__(self, name, gender, tel):
        self.name = name
        self.gender = gender
        self.tel = tel

    # 当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
    # __str__方法需要返回一个字符串，当做这个对象的描写
    def __str__(self):
        # Python格式化字符串的几种方式详解
        # https://blog.csdn.net/m0_46090675/article/details/109690238
        return f'{self.name}, {self.gender}, {self.tel}'

# 测试
stu1 = Student('chenshunpeng', 'boy', 123456789)
print(stu1)