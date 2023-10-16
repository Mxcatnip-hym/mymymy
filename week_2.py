#第一题代码思路 
#1.第一步计算n的约数 遍历1到n//2 找到能够整除n的数
#2.计算每个约数对应的另一个数（和为n）
#3.遍历所有数对计算乘积
#4.选择乘积最大的约数对
def find_maximum_product(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [2]
    elif n == 3:
        return [3]
    elif n == 4:
        return [2, 2]
    else:
        threes_count = n // 3
        remainder = n % 3
        if remainder == 1:
            threes_count -= 1
            remainder = 4
        return [3] * threes_count + [remainder]

# 测试
n = 2001
result = find_maximum_product(n)
print("所求的正整数列是：", result)


#2的n次幂计算 所得结果增长速度很快
Python 2.7.16 (default, Feb 28 2021, 12:34:25) 
[GCC Apple LLVM 12.0.5 (clang-1205.0.19.59.6) [+internal-os, ptrauth-isa=deploy on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
i=10
>>> i=10
>>> a=2**i
>>> print a
1024
>>> a=2**20
>>> print a
1048576
>>> a=2**30
>>> print a
1073741824
>>> a=2**40
>>> print a
1099511627776
>>> a=2**50
>>> print a
1125899906842624


#渡河问题
#0没有 1白菜 2羊 3狼 m为东西索引 -1为啥都不带
#条件1：农夫不在的一侧不能同时存在12和23
#条件2:m！=-1则农夫带东西过河 表示农夫所在一侧m所对的东西存在
#1，2，3都到west则跳出循环得到步骤
#最终步骤为1.带羊过 2.不带回 3.带狼过 4.带羊回 5.带蔬菜过 6.不带回 7.带羊过

import random
 
west = [1, 2, 3]       
east = [0] * 3         
take = []
cnt = 0     
 
while True:
    if cnt % 2 == 1 and (3 in west and 2 in west or 2 in west and 1 in west) \
            or cnt % 2 == 0 and (3 in east and 2 in east or 2 in east and 1 in east):
        west = [1, 2, 3]
        east = [0] * 3
        take = []
        cnt = 0
        continue
    m = random.randint(-1, 2)
    take.append(m)
    if m != -1 and west[m] != 0 and cnt % 2 == 0:
        west[m], east[m] = east[m], west[m]    
    elif m != -1 and east[m] != 0 and cnt % 2 == 1:
        west[m], east[m] = east[m], west[m]
    else:
        take[-1] = -1
    if east == [1, 2, 3]:
        break
    cnt += 1
 
lit = ['no', 'vege', 'sheep', 'wolf']
for i in range(len(take)-1):      
    if take[i] == take[i+1]:
        take[i] = take[i+1] = []
while [] in take:
    take.remove([])
for i in take:                    
    print(lit[i+1])


#笨方法求解根号2
def squareroot1():
    c=2
    i=0
    g=0
    for j in range(0,c+1):
        if(j*j>c and g==0):
            g=j-1
        while(abs(g*g-c)>0.0001):
            g+=0.00001
            i=i+1
            print("%d:g = %.5f" % (i,g))
squareroot1()

# 定义牛顿迭代法函数
def newton_method(c, epsilon=1e-10, max_iterations=1000):
    x = 1  # 初始猜测值
    iterations = 0
    while abs(x**3 - c) > epsilon and iterations < max_iterations:
        x = x - (x**3 - c) / (3 * x**2)  # 牛顿迭代式
        iterations += 1
    return x
#起始值g改变会对结果有影响

# 求解 c=10 的三次方根
c = 10
root = newton_method(c)

print(f"{c}的三次方根是：{root}")


#三种方法求pi值

import math

# 方法1：莱布尼茨级数
def leibniz_pi(n):
    approx_pi = 0
    for i in range(n):
        approx_pi += (-1) ** i / (2 * i + 1)
    return approx_pi * 4

# 方法2：马青公式
def machin_pi(n):
    approx_pi = 1
    for i in range(1, n+1):
        approx_pi *= (2 * i)**2 / ((2 * i - 1) * (2 * i + 1))
    return approx_pi * 2

# 方法3：使用 math 模块中的 pi 常数
math_pi = math.pi

# 计算精度（小数点后10位）
precision = 1e-10

# 比较三种方法的效率
n = 1
while True:
    leibniz_result = leibniz_pi(n)
    machin_result = machin_pi(n)
    if abs(leibniz_result - math_pi) < precision and abs(machin_result - math_pi) < precision:
        print(f"莱布尼茨级数近似π值：{leibniz_result:.10f}")
        print(f"马青公式近似π值：{machin_result:.10f}")
        print(f"math模块中π的值:{math_pi:.10f}")
        print(f"计算精度：{precision:.10f}")
        print(f"迭代次数：{n}")
        break
    n += 1


#计算区间上的定积分
import random
import math

# 定义积分函数
def integrand(x):
    return x**2 + 4 * x * math.sin(x)

# 定义蒙特卡罗法计算定积分的函数
def monte_carlo_integration(iterations, a, b):
    count_inside = 0
    for _ in range(iterations):
        x = random.uniform(a, b)
        y = random.uniform(0, integrand(b))  # 上界取积分函数在[2, 3]范围内的最大值
        if 0 <= y <= integrand(x):
            count_inside += 1
    interval_width = b - a
    total_points = iterations
    points_inside = count_inside
    integral_approximation = (points_inside / total_points) * interval_width * integrand(b)
    return integral_approximation

# 设置迭代次数
iterations = 1000000

# 计算定积分的近似值
integral_approximation = monte_carlo_integration(iterations, 2, 3)

print(f"使用蒙特卡罗法估计的定积分近似值：{integral_approximation:.10f}")