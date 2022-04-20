# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 601)
        MainWindow.setMinimumSize(QtCore.QSize(790, 601))
        MainWindow.setMaximumSize(QtCore.QSize(790, 601))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_camera = QtWidgets.QLabel(self.centralwidget)
        self.label_camera.setGeometry(QtCore.QRect(10, 10, 600, 351))
        self.label_camera.setMinimumSize(QtCore.QSize(600, 351))
        self.label_camera.setMaximumSize(QtCore.QSize(600, 351))
        self.label_camera.setFrameShape(QtWidgets.QFrame.Box)
        self.label_camera.setText("")
        self.label_camera.setScaledContents(True)
        self.label_camera.setObjectName("label_camera")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(640, 10, 120, 131))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton_live = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_live.setGeometry(QtCore.QRect(10, 20, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_live.setFont(font)
        self.pushButton_live.setObjectName("pushButton_live")
        self.pushButton_camera = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_camera.setGeometry(QtCore.QRect(10, 70, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_camera.setFont(font)
        self.pushButton_camera.setObjectName("pushButton_camera")
        self.groupBox_1 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_1.setGeometry(QtCore.QRect(10, 380, 151, 181))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_1.setFont(font)
        self.groupBox_1.setObjectName("groupBox_1")
        self.label = QtWidgets.QLabel(self.groupBox_1)
        self.label.setGeometry(QtCore.QRect(10, 40, 21, 21))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_1)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 21, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_1)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 21, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.groupBox_1)
        self.line.setGeometry(QtCore.QRect(10, 130, 131, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.groupBox_1)
        self.line_2.setGeometry(QtCore.QRect(10, 20, 131, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lbl_object1_x = QtWidgets.QLabel(self.groupBox_1)
        self.lbl_object1_x.setGeometry(QtCore.QRect(40, 40, 91, 21))
        self.lbl_object1_x.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_object1_x.setObjectName("lbl_object1_x")
        self.lbl_object1_y = QtWidgets.QLabel(self.groupBox_1)
        self.lbl_object1_y.setGeometry(QtCore.QRect(40, 70, 91, 21))
        self.lbl_object1_y.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_object1_y.setObjectName("lbl_object1_y")
        self.lbl_object1_z = QtWidgets.QLabel(self.groupBox_1)
        self.lbl_object1_z.setGeometry(QtCore.QRect(40, 100, 91, 21))
        self.lbl_object1_z.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_object1_z.setObjectName("lbl_object1_z")
        self.label_object1_null = QtWidgets.QLabel(self.groupBox_1)
        self.label_object1_null.setGeometry(QtCore.QRect(6, 150, 131, 20))
        self.label_object1_null.setText("")
        self.label_object1_null.setObjectName("label_object1_null")
        self.label_picture = QtWidgets.QLabel(self.centralwidget)
        self.label_picture.setGeometry(QtCore.QRect(640, 150, 121, 91))
        self.label_picture.setFrameShape(QtWidgets.QFrame.Box)
        self.label_picture.setText("")
        self.label_picture.setScaledContents(True)
        self.label_picture.setAlignment(QtCore.Qt.AlignCenter)
        self.label_picture.setObjectName("label_picture")
        self.pushButton_reference = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reference.setGeometry(QtCore.QRect(640, 250, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_reference.setFont(font)
        self.pushButton_reference.setObjectName("pushButton_reference")
        self.pushButton_submit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_submit.setGeometry(QtCore.QRect(640, 310, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_submit.setFont(font)
        self.pushButton_submit.setObjectName("pushButton_submit")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(160, 380, 151, 181))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 21, 21))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 21, 21))
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 100, 21, 21))
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.line_3 = QtWidgets.QFrame(self.groupBox_2)
        self.line_3.setGeometry(QtCore.QRect(10, 130, 131, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.groupBox_2)
        self.line_4.setGeometry(QtCore.QRect(10, 20, 131, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.lbl_object2_x = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_object2_x.setGeometry(QtCore.QRect(40, 40, 91, 21))
        self.lbl_object2_x.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_object2_x.setObjectName("lbl_object2_x")
        self.lbl_object2_y = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_object2_y.setGeometry(QtCore.QRect(40, 70, 91, 21))
        self.lbl_object2_y.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_object2_y.setObjectName("lbl_object2_y")
        self.lbl_object2_z = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_object2_z.setGeometry(QtCore.QRect(40, 100, 91, 21))
        self.lbl_object2_z.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_object2_z.setObjectName("lbl_object2_z")
        self.label_object2_null = QtWidgets.QLabel(self.groupBox_2)
        self.label_object2_null.setGeometry(QtCore.QRect(10, 150, 131, 20))
        self.label_object2_null.setText("")
        self.label_object2_null.setObjectName("label_object2_null")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(470, 380, 151, 181))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(10, 40, 21, 21))
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(10, 70, 21, 21))
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(10, 100, 21, 21))
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.line_5 = QtWidgets.QFrame(self.groupBox_4)
        self.line_5.setGeometry(QtCore.QRect(10, 130, 131, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.groupBox_4)
        self.line_6.setGeometry(QtCore.QRect(10, 20, 131, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.lbl_object4_x = QtWidgets.QLabel(self.groupBox_4)
        self.lbl_object4_x.setGeometry(QtCore.QRect(40, 40, 91, 21))
        self.lbl_object4_x.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_object4_x.setObjectName("lbl_object4_x")
        self.lbl_object4_y = QtWidgets.QLabel(self.groupBox_4)
        self.lbl_object4_y.setGeometry(QtCore.QRect(40, 70, 91, 21))
        self.lbl_object4_y.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_object4_y.setObjectName("lbl_object4_y")
        self.lbl_object4_z = QtWidgets.QLabel(self.groupBox_4)
        self.lbl_object4_z.setGeometry(QtCore.QRect(40, 100, 91, 21))
        self.lbl_object4_z.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_object4_z.setObjectName("lbl_object4_z")
        self.label_object4_null = QtWidgets.QLabel(self.groupBox_4)
        self.label_object4_null.setGeometry(QtCore.QRect(10, 150, 131, 20))
        self.label_object4_null.setText("")
        self.label_object4_null.setObjectName("label_object4_null")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(310, 380, 151, 181))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(10, 40, 21, 21))
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(10, 70, 21, 21))
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(10, 100, 21, 21))
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.line_7 = QtWidgets.QFrame(self.groupBox_3)
        self.line_7.setGeometry(QtCore.QRect(10, 130, 131, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.groupBox_3)
        self.line_8.setGeometry(QtCore.QRect(10, 20, 131, 16))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.lbl_object3_x = QtWidgets.QLabel(self.groupBox_3)
        self.lbl_object3_x.setGeometry(QtCore.QRect(40, 40, 91, 21))
        self.lbl_object3_x.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_object3_x.setObjectName("lbl_object3_x")
        self.lbl_object3_y = QtWidgets.QLabel(self.groupBox_3)
        self.lbl_object3_y.setGeometry(QtCore.QRect(40, 70, 91, 21))
        self.lbl_object3_y.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_object3_y.setObjectName("lbl_object3_y")
        self.lbl_object3_z = QtWidgets.QLabel(self.groupBox_3)
        self.lbl_object3_z.setGeometry(QtCore.QRect(40, 100, 91, 21))
        self.lbl_object3_z.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_object3_z.setObjectName("lbl_object3_z")
        self.label_object3_null = QtWidgets.QLabel(self.groupBox_3)
        self.label_object3_null.setGeometry(QtCore.QRect(10, 150, 131, 20))
        self.label_object3_null.setText("")
        self.label_object3_null.setObjectName("label_object3_null")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 790, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_live.setText(_translate("MainWindow", "Live"))
        self.pushButton_camera.setText(_translate("MainWindow", "Capture"))
        self.groupBox_1.setTitle(_translate("MainWindow", "Object #1"))
        self.label.setText(_translate("MainWindow", "X:"))
        self.label_2.setText(_translate("MainWindow", "Y:"))
        self.label_3.setText(_translate("MainWindow", "Z:"))
        self.lbl_object1_x.setText(_translate("MainWindow", "-"))
        self.lbl_object1_y.setText(_translate("MainWindow", "-"))
        self.lbl_object1_z.setText(_translate("MainWindow", "-"))
        self.pushButton_reference.setText(_translate("MainWindow", "Add reference"))
        self.pushButton_submit.setText(_translate("MainWindow", "Submit"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Object #2"))
        self.label_4.setText(_translate("MainWindow", "X:"))
        self.label_5.setText(_translate("MainWindow", "Y:"))
        self.label_6.setText(_translate("MainWindow", "Z:"))
        self.lbl_object2_x.setText(_translate("MainWindow", "-"))
        self.lbl_object2_y.setText(_translate("MainWindow", "-"))
        self.lbl_object2_z.setText(_translate("MainWindow", "-"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Object #4"))
        self.label_7.setText(_translate("MainWindow", "X:"))
        self.label_8.setText(_translate("MainWindow", "Y:"))
        self.label_9.setText(_translate("MainWindow", "Z:"))
        self.lbl_object4_x.setText(_translate("MainWindow", "-"))
        self.lbl_object4_y.setText(_translate("MainWindow", "-"))
        self.lbl_object4_z.setText(_translate("MainWindow", "-"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Object #3"))
        self.label_10.setText(_translate("MainWindow", "X:"))
        self.label_11.setText(_translate("MainWindow", "Y:"))
        self.label_12.setText(_translate("MainWindow", "Z:"))
        self.lbl_object3_x.setText(_translate("MainWindow", "-"))
        self.lbl_object3_y.setText(_translate("MainWindow", "-"))
        self.lbl_object3_z.setText(_translate("MainWindow", "-"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())