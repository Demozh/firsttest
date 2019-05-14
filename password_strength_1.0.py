#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
功能：判断密码强度
日期：2018.10.10
版本：1.0
"""
def check_number_exist(password_str):
    """
    判断是否含数字
    """
    for c in password_str:
        if c.isnumeric():
            return True
    return False

def check_letter_exist(password_str):
    """
    判断是否含数字
    """
    for c in password_str:
        if c.isalpha():
            return True
    return False

def main():
    """
    主函数
    """
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
    else:
        print('抱歉，密码强度低')

if __name__ == '__main__':
    main()