# -*- coding: utf-8 -*-
from fix_qt_import_erro import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from 初始界面 import *
from 登录界面 import *
from 注册界面 import *
from 游戏大厅 import *
from 开始游戏 import *
from 分墩 import *
from 出牌成功 import *
from AI import *
from 个人中心 import *
from 排行榜 import *
from 游戏规则1 import *
from 游戏规则2 import *
from 登录反馈1 import *
from 超时 import *
from 注册成功 import *
from 学号已绑定 import *
from 用户名已被使用 import *
from 教务处认证失败 import *
from 历史详情 import *
import json
import requests


# 初始界面
class First_window(QMainWindow, Ui_firstwindow):
    def __init__(self):
        super(First_window, self).__init__()
        self.setupUi(self)
        self.dian_ci_jin_ru.clicked.connect(self.btnClick)

    def btnClick(self):
        self.close()


# 登录界面
class Loginwindow(QMainWindow, Ui_login_window):
    def __init__(self):
        super(Loginwindow, self).__init__()
        self.setupUi(self)
        self.zhu_ce.clicked.connect(self.btnClick)

    def btnClick(self):
        self.close()

    def loginfeedback(self):
        account = self.zhang_hao.text()
        password = self.mi_ma.text()

        url = 'http://api.revth.com/auth/login'
        form_data = {
            "username": account,
            "password": password
        }
        headers = {
            "Content-Type": 'application/json',
        }
        response = requests.post(url=url, headers=headers, data=json.dumps(form_data), verify=True)
        print(response.text)
        tmp_dict = dict(json.loads(response.text))
        global T_oken
        global userid
        global name
        T_oken = tmp_dict['data']['token']
        userid = tmp_dict['data']['user_id']
        var = tmp_dict['status']
        if var == 0:
            gamehall.show()
            name = self.zhang_hao.text()
            self.close()
        elif var == 1005:
            loginfeedback1.exec()
        elif var == 2006:
            overtime.exec()
            overtime_btn = overtime.return_2
            overtime_btn.clicked.connect(login_window.show)


# 登录反馈1
class Loginfeedback1(QDialog, Ui_login_feedback1):
    def __init__(self):
        super(Loginfeedback1, self).__init__()
        self.setupUi(self)
        self.return_2.clicked.connect(self.btnClick)

    def btnClick(self):
        self.close()


# 超时提醒
class Overtime(QDialog, Ui_overtime):
    def __init__(self):
        super(Overtime, self).__init__()
        self.setupUi(self)
        self.return_2.clicked.connect(self.btnClick)

    def btnClick(self):
        self.close()


# 注册界面
class Registerwindow(QMainWindow, Ui_register_window):
    def __init__(self):
        super(Registerwindow, self).__init__()
        self.setupUi(self)
        self.deng_lu.clicked.connect(self.btnClick)

    def btnClick(self):
        self.close()

    def RegisterandBind(self):
        account = self.zhang_hao.text()
        password = self.mi_ma.text()
        jwc_account = self.xue_hao.text()
        jwc_password = self.jwc_mima.text()

        url = 'http://www.revth.com:12300/auth/register2'
        form_data = {
            "username": account,
            "password": password,
            "student_number": jwc_account,
            "student_password": jwc_password
        }
        headers = {
            "Content-Type": 'application/json',
        }
        response = requests.post(url=url, headers=headers, data=json.dumps(form_data), verify=True)
        print(response.text)
        tmp_dict = dict(json.loads(response.text))
        var = tmp_dict['status']
        if var == 0:
            register_success.exec()
        elif var == 1001:
            account_used.exec()
        elif var == 1002:
            stunum_used.exec()
        elif var == 1003:
            jwc_failed.exec()


# 注册成功
class Register_success(QDialog, Ui_register_success):
    def __init__(self):
        super(Register_success, self).__init__()
        self.setupUi(self)
        self.return_to_login.clicked.connect(self.btnClick)

    def btnClick(self):
        self.close()
        regsiter_window.close()


# 用户名已被使用
class Account_used(QDialog, Ui_account_used):
    def __init__(self):
        super(Account_used, self).__init__()
        self.setupUi(self)
        self.return_to_register.clicked.connect(self.btnClick)

    def btnClick(self):
        self.close()


# 学号已绑定
class Stunum_used(QDialog, Ui_stunum_used):
    def __init__(self):
        super(Stunum_used, self).__init__()
        self.setupUi(self)
        self.return_to_register.clicked.connect(self.btnClick)

    def btnClick(self):
        self.close()


# 教务处认证失败
class Jwc_failed(QDialog, Ui_jwc_failed):
    def __init__(self):
        super(Jwc_failed, self).__init__()
        self.setupUi(self)
        self.return_to_register.clicked.connect(self.btnClick)

    def btnClick(self):
        self.close()


