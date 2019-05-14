#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math

def save_money_in_week(money_per_week,increase_money,total_week):
    saving = 0
    money_list = []

    for i in range(total_week):
        money_list.append(money_per_week)
        saving = math.fsum(money_list)

        print ('第{}周，存入{}元，账户累计{}元'.format(i + 1,money_per_week,saving))

        money_per_week += increase_money


def main():
    money_per_week = float(input('请输入每周的存入金额： '))
    increase_money = float(input('请输入每周的递增金额： '))
    total_week = int(input('请输入的周数： '))

    save_money_in_week(money_per_week,increase_money,total_week)


if __name__ == '__main__':
    main()