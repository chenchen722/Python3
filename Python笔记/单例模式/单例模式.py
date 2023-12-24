# 单例模式 目的: 保证某一个类只能有一个实例对象存在 减少了内存的消耗

# 实现方式:(第一种用的多,以下五种面试多)
# 1 模块
# from 单例模式_模块 import obi
# from 单例模式_模块 import obi
# from 单例模式_模块 import obi
# from 单例模式_模块 import obi



# 2 类装饰器
# def singleton_mode(self):
#     obj = None
#     def wrapper(*args,**kwargs):
#         nonlocal obj
#         if not obj:
#             obj = self(*args,**kwargs)
#         return obj
#     return wrapper

# @singleton_mode    
# class Hero:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# obj = Hero('陈',18)
# obj2 = Hero('陈',19)
# print(obj,obj2)  # 两个内存地址一模一样 --> 说明是同一个对象
     
    

# 3 绑定方法  
# class Hero:
#     obj = None
    
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     @classmethod
#     def get_obj(self,*args,**kwargs):
#         if not self.obj:
#             self.obj = self(*args,**kwargs)
#         return self.obj
    
    
# obj = Hero.get_obj('陈',18)
# obj2 = Hero.get_obj('陈',19)
# print(obj,obj2) # 两个内存地址一模一样
# 4 __new__方法
# class Hero:
#     obj = None
    
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
   
#     def __new__(self,*args,**kwargs):
#         if not self.obj:
#             self.obj = super().__new__(self)
#         return self.obj

# obj = Hero('陈',18)
# obj2 = Hero('陈',19)
# print(obj,obj2) # 两个内存地址一模一样

# 5 元类
class Mytype(type):
    obj = None
    def __call__(self,*args,**kwargs):
        if not self.obj:
            # self.obj = super().__call__(*args,**kwargs)
            # 下面的方法也可以
            self.obj = self.__new__(self)
        self.__init__(self,*args,**kwargs) # 放在判断里面和外面都可以
        return self.obj
    
class fun(metaclass=Mytype):
    pass
class Hero(fun):
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
   
    

obj = Hero('陈',18)
print(obj,obj.__dict__) # 两个内存地址一模一样

obj2 = Hero('陈',19)
print(obj2,obj2.__dict__)# 两个内存地址一模一样
# 6 并发编程