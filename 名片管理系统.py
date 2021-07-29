
usr_list = [
    {'name': 'zhangsan', 'tel': '1555', 'qq': '6666', 'email': '8888'},
    {'name': 'lisi', 'tel': '555', 'qq': '666', 'email': '8888'},
    {'name': 'wanger', 'tel': '55566', 'qq': '8888', 'email': '66666'}
]

def shuoming():
    print('---------------------------')
    print('      名片管理系统 V1.0       ')
    print('1：添加名片')
    print('2：删除名片')
    print('3：修改名片')
    print('4：查询名片')
    print('5：退出系统')
    print('---------------------------')

def usr_add():
    name = input("请输入姓名：")
    for usr in usr_list:
        if name in usr['name']:
            print("已经有此用户，请重新输入！")
    else:
        tel = input("请输入电话：")
        qq = input("请输入QQ号：")
        email = input("请输入你的邮箱：")
        usr = {'name':name,'tel':tel,'qq':qq,'email':email}
        usr_list.append(usr)
    print(usr_list)

def check_number(n):
    if n.isdigit():
        n = int(n)
        if 0 <= n <len(usr_list):
            return True
    return False

def usr_del():
    number = input("请输入要删除的序号：")
    is_valid = check_number(number)
    if is_valid:
        answer = input("你确定要删除这个人吗？（yes or no):").lower()
        if answer == 'yes':
            usr_list.pop(int(number))
            print('删除用户成功，请进行下一步操作！')
    else:
        print("你输入的序号不合法！")
        usr_del()
    print(usr_list)


def usr_up():
    number = input("请输入你要更新信息的编号：")
    answer = input("你确定要更新这个人的信息吗？（yes or no):").lower()

    if answer == 'yes':
        is_vilid = check_number(number)

        if is_vilid:
            print("1:你要更新这个人全部信息")
            print("2:更新这个人部分信息")
            ans = int(input("请输入你要进行的操作:"))
            if ans == 1:
                usr = usr_list[int(number)]
                print("你要修改用户的原信息为:姓名:{name},手机号:{tel},QQ号:{qq},email:{email}".format(**usr))
                new_name = input("请输入新的用户名:")
                for usr in usr_list:
                    if new_name in usr['name']:
                        print("已经有此用户，请重新输入！")
                        break
                else:
                    new_tel = input("请输入新的tel:")
                    new_qq = input("请输入新的QQ号:")
                    new_email = input("请输入新的email:")
                    usr['name'] = new_name
                    usr['tel'] = new_tel
                    usr['qq'] = new_qq
                    usr['email'] = new_email
            elif ans == 2:
                print("1:更新手机号")
                print("2:更新QQ号")
                print("3:更新email")
                ans1 = int(input("请输入你要进行的操作:"))
                if ans1 == 1:
                    print(number)
                    usr = usr_list[int(number)]
                    print("你要修改用户的原信息为:姓名:{name},手机号:{tel},QQ号:{qq},email:{email}".format(**usr))
                    new_tel = input("请输入新的手机号:")
                    usr['tel'] = new_tel
                elif ans1 == 2:
                    usr = usr_list[int(number)]
                    print("你要修改用户的原信息为:姓名:{name},手机号:{tel},QQ号:{qq},email:{email}".format(**usr))
                    new_qq = input("请输入新的QQ号:")
                    usr['tel'] = new_qq
                elif ans1 == 3:
                    usr = usr_list[int(number)]
                    print("你要修改用户的原信息为:姓名:{name},手机号:{tel},QQ号:{qq},email:{email}".format(**usr))
                    new_email = input("请输入新的email:")
                    usr['tel'] = new_email
                else:
                    print("对不起，没有此操作！")
            else:
                print("对不起，没有此操作！")
        else:
            print("对不起，你输入的编号有误，请重新输入！")
            usr_up()
    print(usr_list)


def usr_search():
    print('1:看个人信息')
    print('2:查看全部信息')
    number = int(input('请输入你要进行的操作:'))
    if number == 1:
        name = input("请输入你要查看人的名字:")
        for usr in usr_list:
            if name in usr['name']:
                print("你要查询人的信息为:姓名:{name},手机号:{tel},QQ号:{qq},email:{email}".format(**usr))
                break
        else:
            print("对不起没有你要查询的用户！")
    elif number == 2:
        print('序号   姓名      手机号      QQ         email')
        for i, usr in enumerate(usr_list):
            print(i, usr['name'].center(12), usr['tel'].center(6), usr['qq'].center(10), usr['email'].center(13))
    else:
        print("对不起，你输入有误，请重新操作！")
        usr_search()


def usr_quit():
    choice = (input("你真的要进行退出吗？（づ￣3￣）づ╭❤(yes or no):")).lower()
    if choice == 'yes':
        exit()
def start():
    while True:
        shuoming()
        m = int(input("请输入你就要进行操作的数字："))
        if m == 1:
            usr_add()
        elif m == 2:
            usr_del()
        elif m == 3:
            usr_up()
        elif m == 4:
            usr_search()
        elif m == 5:
            usr_quit()
        else:
            print("用户输入错误，没有此功能！")


if __name__ == '__main__':
    start()


