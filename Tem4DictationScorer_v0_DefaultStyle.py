# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\lenovo\Desktop\tem4dictationproject\draft.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# DEFAULT STYLE. VERSION 0.

from PyQt5 import sip

from PyQt5 import QtCore
from PyQt5. QtCore import QObject
from PyQt5. QtCore import pyqtSignal
from PyQt5 import QtGui, QtWidgets
from PyQt5. QtWidgets import QMessageBox
from functools import partial

la = [0,0,0,0,0,0,0,0,0,0]
#大,<=2
lb = [0,0,0,0,0,0,0,0,0,0]
#小,<=4

lc = [0,0,0,0,0,0,0,0,0,0]
#明
ld = [0,0,0,0,0,0,0,0,0,0]
#暗



def changelist(where, what, howmany):
    if what:
        la[where]= howmany
    else:
        lb[where]= howmany

def countlist():
    def cd(a, b):
        x = a+ b//2
        y = b%2
        if x > 2:
            x=2
            y=x-2
        return x,y

    for i in range (9):
        xy=cd(la[i], lb[i])
        lc[i]=xy[0]
        ld[i]=xy[1]

    sumld = sum(ld)
    unit = 0

    if sumld >1:
        if sumld < 5:
            unit = 1
        else:
            unit = 2

    unit+= sum(lc)
    result = 10-0.5*unit

    if result == 0.5:
        result = 1
    else:
        result = int(result)
    return result


class Ui_Dialog(QObject):

    countsignal =  pyqtSignal(int)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 500)
        Dialog.setWindowFlags(QtCore.Qt.WindowMinMaxButtonsHint | QtCore.Qt.WindowCloseButtonHint)
        
        # 字体设置不报错但无效
        self.font = QtGui.QFont()
        self.font.setFamily('Consolas')
        
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.showhelp)


        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.verticalLayout.addWidget(self.tabWidget)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        # self.lcdNumber.value(10)此处报错。但又觉得满分没必要计算，就不设置初始显示10了，当然如果实在想看10分可以再拨到0
        self.gridLayout.addWidget(self.lcdNumber, 1, 1, 1, 1)


        self.running()           
        
        self.retranslateUi(Dialog)



    def running(self):
        
        for tab_ in range(10):
            
            tab = QtWidgets.QWidget()
           

            gridLayout_2 = QtWidgets.QGridLayout(tab)
            gridLayout_2.setObjectName("gridLayout_2")
            horizontalLayout = QtWidgets.QHBoxLayout()
            horizontalLayout.setObjectName("horizontalLayout")


            spinBox = QtWidgets.QSpinBox(tab)
            spinBox.setWrapping(False)
            spinBox.setFrame(True)
            spinBox.setAlignment(QtCore.Qt.AlignCenter)
            spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
            spinBox.setMaximum(2)
            spinBox.setObjectName("spinBox")

            spinBox.valueChanged['int'].connect( partial(changelist, tab_, 1))
            # spinBox.valueChanged['int'].connect(self. print)
            spinBox.valueChanged['int'].connect(self. listcounted)
            self.countsignal.connect(self.lcdNumber.display)
            
            

            horizontalLayout.addWidget(spinBox)
            gridLayout_2.addLayout(horizontalLayout, 0, 0, 1, 1)



            dial = QtWidgets.QDial(tab)
            dial.setMaximum(5)
            dial.setPageStep(1)
            dial.setWrapping(True)
            dial.setNotchesVisible(True)
            dial.setObjectName("dial")

            gridLayout_2.addWidget(dial, 0, 1, 1, 1)

            dial.valueChanged['int'].connect(partial(changelist, tab_, 0))
            # dial.valueChanged['int'].connect(self.print)
            dial.valueChanged['int'].connect(self. listcounted)
            self.countsignal.connect(self.lcdNumber.display)



            self.tabWidget.addTab(tab, str(tab_+1))


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "TEM4 DICTATION SCORER"))
        self.pushButton.setText(_translate("Dialog", "❔"))
        self.groupBox.setTitle(_translate("Dialog", "*left: major                   |                  right: minor*"))

    

    # def print(self):
    #     print(countlist())
    #     print(la, lb, lc, ld)


    def showhelp(self):
        
        standard = '''
▲ 重复错误只计一次

A.小错误：

■ 单词拼写错一到两个字母. 

■ 两个字母以下的词、次序颠倒.

■ 标点符号错误(含大小写). 如果标点影响后句大小写，算前句的一个小错. 例:

World War I → world war one; , and then adopted → . And then adopted

■ 冠词、单复数错误. 例:

until the beginning → until beginning; parent → parents


B.大错误：

漏写、加词、造词、换词（冠词作小错计）、大移位、时态错误、一个词变两个词. 例：

loved → love; task — test; trip — trap; flee — flea; have finished — finsh(ed)


C.下列情况不扣分:

数字表记：World War I → World War One; 90 percent → 90%

允许的写法：race car → racecar; well-balanced → well balanced

允许的标点符号等：in the past → in the past,

'''
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("NOTES")
        # msg.resize(1000,1000)调不了

        msg.setText(standard)

        msg.exec()

    def listcounted(self):       
        self.countsignal. emit(countlist())
        

   


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
   
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
