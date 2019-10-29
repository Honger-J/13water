import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import QtCore
from 排行榜 import *
import requests
import json


class Ranklist(QMainWindow, Ui_ranklist):
    def __init__(self):
        super(Ranklist, self).__init__()
        self.setupUi(self)


'''url = 'http://api.revth.com/rank'
response = requests.get(url=url, verify=False)
tmp_list = list(json.loads(response.text))
app=QApplication(sys.argv)
ranklist=Ranklist()
ranklist.name1.setText(tmp_list[0]['name'])
ranklist.score1.setText(str(tmp_list[0]['score']))
ranklist.show()
sys.exit(app.exec_())'''


class obb(object):
    def fuc(self):
        url = 'http://api.revth.com/auth/login'
        form_data = {
            "username": 'wayne',
            "password": '123456'
        }
        headers = {
            "Content-Type": 'application/json',
        }
        response = requests.post(url=url, headers=headers, data=json.dumps(form_data), verify=False)
        print(response.text)
        tmp_dict = dict(json.loads(response.text))
        global T_oken
        global userid
        T_oken = tmp_dict['data']['token']
        userid = tmp_dict['data']['user_id']


if __name__ == '__main__':
    obbb = obb()
    obbb.fuc()
    url = 'http://api.revth.com/history'
    headers = {
        "X-Auth-Token": T_oken
    }
    form_data = {
        "player_id": userid,
        "limit": 10,
        "page": 0
    }
    response = requests.get(url=url, params=form_data, headers=headers)
    print(response.text)
    tmp_list = dict(json.loads(response.text))
    print(tmp_list)
    print(str(tmp_list['data'][0]['score']))
    print(str(tmp_list['data'][0]['card']))
    '''self.score2.setText(str(tmp_list[1]['score']))
    self.history2.setText(str(tmp_list[1]['card']))
    self.score3.setText(str(tmp_list[2]['score']))
    self.history3.setText(str(tmp_list[2]['card']))
    self.score4.setText(str(tmp_list[3]['score']))
    self.history4.setText(str(tmp_list[3]['card']))
    self.show()'''
