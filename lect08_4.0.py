#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
功能：模拟掷骰子，新增模拟投掷两个骰子，新增可视化投掷两个骰子，新增直方图可视化掷两个色子
日期：2018.10.16
版本：4.0
"""
import random
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

def roll_dice():
    """
    模拟掷骰子
    """
    roll = random.randint(1,6)
    return roll

def main():
    """
    主函数
    """
    total_times = 10000

    #记录骰子的结果
    roll_list = []


    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()
        roll_list.append(roll1 + roll2)

    #数据可视化

    plt.hist(roll_list,bins=range(2,14),normed=1,edgecolor='black',linewidth=1)
    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('频率')
    plt.show()

if __name__ == '__main__':
    main()