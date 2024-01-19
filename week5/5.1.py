Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def is_prime(a):
...     if a < 2:
...         return False
...     for i in range(2, int(a**0.5) + 1):
...         if a % i == 0:
...             return False
...     return True
... 
>>> num = int(input("请输入一个数字："))
... if is_prime(num):
...     print(f"{num} 是质数。")
... else:
