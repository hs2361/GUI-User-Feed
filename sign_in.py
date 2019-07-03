# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'feed_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import privy,os,sys,base64

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(476, 288)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 200, 141, 20))
        self.label_3.setObjectName("label_3")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(70, 60, 351, 61))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.Email = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Email.setObjectName("Email")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Email)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.Password = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Password.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Password)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 10, 81, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.SignIn = QtWidgets.QPushButton(self.centralwidget)
        self.SignIn.setGeometry(QtCore.QRect(180, 130, 101, 41))
        self.SignIn.setObjectName("SignIn")
        self.SignUp = QtWidgets.QPushButton(self.centralwidget)
        self.SignUp.setGeometry(QtCore.QRect(270, 190, 101, 41))
        self.SignUp.setObjectName("SignUp")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 476, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.DialogBox = QtWidgets.QMessageBox(self.centralwidget)
        self.DialogBox.setIcon(QtWidgets.QMessageBox.Warning)
        self.DialogBox.setText("You don't have an exisiting account. Please Sign Up for an account")
        self.DialogBox.setWindowTitle("Account does not exist!")
        self.DialogBox.setStandardButtons(QtWidgets.QMessageBox.Cancel)
        self.DialogBox.setObjectName("DialogBox")
        self.DialogBox2 = QtWidgets.QMessageBox(self.centralwidget)
        self.DialogBox2.setIcon(QtWidgets.QMessageBox.Warning)
        self.DialogBox2.setText("Incorrect Password")
        self.DialogBox2.setWindowTitle("Error!")
        self.DialogBox2.setStandardButtons(QtWidgets.QMessageBox.Cancel)
        self.DialogBox2.setObjectName("DialogBox2")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.SignIn.clicked.connect(self.signin)
        self.SignUp.clicked.connect(self.signupform)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Your Feed"))
        self.label_3.setText(_translate("MainWindow", "Don\'t have an account?"))
        self.label.setText(_translate("MainWindow", "Email ID"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.label_4.setText(_translate("MainWindow", "Sign In"))
        self.SignIn.setText(_translate("MainWindow", "Sign In"))
        self.SignUp.setText(_translate("MainWindow", "Sign Up"))
    
    def signupform(self):
        os.system("python sign_up_form.py")
        
    def signin(self):
        email = self.Email.text()
        password = self.Password.text()
        if not os.path.isfile(f"{email.split('@')[0]}.txt"):
            self.DialogBox.exec_()
        else:
            with open(f"{email.split('@')[0]}.txt","r") as f:
                lines = f.readlines()
                try:
                    stored_password =  privy.peek(lines[2],password)
                    del(stored_password)
                    with open("signedin.txt","w") as f:
                        f.write(email + "\n" + base64.b64encode(password.encode("utf-8")).decode("utf-8"))
                    os.system("python feed_gui.py")
                    sys.exit()
                except ValueError:
                    self.DialogBox2.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