# 游戏大厅
class Gamehall(QMainWindow, Ui_game_hall):
    def __init__(self):
        super(Gamehall, self).__init__()
        self.setupUi(self)
        self.you_xi_gui_ze.clicked.connect(self.btnClick)
        self.kai_shi_you_xi.clicked.connect(self.btnClick)
        self.ge_ren_zhong_xin.clicked.connect(self.btnClick)
        self.pai_hang_bang.clicked.connect(self.btnClick)

    def btnClick(self):
        self.close()


# 开始游戏
class Startgame(QMainWindow, Ui_Startgame):
    def __init__(self):
        super(Startgame, self).__init__()
        self.setupUi(self)
        self.buttonfendun.clicked.connect(self.btnClick)

    def btnClick(self):
        self.close()

    def showPoker(self):
        url = 'http://www.revth.com:12300/game/open'
        headers = {"X-Auth-Token": T_oken}
        response = requests.post(url=url, headers=headers)
        dicts = dict(json.loads(response.text))
        print(dicts)
        s = dicts["data"]["card"]
        global idd
        idd = dicts["data"]["id"]
        global poker
        poker = Poker(s)
        self.mypuke_1.setStyleSheet(
            "border-image: url(:/.../puke/" + str(poker.cards[0][0]) + str(poker.cards[0][1]) + ".png);")
        self.mypuke_2.setStyleSheet(
            "border-image: url(:/.../puke/" + str(poker.cards[1][0]) + str(poker.cards[1][1]) + ".png);")
        self.mypuke_3.setStyleSheet(
            "border-image: url(:/.../puke/" + str(poker.cards[2][0]) + str(poker.cards[2][1]) + ".png);")
        self.mypuke_4.setStyleSheet(
            "border-image: url(:/.../puke/" + str(poker.cards[3][0]) + str(poker.cards[3][1]) + ".png);")
        self.mypuke_5.setStyleSheet(
            "border-image: url(:/.../puke/" + str(poker.cards[4][0]) + str(poker.cards[4][1]) + ".png);")
        self.mypuke_6.setStyleSheet(
            "border-image: url(:/.../puke/" + str(poker.cards[5][0]) + str(poker.cards[5][1]) + ".png);")
        self.mypuke_7.setStyleSheet(
            "border-image: url(:/.../puke/" + str(poker.cards[6][0]) + str(poker.cards[6][1]) + ".png);")
        self.mypuke_8.setStyleSheet(
            "border-image: url(:/.../puke/" + str(poker.cards[7][0]) + str(poker.cards[7][1]) + ".png);")
        self.mypuke_9.setStyleSheet(
            "border-image: url(:/.../puke/" + str(poker.cards[8][0]) + str(poker.cards[8][1]) + ".png);")
        self.mypuke_10.setStyleSheet(
            "border-image: url(:/.../puke/" + str(poker.cards[9][0]) + str(poker.cards[9][1]) + ".png);")
        self.mypuke_11.setStyleSheet(
            "border-image: url(:/.../puke/" + str(poker.cards[10][0]) + str(poker.cards[10][1]) + ".png);")
        self.mypuke_12.setStyleSheet(
            "border-image: url(:/.../puke/" + str(poker.cards[11][0]) + str(poker.cards[11][1]) + ".png);")
        self.mypuke_13.setStyleSheet(
            "border-image: url(:/.../puke/" + str(poker.cards[12][0]) + str(poker.cards[12][1]) + ".png);")
        self.show()


