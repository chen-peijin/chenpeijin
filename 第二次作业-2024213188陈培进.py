#!/usr/bin/env python
# coding: utf-8

# In[5]:


import math

# 定义常量
g = 9.8  # 重力加速度，单位：m/s^2
initial_height = 100  # 初始高度，单位：米

def calculate_rebound(n):
    """
    计算第n次反弹的高度、总经过距离和总运动时间。
    
    参数:
    n -- 反弹次数
    
    返回:
    rebound_height -- 第n次反弹的高度
    total_distance -- 球一共经过的距离
    total_time -- 球运动的总时间
    """
    # 第n次反弹的高度是初始高度的(1/2)^n
    rebound_height = initial_height * (0.5 ** n)
    
    # 总经过距离是初始下落距离加上每次反弹的两倍距离（上升和下降）
    total_distance = initial_height + 2 * sum([initial_height * (0.5 ** i) for i in range(1, n+1)])
    
    # 总时间是初始下落时间加上每次反弹的两倍时间（上升和下降）
    # 每次下落的时间是sqrt(2 * 高度 / g)
    total_time = (math.sqrt(2 * initial_height / g) * (1 + 2 * sum([0.5 ** i for i in range(n)])))
    
    return rebound_height, total_distance, total_time

# 输入反弹次数，10次
n = 10

# 计算结果
rebound_height, total_distance, total_time = calculate_rebound(n)

# 输出结果
print(f"第{n}次反弹的高度: {rebound_height} 米")
print(f"此时球一共经过: {total_distance} 米")
print(f"此时球运动了: {total_time} 秒")

# 输出第n次的数学表达式
print("\n数学表达式:")
print(f"第n次反弹的高度: H_n = {initial_height} * (0.5)^n")
print(f"总经过距离: D_n = {initial_height} + 2 * ({initial_height} * (0.5)^1 + {initial_height} * (0.5)^2 + ... + {initial_height} * (0.5)^n)")
print(f"总运动时间: T_n = sqrt(2 * {initial_height} / {g}) * (1 + 2 * (0.5^1 + 0.5^2 + ... + 0.5^n))")


# In[ ]:




