# coding=gbk

from student import *


class StudentManager(object):
    def __init__(self):
        # 存储数据所用的列表
        self.student_list = []

    # 一. 程序入口函数，启动程序后执行的函数
    def run(self):
        # 1. 加载学员信息
        self.load_student()

        while True:
            # 2. 显示功能菜单
            self.show_menu()

            # 3. 用户输入功能序号
            menu_num = int(input('请输入您需要的功能序号：'))

            # 4 根据用户输入的功能序号执行不同的功能
            if menu_num == 1:
                # 添加学员
                self.add_student()
            elif menu_num == 2:
                # 删除学员
                self.del_student()
            elif menu_num == 3:
                # 修改学员信息
                self.modify_student()
            elif menu_num == 4:
                # 查询学员信息
                self.search_student()
            elif menu_num == 5:
                # 显示所有学员信息
                self.show_student()
            elif menu_num == 6:
                # 保存学员信息
                self.save_student()
            elif menu_num == 7:
                # 退出系统
                break

    # 二. 定义功能函数

    # staticmethod用于修饰类中的方法, 使其可以在不创建类实例的情况下调用方法，这样做的好处是执行效率比较高
    # https://www.cnblogs.com/longyi2020/p/14451406.html
    @staticmethod
    def show_menu():
        print('请选择如下功能-----------------')
        print('1:添加学员')
        print('2:删除学员')
        print('3:修改学员信息')
        print('4:查询学员信息')
        print('5:显示所有学员信息')
        print('6:保存学员信息')
        print('7:退出系统')

    def add_student(self):
        name = input('请输入您的姓名')
        gender = input('请输入您的性别')
        tel = input('请输入您的手机号')

        student = Student(name, gender, tel)
        self.student_list.append(student)
        print(self.student_list)
        print(student)

    def del_student(self):
        del_name = input('请输入要删除的学员的姓名：')
        for i in self.student_list:
            if i.name == del_name:
                print('删除成功')
                self.student_list.remove(i)
                break
        else:
            print('查无此人！')

        print(self.student_list)

    def modify_student(self):
        modify_name = input('请输入要修改的学员的姓名：')
        for i in self.student_list:
            if i.name == modify_name:
                i.name = input('请输入学员姓名：')
                i.gender = input('请输入学员性别：')
                i.tel = input('请输入学员手机号：')
                print(f'修改该学员信息成功，姓名{i.name},性别{i.gender}, 手机号{i.tel}')
                break
        else:
            print('查无此人！')

    def search_student(self):
        search_name = input('请输入要查询的学员的姓名：')
        for i in self.student_list:
            if i.name == search_name:
                print(f'姓名{i.name},性别{i.gender}, 手机号{i.tel}')
                break
        else:
            print('查无此人!')

    def show_student(self):
        # ‘\t’的作用：让数据紧跟在制表符后面输出
        print('姓名\t性别\t手机号')
        for i in self.student_list:
            print(f'{i.name}\t{i.gender}\t{i.tel}')

    def save_student(self):
        f = open('student.data', 'w')

        # 注意1：文件写入的数据不能是学员对象的内存地址，需要把学员数据转换成列表字典数据再做存储
        new_list = [i.__dict__ for i in self.student_list]
        # [{'name': 'aa', 'gender': 'nv', 'tel': '111'}]
        print(new_list)

        # 注意2：文件内数据要求为字符串类型，故需要先转换数据类型为字符串才能文件写入数据
        f.write(str(new_list))

        f.close()

    def load_student(self):
        # 尝试以"r"模式打开数据文件，文件不存在则提示用户；文件存在（没有异常）则读取数据
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            data = f.read()

            # 文件中读取的数据都是字符串且字符串内部为字典数据，故需要转换数据类型再转换字典为对象后存储到学员列表
            # eval()方法会解析传入该方法的表达式，并且会在程序中运行解析后的表达式。换句话说，它会将一个字符串解析成代码来执行
            new_list = eval(data)
            self.student_list = [Student(i['name'], i['gender'], i['tel']) for i in new_list]

        # finally块不被执行的情况，总共有3种：不进入try块、程序中止、线程中止(带finally块的是守护线程，其非守护线程都执行完毕)
        finally:
            f.close()