# 分墩
class Fendun(QMainWindow, Ui_Fendun):
    def __init__(self):
        super(Fendun, self).__init__()
        self.setupUi(self)
        self.buttonchupai.clicked.connect(self.btnClick)

    def btnClick(self):
        pass

    def showpoker(self):
        poker.solve()
        self.mypuke_1.setStyleSheet(
            "border-image: url(:/.../puke/" + str(poker.max[1][0][0][0]) + str(poker.max[1][0][0][1]) + ".png);")
        self.mypuke_2.setStyleSheet(
            "border-image: url(:/.../puke/" + str(poker.max[1][0][1][0]) + str(poker.max[1][0][1][1]) + ".png);")
        self.mypuke_3.setStyleSheet(
            "border-image: url(:/.../puke/" + str(poker.max[1][0][2][0]) + str(poker.max[1][0][2][1]) + ".png);")
        self.mypuke_4.setStyleSheet(
            "border-image: url(:/.../puke/" + str(poker.max[1][1][0][0]) + str(poker.max[1][1][0][1]) + ".png);")
        self.mypuke_5.setStyleSheet(
            "border-image: url(:/.../puke/" + str(poker.max[1][1][1][0]) + str(poker.max[1][1][1][1]) + ".png);")
        self.mypuke_6.setStyleSheet(
            "border-image: url(:/.../puke/" + str(poker.max[1][1][2][0]) + str(poker.max[1][1][2][1]) + ".png);")
        self.mypuke_7.setStyleSheet(
            "border-image: url(:/.../puke/" + str(poker.max[1][1][3][0]) + str(poker.max[1][1][3][1]) + ".png);")
        self.mypuke_8.setStyleSheet(
            "border-image: url(:/.../puke/" + str(poker.max[1][1][4][0]) + str(poker.max[1][1][4][1]) + ".png);")
        self.mypuke_9.setStyleSheet(
            "border-image: url(:/.../puke/" + str(poker.max[1][2][0][0]) + str(poker.max[1][2][0][1]) + ".png);")
        self.mypuke_10.setStyleSheet(
            "border-image: url(:/.../puke/" + str(poker.max[1][2][1][0]) + str(poker.max[1][2][1][1]) + ".png);")
        self.mypuke_11.setStyleSheet(
            "border-image: url(:/.../puke/" + str(poker.max[1][2][2][0]) + str(poker.max[1][2][2][1]) + ".png);")
        self.mypuke_12.setStyleSheet(
            "border-image: url(:/.../puke/" + str(poker.max[1][2][3][0]) + str(poker.max[1][2][3][1]) + ".png);")
        self.mypuke_13.setStyleSheet(
            "border-image: url(:/.../puke/" + str(poker.max[1][2][4][0]) + str(poker.max[1][2][4][1]) + ".png);")
        self.show()


# 出牌成功
class Success(QDialog, Ui_Success):
    def __init__(self):
        super(Success, self).__init__()
        self.setupUi(self)
        self.button_return.clicked.connect(self.btnClick)

    def btnClick(self):
        self.close()
        fendun.close()

    def submit(self):
        outp = json.dumps({"id": idd, "card": poker.maxoutp()})
        response = requests.post(url='http://api.revth.com/game/submit', data=outp,
                                 headers={"X-Auth-Token": T_oken, "Content-Type": "application/json"})
        print(dict(json.loads(response.text)))
        self.show()


# 个人中心
class Personcenter(QMainWindow, Ui_personcenter):
    def __init__(self):
        super(Personcenter, self).__init__()
        self.setupUi(self)
        self.buttonfanhui.clicked.connect(self.btnClick)

    def btnClick(self):
        self.close()

    def showhistory(self):
        url = 'http://api.revth.com/history'
        form_data = {
            "player_id": userid,
            "limit": 10,
            "page": 0
        }
        headers = {
            "X-Auth-Token": T_oken
        }
        response = requests.get(url=url, params=form_data, headers=headers)
        print(response.text)
        tmp_list = dict(json.loads(response.text))
        print(tmp_list)
        self.namelabel.setText(name)
        self.ID_1.setText(str(tmp_list['data'][0]['id']))
        self.score1.setText(str(tmp_list['data'][0]['score']))
        self.history1.setText(str(tmp_list['data'][0]['card']))
        self.ID_2.setText(str(tmp_list['data'][1]['id']))
        self.score2.setText(str(tmp_list['data'][1]['score']))
        self.history2.setText(str(tmp_list['data'][1]['card']))
        self.ID_3.setText(str(tmp_list['data'][2]['id']))
        self.score3.setText(str(tmp_list['data'][2]['score']))
        self.history3.setText(str(tmp_list['data'][2]['card']))
        self.ID_4.setText(str(tmp_list['data'][3]['id']))
        self.score4.setText(str(tmp_list['data'][3]['score']))
        self.history4.setText(str(tmp_list['data'][3]['card']))
        self.show()


# 排行榜
class Ranklist(QMainWindow, Ui_ranklist):
    def __init__(self):
        super(Ranklist, self).__init__()
        self.setupUi(self)
        self.buttonfanhui.clicked.connect(self.btnClick)

    def btnClick(self):
        self.close()

    def showrank(self):
        url = 'http://api.revth.com/rank'
        response = requests.get(url=url, verify=False)
        tmp_list = list(json.loads(response.text))
        self.name1.setText(tmp_list[0]['name'])
        self.score1.setText(str(tmp_list[0]['score']))
        self.name2.setText(tmp_list[1]['name'])
        self.score2.setText(str(tmp_list[1]['score']))
        self.name3.setText(tmp_list[2]['name'])
        self.score3.setText(str(tmp_list[2]['score']))
        self.name4.setText(tmp_list[3]['name'])
        self.score4.setText(str(tmp_list[3]['score']))
        self.name5.setText(str(tmp_list[4]['name']))
        self.score5.setText(str(tmp_list[4]['score']))
        self.show()


