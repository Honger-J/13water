import itertools
import re
import requests
import json


class Poker:
    def __init__(self, string):
        self.cards = []  # 黑桃$、梅花*、方块#、红桃&
        self.max = [0, []]
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
            self.cards.append([i, j])
            if re.search(' ', string) is None:
                break
            string = string[re.search(' ', string).span()[1]:]
        self.cards.sort(reverse=True)

    def solve(self):
        card_1 = list(itertools.combinations(self.cards, 5))
        for card_a in card_1:  # card_a为后墩
            card_2 = self.del_5(card_a, self.cards.copy())  # card_2为除去后墩所余牌
            score_a, val_a = Judge(card_a).score_BM()

            card_3 = list(itertools.combinations(card_2, 5))
            for card_b in card_3:  # card_b为中墩
                score_b, val_b = Judge(card_b).score_BM()
                if val_b > val_a:  # 中后倒水
                    continue
                card_c = self.del_5(card_b, card_2.copy())  # card_c为前墩
                score_c, val_c = Judge(card_c).score_F()
                if val_c > val_b:  # 前中倒水
                    continue
                score = score_c + score_a + score_b

                if score > self.max[0]:
                    self.max[0] = score
                    self.max[1] = [card_c, card_b, card_a]

    def del_5(self, cards1, cards2):  # delete cards1 from cards2
        for i in cards1:
            cards2.remove(i)
        return cards2

    def trans(self, card):
        transtr_1 = ['$', '*', '#', '&']
        transtr_2 = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return transtr_1[card[1] - 1] + transtr_2[card[0] - 2]

    def maxoutp(self):
        card = [
            self.trans(self.max[1][0][0]) + ' ' + self.trans(self.max[1][0][1]) + ' ' + self.trans(self.max[1][0][2]),

            self.trans(self.max[1][1][0]) + ' ' + self.trans(self.max[1][1][1]) + ' ' + self.trans(
                self.max[1][1][2]) + ' ' +
            self.trans(self.max[1][1][3]) + ' ' + self.trans(self.max[1][1][4]),

            self.trans(self.max[1][2][0]) + ' ' + self.trans(self.max[1][2][1]) + ' ' + self.trans(
                self.max[1][2][2]) + ' ' +
            self.trans(self.max[1][2][3]) + ' ' + self.trans(self.max[1][2][4])]
        return card


