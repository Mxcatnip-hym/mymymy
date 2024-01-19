import time

start_time = time.time()

for _ in range(1000000):
    pass

end_time = time.time()

execution_time = end_time - start_time

print(f"程序执行时间为: {execution_time} 秒")