# 游戏规则1
class Rulewindow1(QMainWindow, Ui_rulewindow1):
    def __init__(self):
        super(Rulewindow1, self).__init__()
        self.setupUi(self)
        self.nextpage.clicked.connect(self.btnClick)

    def btnClick(self):
        self.close()


# 游戏规则2
class Rulewindow2(QMainWindow, Ui_rulewindow2):
    def __init__(self):
        super(Rulewindow2, self).__init__()
        self.setupUi(self)
        self.return_2.clicked.connect(self.btnClick)

    def btnClick(self):
        self.close()


def find(string):
    cards = []
    while string is not None:
        if string[1] == 'A':
            i = 14
        elif string[1] == 'J':
            i = 11
        elif string[1] == 'Q':
            i = 12
        elif string[1] == 'K':
            i = 13
        else:
            i = int(re.search('[0-9]+', string).group())
        if string[0] == '$':
            j = 1
        elif string[0] == '*':
            j = 2
        elif string[0] == '#':
            j = 3
        else:  # &
            j = 4
        cards.append([i, j])
        if re.search(' ', string) is None:
            break
        string = string[re.search(' ', string).span()[1]:]
    return cards


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建具体对象
    firstwindow = First_window()
    login_window = Loginwindow()
    loginfeedback1 = Loginfeedback1()
    overtime = Overtime()
    regsiter_window = Registerwindow()
    register_success = Register_success()
    account_used = Account_used()
    stunum_used = Stunum_used()
    jwc_failed = Jwc_failed()
    gamehall = Gamehall()
    startgame = Startgame()
    fendun = Fendun()
    success = Success()
    personcenter = Personcenter()
    ranklist = Ranklist()
    rulewindow1 = Rulewindow1()
    rulewindow2 = Rulewindow2()

    # 初始界面
    first_btn = firstwindow.dian_ci_jin_ru
    first_btn.clicked.connect(login_window.show)
    firstwindow.show()

    # 登录界面
    login_btn1 = login_window.zhu_ce
    login_btn1.clicked.connect(regsiter_window.show)
    login_btn2 = login_window.login_button
    login_btn2.clicked.connect(login_window.loginfeedback)

    # 登录结果反馈
    loginfeedback1_btn = loginfeedback1.return_2
    loginfeedback1_btn.clicked.connect(login_window.show)

    # 注册界面
    regsiter_btn1 = regsiter_window.deng_lu
    regsiter_btn1.clicked.connect(login_window.show)
    register_btn2 = regsiter_window.register_button
    register_btn2.clicked.connect(regsiter_window.RegisterandBind)

    # 注册成功
    register_success_btn = register_success.return_to_login
    register_success_btn.clicked.connect(login_window.show)

    # 用户名已被使用
    account_used_btn = account_used.return_to_register
    account_used_btn.clicked.connect(regsiter_window.show)

    # 学号已绑定
    stunum_used_btn = stunum_used.return_to_register
    stunum_used_btn.clicked.connect(regsiter_window.show)

    # 教务处认证失败
    jwc_failed_btn = jwc_failed.return_to_register
    jwc_failed_btn.clicked.connect(regsiter_window.show)

    # 游戏大厅
    gamehall_startbtn = gamehall.kai_shi_you_xi
    gamehall_personbtn = gamehall.ge_ren_zhong_xin
    gamehall_rulebtn = gamehall.you_xi_gui_ze
    gamehall_rankbtn = gamehall.pai_hang_bang
    # 开始游戏按键
    gamehall_startbtn.clicked.connect(startgame.showPoker)
    # 个人中心按键
    gamehall_personbtn.clicked.connect(personcenter.showhistory)
    # 游戏规则按键
    gamehall_rulebtn.clicked.connect(rulewindow1.show)
    # 排行榜按键
    gamehall_rankbtn.clicked.connect(ranklist.showrank)

    # 开始游戏
    startgame.buttonfendun.clicked.connect(fendun.showpoker)

    # 分墩
    fendun.buttonchupai.clicked.connect(success.submit)

    # 出牌成功
    success.button_return.clicked.connect(gamehall.show)

    # 个人中心
    personcenter_btn = personcenter.buttonfanhui
    personcenter_btn.clicked.connect(gamehall.show)

    # 排行榜
    ranklist_btn = ranklist.buttonfanhui
    ranklist_btn.clicked.connect(gamehall.show)

    # 游戏规则1
    rulewindow1_btn = rulewindow1.nextpage
    rulewindow1_btn.clicked.connect(rulewindow2.show)

    # 游戏规则2
    rulewindow2_btn = rulewindow2.return_2
    rulewindow2_btn.clicked.connect(gamehall.show)

    sys.exit(app.exec_())
