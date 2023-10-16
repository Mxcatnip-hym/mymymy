#进位制转换
a=int(input("number:"))
m=''
while a>0:
    m+=str(a%2)
    a=a//2
print(m[::-1])

# 生成10到20的随机浮点数
import random
random_float = random.uniform(10, 20)
print(f"随机浮点数: {random_float}")

#正则法验证身份证号是否合法
import re

def validate_id_card(id_card):
    pattern = r"^\d{17}[\dXx]$"
    if re.match(pattern, id_card):
        return True
    else:
        return False

id_card = "130106200109234214"  # 你可以修改这里的身份证号
if validate_id_card(id_card):
    print("身份证号合法")
else:
    print("身份证号不合法")


#链表
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 在链表末尾添加节点
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # 在链表头部插入节点
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 删除节点
    def delete_node(self, key):
        current_node = self.head
        # 处理头节点
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        # 处理非头节点
        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev.next = current_node.next
        current_node = None

    # 查找节点
    def find(self, key):
        current_node = self.head
        while current_node:
            if current_node.data == key:
                return current_node
            current_node = current_node.next
        return None

    # 修改节点数据
    def update_node(self, key, new_data):
        node = self.find(key)
        if node:
            node.data = new_data

    # 打印链表
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")


#1到100间所有偶数
for num in range(2, 101, 2):
    print(num)

#百分制转等级制
score = 85  # 可以修改这里的分数
if score < 60:
    grade = "不合格"
elif 60 <= score <= 74:
    grade = "合格"
elif 75 <= score <= 89:
    grade = "良好"
else:
    grade = "优秀"

print(f"考试成绩为 {score}，等级为 {grade}")


#辗转相除法求最大公约数
n=int(input())
m=int(input())
def fun(n,m):
    temp=n%m
    while temp!=0:
        n=m
        m=temp
        temp=n%m
    return m

print(fun(n,m))

import random
import time

# 随机生成数组并用不同方式排序
# 选择排序
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


# 归并排序
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    return merged


# 测试不同长度的数列排序
for size in [1000, 10000, 100000]:
    random_numbers = random.sample(range(size * 10), size)

    # 选择排序
    start_time = time.time()
    selection_sort(random_numbers.copy())
    selection_time = time.time() - start_time

    # 归并排序
    start_time = time.time()
    merge_sort(random_numbers.copy())
    merge_time = time.time() - start_time

    print(f"数组长度: {size}")
    print(f"选择排序时间: {selection_time:.6f} 秒")
    print(f"归并排序时间: {merge_time:.6f} 秒")
    print("=" * 30)


#按规则用A数组计算B数组
def construct_array(A):
    n = len(A)
    B = [1] * n   # 创建与数组 A 相同长度的新数组 B，并初始化为 1

    # 从左到右计算每个元素左侧所有元素的乘积
    left_product = 1
    for i in range(n):
        B[i] *= left_product
        left_product *= A[i]

    # 从右到左计算每个元素右侧所有元素的乘积，并累乘到数组 B 中
    right_product = 1
    for i in range(n-1, -1, -1):
        B[i] *= right_product
        right_product *= A[i]
    
    return B
