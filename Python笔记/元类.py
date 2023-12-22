# 元类: 实例化产生类的类
# 把类作为对象
# 元类 --> 实例化 --> 类 --> 实例化 --> 对象

# Human --> 肯定也是调用了某个类
# 每一个关键字的背后对应一系列的功能
# 分析class的底层,是怎么一步步把类造出来的 --> 可以自己造类,高度定制化自己的类

# 用class定义的所有类,以及内置的类,都是由内置的元类type,实例化产生的


# 定义一个类
# class Human:  # 变量名指向的值,才是类,Human只是个名而已,它的背后才是'类'
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print('name:',self.name,'age:',self.age)
        
        

# # 基于类创建对象
# obj = Human('陈',18)

# print(type(obj)) # 用type查看obj的类
# print(type(Human)) # 用type查看Human的类 --> type,也就是说type就是内置的元类
# print(type(str)) # 用type查看内置函数(内置的类)str的类 --> type
# print(Human.__dict__) # 有很多内置的功能


# 分析class是怎么造类的
# Human = type(.....) 一定是调用元类 type 传了一堆参数

# # 1.类名
# class_name = 'name'

# # 2.基类
# class_bases = (object,)

# # 3.类的子代码 -- 类的子代码会在定义阶段执行 -- 产生名称空间
# class_dic= {}
# class_body = '''
# def __init__(self,name,age):
#             self.name = name
#             self.age = age

# def info(self):
#             print('name:',self.name,'age:',self.age)
# '''

# # 把产生的名字传到字典class_dic里 -- 需要用内置函数exec -- 拿名称空间
# exec(class_body,{},class_dic) # 第一个参数传子代码,第二个参数--全局名称空间(这个例子没用到),第三个参数--类的名称空间

# # print(class_dic) # 只有类子代码里面存在的名字 这一点和 Human.__dict__ 做比较

# # 4.调用元类 -- 如果没有指定元类,就默认使用的是type
# Human = type(class_name,class_bases,class_dic)
# # print(Human)


# # 总结 基于这四个步骤,没有用class,也造出了一个类--也就是说,class底层做的事,就是这四步
# obj = Human('陈',18)
# obj.info()

# 作用: 清楚这四个步骤之后,可以对我们定义的类,做定制化操作-->主要针对第四步



# raise  可以主动抛出一个异常  --> raise 报错名称('报错内容')
# raise NameError('类名不能有下划线')

# 自定义元类
# class Mytype(type):               #只有继承了type的类才能是元类
#     def __init__(self,class_name,class_bases,class_dic):
#         # print('Mytype.init')
#         if '_' in class_name:
#             raise NameError('类名不能有下划线')
#         # print(class_dic)
#         if not class_dic.get('__doc__'):
#             raise SyntaxError('定义类必须写注释')
        
# # Human = Mytype(class_name,class_bases,class_dic)
# # 1. 产生一个空对象Human
# # 2. 调用Mytype的init方法
# # 3. 返回初始化好的对象Human

# class Human(object,metaclass=Mytype):# 给Human指定元类,metaclass默认等于的type,也就是默认用的内置的元类
#     '''
#         文档注释
#     '''

#     def __init__(self,name,age):        #如果想要继承其他的类,就写前面(父类),只要保证 metaclass=type 在最后就行
#         self.name = name
#         self.age = age

#     def info(self):
#         print('name:',self.name,'age:',self.age)
        