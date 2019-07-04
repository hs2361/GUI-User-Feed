from PyQt5 import QtCore, QtGui, QtWidgets
email = ""
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 702)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.label_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.Name = QtWidgets.QLineEdit(self.centralwidget)
        self.Name.setObjectName("Name")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Name)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.EmailID = QtWidgets.QLineEdit(self.centralwidget)
        self.EmailID.setObjectName("EmailID")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.EmailID)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.Password)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.City = QtWidgets.QLineEdit(self.centralwidget)
        self.City.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.City.setObjectName("City")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.City)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.Server = QtWidgets.QLineEdit(self.centralwidget)
        self.Server.setObjectName("Server")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.Server)
        self.Port = QtWidgets.QLineEdit(self.centralwidget)
        self.Port.setObjectName("Port")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.Port)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.formLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 1)
        self.Health = QtWidgets.QCheckBox(self.centralwidget)
        self.Health.setObjectName("Health")
        self.gridLayout_2.addWidget(self.Health, 8, 0, 1, 1)
        self.Business = QtWidgets.QCheckBox(self.centralwidget)
        self.Business.setObjectName("Business")
        self.gridLayout_2.addWidget(self.Business, 5, 0, 1, 1)
        self.Technology = QtWidgets.QCheckBox(self.centralwidget)
        self.Technology.setObjectName("Technology")
        self.gridLayout_2.addWidget(self.Technology, 11, 0, 1, 1)
        self.Science = QtWidgets.QCheckBox(self.centralwidget)
        self.Science.setObjectName("Science")
        self.gridLayout_2.addWidget(self.Science, 9, 0, 1, 1)
        self.General = QtWidgets.QCheckBox(self.centralwidget)
        self.General.setObjectName("General")
        self.gridLayout_2.addWidget(self.General, 7, 0, 1, 1)
        self.Entertainment = QtWidgets.QCheckBox(self.centralwidget)
        self.Entertainment.setObjectName("Entertainment")
        self.gridLayout_2.addWidget(self.Entertainment, 6, 0, 1, 1)
        self.Sports = QtWidgets.QCheckBox(self.centralwidget)
        self.Sports.setObjectName("Sports")
        self.gridLayout_2.addWidget(self.Sports, 10, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.SpanningRole, self.gridLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Joke = QtWidgets.QCheckBox(self.centralwidget)
        self.Joke.setObjectName("Joke")
        self.gridLayout.addWidget(self.Joke, 1, 0, 1, 1)
        self.Word = QtWidgets.QCheckBox(self.centralwidget)
        self.Word.setObjectName("Word")
        self.gridLayout.addWidget(self.Word, 3, 0, 1, 1)
        self.Quote = QtWidgets.QCheckBox(self.centralwidget)
        self.Quote.setObjectName("Quote")
        self.gridLayout.addWidget(self.Quote, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.formLayout_2.setLayout(2, QtWidgets.QFormLayout.SpanningRole, self.gridLayout)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Submit = QtWidgets.QPushButton(self.centralwidget)
        self.Submit.setObjectName("Submit")
        self.gridLayout_4.addWidget(self.Submit, 0, 0, 1, 1)
        self.Clear = QtWidgets.QPushButton(self.centralwidget)
        self.Clear.setObjectName("Clear")
        self.gridLayout_4.addWidget(self.Clear, 3, 0, 1, 1)
        self.Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Exit.setObjectName("Exit")
        self.gridLayout_4.addWidget(self.Exit, 4, 0, 1, 1)
        self.formLayout_2.setLayout(3, QtWidgets.QFormLayout.SpanningRole, self.gridLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.DialogBox = QtWidgets.QMessageBox(self.centralwidget)
        self.DialogBox.setIcon(QtWidgets.QMessageBox.Warning)
        self.DialogBox.setText("Please fill all fields marked with *, and enter a valid Email ID and SMTP Port")
        self.DialogBox.setWindowTitle("Error Submitting Form!")
        self.DialogBox.setStandardButtons(QtWidgets.QMessageBox.Cancel)
        self.DialogBox.setObjectName("DialogBox")
        self.DialogBox2 = QtWidgets.QMessageBox(self.centralwidget)
        self.DialogBox2.setIcon(QtWidgets.QMessageBox.Warning)
        self.DialogBox2.setText("Account already exists! Please Click the 'Sign In' button in the Sign In Screen")
        self.DialogBox2.setWindowTitle("Account Exists!")
        self.DialogBox2.setStandardButtons(QtWidgets.QMessageBox.Cancel)
        self.DialogBox2.setObjectName("DialogBox2")
        self.DialogBox3 = QtWidgets.QMessageBox(self.centralwidget)
        self.DialogBox3.setIcon(QtWidgets.QMessageBox.Warning)
        self.DialogBox3.setText("Weather data unavailable for this city! Please try another city")
        self.DialogBox3.setWindowTitle("Invalid City!")
        self.DialogBox3.setStandardButtons(QtWidgets.QMessageBox.Cancel)
        self.DialogBox3.setObjectName("DialogBox2")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Submit.clicked.connect(self.get_user_preferences)
        self.Clear.clicked.connect(self.clear_form)
        self.Exit.clicked.connect(QtCore.QCoreApplication.instance().quit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sign Up"))
        self.label_2.setText(_translate("MainWindow", "Personal Information"))
        self.label.setText(_translate("MainWindow", "Name*"))
        self.label_3.setText(_translate("MainWindow", "Email ID*"))
        self.label_4.setText(_translate("MainWindow", "Password*"))
        self.label_5.setText(_translate("MainWindow", "City*"))
        self.label_7.setText(_translate("MainWindow", "Categories of news I am interested in receiving (Check atleast one)*:"))
        self.label_9.setText(_translate("MainWindow", "SMTP Server*"))
        self.label_10.setText(_translate("MainWindow", "SMTP Port*"))
        self.Health.setText(_translate("MainWindow", "Health"))
        self.Business.setText(_translate("MainWindow", "Business"))
        self.Technology.setText(_translate("MainWindow", "Technology"))
        self.Science.setText(_translate("MainWindow", "Science"))
        self.General.setText(_translate("MainWindow", "General"))
        self.Entertainment.setText(_translate("MainWindow", "Entertainment"))
        self.Sports.setText(_translate("MainWindow", "Sports"))
        self.label_6.setText(_translate("MainWindow", "News Feed Preferences"))
        self.Joke.setText(_translate("MainWindow", "Joke of the Day"))
        self.Word.setText(_translate("MainWindow", "Word of the Day"))
        self.Quote.setText(_translate("MainWindow", "Quote of the Day"))
        self.label_8.setText(_translate("MainWindow", "I wish to receive:"))
        self.Submit.setText(_translate("MainWindow", "Submit"))
        self.Clear.setText(_translate("MainWindow", "Clear Form"))
        self.Exit.setText(_translate("MainWindow", "Exit"))

    def get_user_preferences(self):
        def validate_form():
            def validate_email(e):
                import string
                letters = string.ascii_lowercase
                try:
                    user = e.split('@')[0]
                    dom = e.split('@')[1].split('.')[0]
                    ext = e.split('@')[1].split('.')[1]
                    if (user[0] not in letters) or (not all(map(lambda e: e in letters,list(dom)))) or (not all(map(lambda e: e in letters,list(ext)))):
                        raise ValueError
                    if not all(map(lambda e: e in letters+'_-,.0123456789',user[1::])):
                        raise ValueError
                    return True
                except:
                    return False

            def validate_port(p):
                return all(map(lambda i: i in '0123456789',list(p)))

            c1 = (self.Name.text() != "")
            c2 = (self.EmailID.text() != "")
            c3 = (self.Password.text() != "")
            c4 = (self.City.text() != "")
            c5 = any([self.Business.isChecked(),self.Entertainment.isChecked(),self.General.isChecked(),self.Health.isChecked(),self.Science.isChecked(),self.Sports.isChecked(),self.Technology.isChecked()])
            c6 = validate_email(self.EmailID.text())
            c7 = (self.Server.text() != "")
            c8 = validate_port(self.Port.text())
            return all([c1,c2,c3,c4,c5,c6,c7,c8])
        
        def check_existing(email):
            import os
            return os.path.isfile(f"{email.split('@')[0]}.txt")

        def validate_city(city):
            import requests
            request = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city.lower().capitalize()}&APPID=213fc9be40420ed21ae1365c8dd63666&units=metric")
            if request.status_code == 200:
                return True
            return False

        def personal_information():
            import privy
            global email
            name = self.Name.text()
            email = self.EmailID.text()
            password = self.Password.text()
            city = self.City.text()
            
            with open(f"{email.split('@')[0]}.txt","w") as f:
                f.write("\n".join([name,email,privy.hide(password.encode("utf-8"),password,security=5,salt=None,server=True),city]))

        def news_preferences():
            cat_list = []

            if self.Business.isChecked():
                cat_list.append("business")
            if self.Entertainment.isChecked():
                cat_list.append("entertainment")
            if self.General.isChecked():
                cat_list.append("general")
            if self.Health.isChecked():
                cat_list.append("health")
            if self.Science.isChecked():
                cat_list.append("science")
            if self.Sports.isChecked():
                cat_list.append("sports")
            if self.Technology.isChecked():
                cat_list.append("technology")
            
            with open(f"{email.split('@')[0]}.txt","a") as f:
                f.writelines("\n" + str(cat_list) + "\n")

        def other_preferences():
            SMTP_SERVER = self.Server.text()
            SMTP_PORT = self.Port.text()
            with open(f"{email.split('@')[0]}.txt","a") as f:
                f.write("\n".join([str(self.Joke.isChecked()),str(self.Quote.isChecked()),str(self.Word.isChecked()),SMTP_SERVER,SMTP_PORT]))

        if (not check_existing(self.EmailID.text())) and validate_city(self.City.text()) and validate_form():                
            personal_information()
            news_preferences()
            other_preferences()
            self.Clear.click()

        elif check_existing(self.EmailID.text()):
            self.DialogBox2.exec_()

        elif not validate_city(self.City.text()):
            self.DialogBox3.exec_()

        else:
            self.DialogBox.exec_()         

    def clear_form(self):
        self.Name.setText("")
        self.EmailID.setText("")
        self.Password.setText("")
        self.City.setText("")
        self.Server.setText("")
        self.Port.setText("")

        self.Business.setChecked(False)
        self.Entertainment.setChecked(False)
        self.Health.setChecked(False)
        self.Science.setChecked(False)
        self.Sports.setChecked(False)
        self.General.setChecked(False)
        self.Technology.setChecked(False)
        self.Joke.setChecked(False)
        self.Quote.setChecked(False)
        self.Word.setChecked(False)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())