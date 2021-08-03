import random

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from LoginPane import LoginClass
from RegisterPane import RegisterClass
from MainPane import MainClass
from GamePane import Game
from SituationPane import Situation
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.Qt import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

if __name__ == '__main__':

    current_account = ""
    _translate = QtCore.QCoreApplication.translate

    accountMessage = pd.read_excel('Data/Accountdata.xlsx', index_col=0)
    ques1 = pd.read_excel('Data/Question1.xlsx', header=None)
    ques2 = pd.read_excel("Data/Question2.xlsx", header=None)
    ques3 = pd.read_excel("Data/Question3.xlsx", header=None)
    conditions = pd.read_excel("Data/condition.xlsx", index_col=0)

    oneNumber = 0
    twoNumber = 0
    threeNumber = 0

    app = QApplication(sys.argv)
    loginPane = LoginClass()
    registerPane = RegisterClass()

    mainPane = MainClass()
    gamePane = Game()
    situationPane = Situation()


    def check_login(account, pwd):
        if not (account == "" or pwd == ""):
            if not account.isdigit() and account in accountMessage.columns and str(accountMessage[account][0]) == pwd:
                print("登录成功")
                mainPane.show()
                loginPane.hide()
                global current_account
                current_account = account
                _translate = QtCore.QCoreApplication.translate
                mainPane.label_5.setText(_translate("Form", "用户 {} ，已登录！".format(account)))


            else:
                loginPane.show_error_animation()
        else:
            loginPane.show_error_animation()


    def check_register(account, pwd, confirm_pwd):
        if account == "" or pwd == "" or confirm_pwd == "":
            registerPane.notSpace()
        elif account[0].isdigit():
            registerPane.notNumber()
        elif pwd != confirm_pwd:
            registerPane.show_not_equal()
        elif account in accountMessage.columns:
            registerPane.alreadyhad()
        else:
            registerPane.sccess()
            loginPane.show()
            registerPane.hide()
            accountMessage.insert(0, account, [pwd])
            accountMessage.to_excel("Data/Accountdata.xlsx")
            conditions.insert(0, account, [0, 0, 0, 0, 0, 0])
            conditions.to_excel("Data/condition.xlsx")


    def showRegister():
        registerPane.account_le.clear()
        registerPane.password_le.clear()
        registerPane.confirm_pwd_le.clear()
        registerPane.show()
        loginPane.hide()


    def returntoLogin():
        loginPane.name.clear()
        loginPane.pwd.clear()
        loginPane.show()
        registerPane.hide()


    def mainToLogin():
        loginPane.name.clear()
        loginPane.pwd.clear()
        loginPane.show()
        mainPane.hide()


    print(accountMessage)
    mainPane.returnbutton.clicked.connect(mainToLogin)
    loginPane.pushButton.clicked.connect(showRegister)
    loginPane.login_btn.clicked.connect(lambda: check_login(loginPane.name.text(), loginPane.pwd.text()))
    registerPane.pushButton.clicked.connect(
        lambda: check_register(registerPane.account_le.text(), registerPane.password_le.text(),
                               registerPane.confirm_pwd_le.text()))
    registerPane.returnButton.clicked.connect(returntoLogin)


    def view_situation():
        global situationPane
        situationPane = Situation()
        situationPane.returnbutton.clicked.connect(situationToMain)

        global current_account
        details = conditions[current_account].tolist()
        a0 = details[0]
        a1 = details[1]
        b0 = details[2]
        b1 = details[3]
        c0 = details[4]
        c1 = details[5]

        rate1 = 0
        rate2 = 0
        rate3 = 0

        if a1 != 0:
            rate1 = a0 / a1
        if b1 != 0:
            rate2 = b0 / b1
        if c1 != 0:
            rate3 = c0 / c1
        rate = [rate1, rate2, rate3]
        kinds = ["Single choice", "Judgment", "Short ans"]
        situationPane.PrepareTwo(kinds, rate)
        situationPane.PrepareOne(kinds, rate)

        situationPane.show()
        mainPane.hide()


    nowOne = 0
    nowTwo = 0
    nowThree = 0
    all = 0

    ls1 = []
    ls2 = []
    ls3 = []


    class One:
        def __init__(self, str1, a, b, c, d, ans):
            self.ques = str1
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.ans = ans


    class Two:
        def __init__(self, str, ans):
            self.ques = str
            self.ans = ans


    class myThree:
        def __init__(self, str2, ans):
            self.ques = str2
            self.ans = ans


    for i in range(20):
        ll = ques1[i].tolist()
        # print(ll)
        temp = One(ll[0], ll[1], ll[2], ll[3], ll[4], ll[5])
        ls1.append(temp)

        lw = ques2[i].tolist()
        temp = Two(lw[0], lw[1])
        ls2.append(temp)
    for i in range(10):
        la = ques3[i].tolist()
        temp = myThree(la[0], la[1])
        ls3.append(temp)

    template1 = "现在是单选题的第{}题，共{}道单选题，所有题型总计{}道题\n\n"
    template2 = "现在是判断题的第{}题，共{}道判断题，所有题型总计{}道题\n\n"
    template3 = "现在是简答题的第{}题，共{}道简答题，所有题型总计{}道题\n\n"


    def submit_number(one, two, three):
        global oneNumber, nowOne
        global twoNumber, nowTwo
        global threeNumber, nowThree, all, right1, right2, right3
        if one == "" or two == "" or three == "":
            mainPane.notNumber()
        elif not (one.isdigit() and two.isdigit() and three.isdigit()):
            mainPane.notNumber()
        else:
            one = int(one)
            two = int(two)
            three = int(three)
            if one < 1 or two < 1 or three < 1 or two > 20 or one > 20 or three > 20:
                mainPane.notNumber()
            else:
                right1 = 0
                right2 = 0
                right3 = 0
                gamePane.three.clear()
                random.shuffle(ls1)
                random.shuffle(ls2)
                random.shuffle(ls3)
                oneNumber = one
                twoNumber = two
                threeNumber = three
                nowOne = 1
                nowTwo = 0
                nowThree = 0
                all = one + two + three
                print(one, two, three)
                mainPane.success()

                ok1 = template1.format(nowOne, one, all)
                gamePane.label.setText(_translate("Form", ok1 + ls1[nowOne - 1].ques + ":\n\nA. " + ls1[
                    nowOne - 1].a + "\n\nB. " + ls1[nowOne - 1].b + "\n\nC. " + ls1[nowOne - 1].c + "\n\nD. " + ls1[
                                                      nowOne - 1].d + "\n"))
                gamePane.show()
                mainPane.hide()


    def situationToMain():
        mainPane.show()
        situationPane.hide()


    def gameToMain():
        mainPane.one.clear()
        mainPane.two.clear()
        mainPane.three.clear()
        mainPane.show()
        gamePane.hide()


    right1 = 0
    right2 = 0
    right3 = 0


    def check(answer):
        gamePane.three.clear()
        global oneNumber, nowOne
        global twoNumber, nowTwo
        global threeNumber, nowThree, all, right1, right2, right3
        # if nowThree > threeNumber:
        #     global current_account
        #     details = conditions[current_account].tolist()
        #     details[0] += right1
        #     details[1] += oneNumber
        #     details[2] += right2
        #     details[3] += twoNumber
        #     details[4] += right3
        #     details[5] += threeNumber
        #     conditions[current_account] = np.array(details)
        #     print(conditions)
        #     conditions.to_excel("Data/condition.xlsx")
        #     # accountMessage.to_excel("Data/Accountdata.xlsx")
        #     gameToMain()
        if nowOne <= oneNumber:
            ans = ls1[nowOne - 1].ans
            if ans == answer:
                gamePane.right()
                right1 += 1
            else:
                gamePane.wrong(ans)
        elif nowTwo <= twoNumber:
            ans = ls2[nowTwo - 1].ans
            if ans == answer:
                gamePane.right()
                right2 += 1
            else:
                gamePane.wrong(ans)
        elif nowThree <= threeNumber:
            ans = ls3[nowThree - 1].ans
            if ans == answer:
                gamePane.right()
                right3 += 1
            else:
                gamePane.wrong(ans)

        nowOne += 1
        if nowOne > oneNumber:
            nowTwo += 1
            if nowTwo > twoNumber:
                nowThree += 1

        if nowOne <= oneNumber:
            ok1 = template1.format(nowOne, oneNumber, all)
            gamePane.label.setText(_translate("Form",
                                              ok1 + ls1[nowOne - 1].ques + ":\n\nA. " + ls1[nowOne - 1].a + "\n\nB. " +
                                              ls1[nowOne - 1].b + "\n\nC. " + ls1[nowOne - 1].c + "\n\nD. " + ls1[
                                                  nowOne - 1].d + "\n"))
        elif nowTwo <= twoNumber:
            ok1 = template2.format(nowTwo, twoNumber, all)
            gamePane.label.setText(_translate("Form",
                                              ok1 + ls2[nowTwo - 1].ques + "()\n\n"))
        elif nowThree <= threeNumber:
            ok1 = template3.format(nowThree, threeNumber, all)
            gamePane.label.setText(_translate("Form", ok1 + ls3[nowThree - 1].ques))
        else:
            global current_account
            details = conditions[current_account].tolist()
            details[0] += right1
            details[1] += oneNumber
            details[2] += right2
            details[3] += twoNumber
            details[4] += right3
            details[5] += threeNumber
            conditions[current_account] = np.array(details)
            print(conditions)
            conditions.to_excel("Data/condition.xlsx")
            gameToMain()


    gamePane.submit.clicked.connect(lambda: check(gamePane.three.text()))
    gamePane.returnbutton.clicked.connect(gameToMain)
    situationPane.returnbutton.clicked.connect(situationToMain)
    mainPane.submit.clicked.connect(
        lambda: submit_number(mainPane.one.text(), mainPane.two.text(), mainPane.three.text()))
    mainPane.condition.clicked.connect(view_situation)
    loginPane.show()
    sys.exit(app.exec_())
