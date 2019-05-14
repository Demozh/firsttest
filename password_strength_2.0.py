#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
功能：判断密码强度,新增循环终止
日期：2018.10.11
版本：2.0
"""
def check_number_exist(password_str):
    """
    判断是否含数字
    """
    has_number = False
    for c in password_str:
        if c.isnumeric():
            has_number = True
            break
    return has_number

def check_letter_exist(password_str):
    """
    判断是否含数字
    """
    has_letter = False
    for c in password_str:
        if c.isalpha():
            has_letter = True
            break
    return has_letter

def main():
    """
    主函数
    """
    try_times = 5

    while try_times > 0:

        password = input('请输入密码：')
        strength_level = 0

        #密码规则1：长度大于8
        if len(password) >= 8:
            strength_level += 1
        else:
            print('密码长度至少要求8位')

        # 密码规则2：包含数字
        if check_number_exist(password):
            strength_level += 1
        else:
            print('密码要求包含数字')

        # 密码规则3：包含字母
        if check_letter_exist(password):
            strength_level += 1
        else:
            print('密码要求包含字母')

        if strength_level == 3:
            print('恭喜，密码强度合格')
            break
        else:
            print('抱歉，密码强度低')
            try_times -= 1
        print()

    if try_times <= 0:
        print('尝试次数过多，密码设置失败')

if __name__ == '__main__':
    main()