#coding=gbk

class Student(object):
    # ��python�з����������__xxxx__()�ģ���ô��������Ĺ��ܣ���˽�����ħ��������
    def __init__(self, name, gender, tel):
        self.name = name
        self.gender = gender
        self.tel = tel

    # ��ʹ��print��������ʱ��ֻҪ�Լ�������__str__(self)��������ô�ͻ��ӡ�������������return������
    # __str__������Ҫ����һ���ַ�������������������д
    def __str__(self):
        # Python��ʽ���ַ����ļ��ַ�ʽ���
        # https://blog.csdn.net/m0_46090675/article/details/109690238
        return f'{self.name}, {self.gender}, {self.tel}'

# ����
stu1 = Student('chenshunpeng', 'boy', 123456789)
print(stu1)