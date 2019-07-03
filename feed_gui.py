# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'feed_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import json,requests,urllib,re,random,imaplib,email,privy,ast,getpass,base64
from bs4 import BeautifulSoup as bs
from feed_config import weather_api,news_api

emailid = ""
password = ""
city = ""
news_cat_list = ""
joke = ""
quote = ""
word = ""
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(791, 846)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.WelcomeLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomeLabel.setFont(font)
        self.WelcomeLabel.setObjectName("WelcomeLabel")
        self.gridLayout_2.addWidget(self.WelcomeLabel, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Quote = QtWidgets.QTextEdit(self.centralwidget)
        self.Quote.setReadOnly(True)
        self.Quote.setObjectName("Quote")
        self.gridLayout.addWidget(self.Quote, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.Joke = QtWidgets.QTextEdit(self.centralwidget)
        self.Joke.setReadOnly(True)
        self.Joke.setObjectName("Joke")
        self.gridLayout.addWidget(self.Joke, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.QuoteLbl = QtWidgets.QLabel(self.centralwidget)
        self.QuoteLbl.setObjectName("QuoteLbl")
        self.gridLayout.addWidget(self.QuoteLbl, 4, 0, 1, 1)
        self.JokeLbl = QtWidgets.QLabel(self.centralwidget)
        self.JokeLbl.setObjectName("JokeLbl")
        self.gridLayout.addWidget(self.JokeLbl, 3, 0, 1, 1)
        self.WordLbl = QtWidgets.QLabel(self.centralwidget)
        self.WordLbl.setObjectName("WordLbl")
        self.gridLayout.addWidget(self.WordLbl, 5, 0, 1, 1)
        self.Email = QtWidgets.QTextEdit(self.centralwidget)
        self.Email.setReadOnly(True)
        self.Email.setObjectName("Email")
        self.gridLayout.addWidget(self.Email, 0, 1, 1, 1)
        self.News = QtWidgets.QTextEdit(self.centralwidget)
        self.News.setReadOnly(True)
        self.News.setObjectName("News")
        self.gridLayout.addWidget(self.News, 1, 1, 1, 1)
        self.Weather = QtWidgets.QTextEdit(self.centralwidget)
        self.Weather.setReadOnly(True)
        self.Weather.setObjectName("Weather")
        self.gridLayout.addWidget(self.Weather, 2, 1, 1, 1)
        self.Word = QtWidgets.QTextEdit(self.centralwidget)
        self.Word.setReadOnly(True)
        self.Word.setObjectName("Word")
        self.gridLayout.addWidget(self.Word, 5, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 791, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.disp_basics()
        self.disp_optionals()
        self.disp_quote()
        self.disp_word()
        self.disp_joke()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Welcome!"))
        self.WelcomeLabel.setText(_translate("MainWindow", "Welcome name!!"))
        self.label_3.setText(_translate("MainWindow", "Weather in your city:"))
        self.label_2.setText(_translate("MainWindow", "News articles for you:"))
        self.label.setText(_translate("MainWindow", "Here are the subjects of your latest 5 emails:"))
        self.QuoteLbl.setText(_translate("MainWindow", "Quote of the Day:"))
        self.JokeLbl.setText(_translate("MainWindow", "Joke of the Day:"))
        self.WordLbl.setText(_translate("MainWindow", "Word of the Day"))

    def disp_basics(self):
        def disp_name():
            with open("signedin.txt","r") as f:
                global emailid,password,city,news_cat_list,joke,quote,word
                lines = f.readlines()
                emailid = lines[0]
                password = base64.b64decode(lines[1].encode("utf-8")).decode("utf-8")
            with open(f"{emailid.split('@')[0]}.txt","r") as f:
                lines = list(f.readlines())
                name = lines[0]
                city = lines[3]
                news_cat_list = ast.literal_eval(lines[4])
                joke = ast.literal_eval(lines[5])
                quote = ast.literal_eval(lines[6])
                word = ast.literal_eval(lines[7])
            self.WelcomeLabel.setText(f"Welcome, {name}!")

        def disp_email():
            global SMTP_SERVER,SMTP_PORT
            M = imaplib.IMAP4_SSL(SMTP_SERVER,SMTP_PORT)
            M.login(emailid,password)
            M.select('inbox')
            latest_email_subjects = ""
            typ, message_numbers = M.search(None, 'ALL')
            del(typ)
            m1 = message_numbers[0].split()
            latest = m1[-5::]
            sorted_mails = sorted(map(int,latest), reverse=True)
            latest_5_emails = [str(i) for i in sorted_mails]

            for i in latest_5_emails:
                typ, data = M.fetch(i, '(RFC822)')
                msg = email.message_from_string(data[0][1].decode("utf-8"))
                latest_email_subjects += (f"\n{msg['Subject']}")

            M.close()
            M.logout()
            self.Email.setPlainText(latest_email_subjects)
        
        def disp_weather(city):
            weather_data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city.lower().capitalize()}&APPID={weather_api}&units=metric")
            weather = weather_data.json()
            description = f"Weather description of {city.lower().capitalize().strip()}: {weather['weather'][0]['description'].capitalize().strip()}\n"
            description += f"The temperature in {city.lower().capitalize().strip()} is " + str(weather['main']['temp']) + "°C\n"
            description += f"The humidity in {city.lower().capitalize().strip()} is {weather['main']['humidity']}%\n"
            description += f"The wind is blowing at a speed of {weather['wind']['speed']} m/s"
            self.Weather.setPlainText(description)   

        def disp_news():
            url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={news_api}'
            news = []
            articles = ""

            for i in news_cat_list:
                news.append(requests.get(url + f"&category={i.strip()}").json())
            for i in news:
                c = 1
                while c < 4:
                    articles += (i['articles'][c]['title'] + "\n")
                    if not i['articles'][c]['description'] is None:
                        articles += (i['articles'][c]['description'] + '\n\n')
                    else:
                        articles += ("\n")
                    c += 1
            self.News.setPlainText(articles)  

        disp_name()
        disp_email()
        disp_news()   
        disp_weather(city)     

    def disp_joke(self):
        page = random.randint(1,34)
        j = f"http://www.laughfactory.com/jokes/clean-jokes/{page}"
        joke_soup = bs(urllib.request.urlopen(j),features="lxml")
        joke = joke_soup.select(".joke-text p")
        self.Joke.setPlainText("Joke of the Day:\n" + re.split('"joke_[0-9][0-9][0-9][0-9][0-9]">\r\n',str(random.choice(joke)))[1].replace("</p>",'').replace("<br/>",'\n').strip() + "\n")

    def disp_quote(self):
        q = "http://wisdomquotes.com/quote-of-the-day"
        quote_soup = bs(urllib.request.urlopen(q),features="lxml")
        quote = quote_soup.select('.quotescollection-quote p')
        self.Quote.setPlainText("Quote of the Day:\n" + str(quote[0]).replace('<p>','').replace('</p>','') + '\n')

    def disp_word(self):
        w = "https://www.dictionary.com/e/word-of-the-day"
        word_soup = bs(urllib.request.urlopen(w),features="lxml")
        word = word_soup.select(".wotd-item__definition h1")
        definition = word_soup.select(".wotd-item__definition__text")
        self.Word.setPlainText("Word of the Day:\n" + str(word[0]).replace("<h1>",'').replace("</h1>",'') + "\n" + str(definition[0]).replace('<div class="wotd-item__definition__text">','').replace("</div>",'') + "\n")

    def disp_optionals(self):
        if not joke:
            self.JokeLbl.hide()  
            self.Joke.hide()     
        if not word:
            self.WordLbl.hide()  
            self.Word.hide()
        if not quote:
            self.QuoteLbl.hide()  
            self.Quote.hide()
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