class Judge:
    def __init__(self, card):
        self.card = card

    def score_BM(self):  # 中后墩
        x = self.tonghuashun()
        if x != 0:
            return ((x - 6) * 4 + 2613324) / 2613360 * 2, x + 160
        x = self.zhadan()
        if x != 0:
            return ((x - 2) * 48 + 2612700) / 2613360 * 1.5, x + 140
        x = self.hulu()
        if x != 0:
            return ((x - 2) * 288 + 2608956) / 2613360 * 1.2, x + 120
        x = self.tonghua()
        if x != 0:
            return ((x - 2) * 396 + 2603808) / 2613360, x + 100
        x = self.shunzi()
        if x != 0:
            return ((x - 6) * 1024 + 2594592) / 2613360, x + 80
        x = self.santiao_5()
        if x != 0:
            return ((x - 2) * 4224 + 2539680) / 2613360, x + 60
        x = self.erdui()
        if x != 0:
            return ((x - 2) * 9504 + 2416128) / 2613360, x + 40
        x = self.duizi_5()
        if x != 0:
            return ((x - 2) * 84480 + 1317888) / 2613360, x + 20
        else:  # 散牌
            return ((self.card[0][0] - 2) + (self.card[1][0] - 2) * 0.1 + (self.card[2][0] - 2) * 0.01 + (
                    self.card[3][0] - 2) * 0.001 + (self.card[4][0] - 2) * 0.0001) * 101376 / 2613360, self.card[0][0] + \
                   self.card[1][0] * 0.1 + self.card[2][0] * 0.01 + self.card[3][0] * 0.001 + self.card[4][0] * 0.0001

    def score_F(self):  # 前墩
        x = self.santiao_3()
        if x != 0:
            return ((x - 2) * 4 + 22048) / 22090, x + 60
        x = self.duizi_3()
        if x != 0:
            return ((x - 2) * 288 + 18304) / 22090, x + 20
        else:
            return ((self.card[0][0] - 2) + (self.card[1][0] - 2) * 0.1 + (self.card[2][0] - 2) * 0.01) * 1408 / 22090, \
                   self.card[0][0] + self.card[1][0] * 0.1 + self.card[2][0] * 0.01

    def tonghuashun(self):
        for i in range(4):
            if self.card[i][0] - self.card[i + 1][0] != 1 or self.card[i][1] != self.card[i + 1][1]:
                return 0
        return self.card[0][0]

    def zhadan(self):
        if self.card[1][0] == self.card[3][0] and (
                self.card[0][0] == self.card[1][0] or self.card[3][0] == self.card[4][0]):
            return self.card[1][0]
        return 0

    def hulu(self):
        if (self.card[0][0] == self.card[1][0] and self.card[2][0] == self.card[4][0]) or (
                self.card[0][0] == self.card[2][0] and self.card[3][0] == self.card[4][0]):
            return self.card[2][0]
        return 0

    def tonghua(self):
        for i in range(4):
            if self.card[i][1] != self.card[i + 1][1]:
                return 0
        return self.card[0][0]

    def shunzi(self):
        for i in range(4):
            if self.card[i][0] - self.card[i + 1][0] != 1:
                return 0
        return self.card[0][0]

    def santiao_5(self):
        if self.card[0][0] == self.card[2][0] or self.card[1][0] == self.card[3][0] or self.card[2][0] == self.card[4][
            0]:
            return self.card[2][0]
        return 0

    def erdui(self):
        if (self.card[0][0] == self.card[1][0] and self.card[2][0] == self.card[3][0]) or (
                self.card[0][0] == self.card[1][0] and self.card[3][0] == self.card[4][0]) or (
                self.card[1][0] == self.card[2][0] and self.card[3][0] == self.card[4][0]):
            return self.card[1][0]
        return 0

    def duizi_5(self):
        for j in range(2):
            if self.card[j][0] == self.card[j + 1][0]:
                return self.card[j][0]
        return 0

    def santiao_3(self):
        if self.card[0][0] == self.card[1][0] and self.card[1][0] == self.card[2][0]:
            return self.card[0][0]
        return 0

    def duizi_3(self):
        if self.card[0][0] == self.card[1][0] or self.card[1][0] == self.card[2][0]:
            return self.card[1][0]
        return 0


#  login
url = 'http://api.revth.com/auth/login'
form_data = {
    "username": 'czh',
    "password": '123456'
}
headers = {
    "Content-Type": 'application/json',
}
response = requests.post(url=url, headers=headers, data=json.dumps(form_data), verify=False)
dicts = dict(json.loads(response.text))
token = dicts["data"]["token"]
print(dicts)
print(token)

#  start game
n = 0
while 1:
    n += 1
    print(n)
    if n == 50:
        break

    response = requests.post(url='http://www.revth.com:12300/game/open',
                             headers={"X-Auth-Token": token})
    dicts = dict(json.loads(response.text))
    print(dicts)
    s = dicts["data"]["card"]
    # s = input()
    poker = Poker(s)
    poker.solve()
    print(poker.maxoutp())
    outp = json.dumps({"card": poker.maxoutp()})

    outp = json.dumps({"id": dicts["data"]["id"], "card": poker.maxoutp()})
    response = requests.post(url='http://api.revth.com/game/submit', data=outp,
                             headers={"X-Auth-Token": token, "Content-Type": "application/json"})
    dicts = dict(json.loads(response.text))
    print(dicts)
