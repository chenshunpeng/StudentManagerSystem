# coding=gbk

from student import *


class StudentManager(object):
    def __init__(self):
        # �洢�������õ��б�
        self.student_list = []

    # һ. ������ں��������������ִ�еĺ���
    def run(self):
        # 1. ����ѧԱ��Ϣ
        self.load_student()

        while True:
            # 2. ��ʾ���ܲ˵�
            self.show_menu()

            # 3. �û����빦�����
            menu_num = int(input('����������Ҫ�Ĺ�����ţ�'))

            # 4 �����û�����Ĺ������ִ�в�ͬ�Ĺ���
            if menu_num == 1:
                # ���ѧԱ
                self.add_student()
            elif menu_num == 2:
                # ɾ��ѧԱ
                self.del_student()
            elif menu_num == 3:
                # �޸�ѧԱ��Ϣ
                self.modify_student()
            elif menu_num == 4:
                # ��ѯѧԱ��Ϣ
                self.search_student()
            elif menu_num == 5:
                # ��ʾ����ѧԱ��Ϣ
                self.show_student()
            elif menu_num == 6:
                # ����ѧԱ��Ϣ
                self.save_student()
            elif menu_num == 7:
                # �˳�ϵͳ
                break

    # ��. ���幦�ܺ���

    # staticmethod�����������еķ���, ʹ������ڲ�������ʵ��������µ��÷������������ĺô���ִ��Ч�ʱȽϸ�
    # https://www.cnblogs.com/longyi2020/p/14451406.html
    @staticmethod
    def show_menu():
        print('��ѡ�����¹���-----------------')
        print('1:���ѧԱ')
        print('2:ɾ��ѧԱ')
        print('3:�޸�ѧԱ��Ϣ')
        print('4:��ѯѧԱ��Ϣ')
        print('5:��ʾ����ѧԱ��Ϣ')
        print('6:����ѧԱ��Ϣ')
        print('7:�˳�ϵͳ')

    def add_student(self):
        name = input('��������������')
        gender = input('�����������Ա�')
        tel = input('�����������ֻ���')

        student = Student(name, gender, tel)
        self.student_list.append(student)
        print(self.student_list)
        print(student)

    def del_student(self):
        del_name = input('������Ҫɾ����ѧԱ��������')
        for i in self.student_list:
            if i.name == del_name:
                print('ɾ���ɹ�')
                self.student_list.remove(i)
                break
        else:
            print('���޴��ˣ�')

        print(self.student_list)

    def modify_student(self):
        modify_name = input('������Ҫ�޸ĵ�ѧԱ��������')
        for i in self.student_list:
            if i.name == modify_name:
                i.name = input('������ѧԱ������')
                i.gender = input('������ѧԱ�Ա�')
                i.tel = input('������ѧԱ�ֻ��ţ�')
                print(f'�޸ĸ�ѧԱ��Ϣ�ɹ�������{i.name},�Ա�{i.gender}, �ֻ���{i.tel}')
                break
        else:
            print('���޴��ˣ�')

    def search_student(self):
        search_name = input('������Ҫ��ѯ��ѧԱ��������')
        for i in self.student_list:
            if i.name == search_name:
                print(f'����{i.name},�Ա�{i.gender}, �ֻ���{i.tel}')
                break
        else:
            print('���޴���!')

    def show_student(self):
        # ��\t�������ã������ݽ������Ʊ���������
        print('����\t�Ա�\t�ֻ���')
        for i in self.student_list:
            print(f'{i.name}\t{i.gender}\t{i.tel}')

    def save_student(self):
        f = open('student.data', 'w')

        # ע��1���ļ�д������ݲ�����ѧԱ������ڴ��ַ����Ҫ��ѧԱ����ת�����б��ֵ����������洢
        new_list = [i.__dict__ for i in self.student_list]
        # [{'name': 'aa', 'gender': 'nv', 'tel': '111'}]
        print(new_list)

        # ע��2���ļ�������Ҫ��Ϊ�ַ������ͣ�����Ҫ��ת����������Ϊ�ַ��������ļ�д������
        f.write(str(new_list))

        f.close()

    def load_student(self):
        # ������"r"ģʽ�������ļ����ļ�����������ʾ�û����ļ����ڣ�û���쳣�����ȡ����
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            data = f.read()

            # �ļ��ж�ȡ�����ݶ����ַ������ַ����ڲ�Ϊ�ֵ����ݣ�����Ҫת������������ת���ֵ�Ϊ�����洢��ѧԱ�б�
            # eval()�������������÷����ı��ʽ�����һ��ڳ��������н�����ı��ʽ�����仰˵�����Ὣһ���ַ��������ɴ�����ִ��
            new_list = eval(data)
            self.student_list = [Student(i['name'], i['gender'], i['tel']) for i in new_list]

        # finally�鲻��ִ�е�������ܹ���3�֣�������try�顢������ֹ���߳���ֹ(��finally������ػ��̣߳�����ػ��̶߳�ִ�����)
        finally:
            f.close()
