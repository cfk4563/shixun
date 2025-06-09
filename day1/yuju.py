# # 函数定义
# def greet(name, greeting="Hello"):
#     return f"{greeting}, {name}!"
#
# # a = greet("Alice")
#
# # print(greet("Alice"))  # Hello, Alice!
# print(greet("Bob", "Hi"))  # Hi, Bob!

# # 可变参数
# def sum_numbers(*args):
#     return sum(args)
# print(sum_numbers(1, 2, 3, 4))  #
#
# 匿名函数
# double = lambda x: x * 2
# print(double(5))  # 10


# 高阶函数
def apply_func(func, value):
    return func(value)

print(apply_func(lambda x: x ** 2, 8))  #