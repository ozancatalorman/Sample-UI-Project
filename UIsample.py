import sys
import sqlite3
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.connect()
        self.init_ui()

    def connect(self):
        connection = sqlite3.connect("membersdatabase.db")
        self.cursor = connection.cursor()

        self.cursor.execute("Create Table If not exists members(username TEXT, password TEXT)")
        connection.commit()


    def init_ui(self):
        self.username = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.button = QtWidgets.QPushButton("Log In")
        self.text = QtWidgets.QLabel("")
        self.chc = QtWidgets.QCheckBox("Remember Log In Information")
        self.ra = QtWidgets.QLabel("Which account do you want to log in ?")
        self.sendersaccount = QtWidgets.QRadioButton("Sender Account")
        self.receiversaccount = QtWidgets.QRadioButton("Receiver Account")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.username)
        v_box.addWidget(self.password)
        v_box.addWidget(self.text)
        v_box.addWidget(self.ra)
        v_box.addWidget(self.sendersaccount)
        v_box.addWidget(self.receiversaccount)
        v_box.addStretch()
        v_box.addWidget(self.chc)
        v_box.addStretch()
        v_box.addWidget(self.button)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.button.clicked.connect(lambda : self.login(self.sendersaccount.isChecked(),self.receiversaccount.isChecked()))



        self.setLayout(h_box)

        self.setWindowTitle("Log In Page")

        self.setGeometry(370, 210, 700, 530)

        self.show()




    def login(self, a, b):
        name = self.username.text()
        psw = self.password.text()

        self.cursor.execute("Select * from members where username = ? and password = ?", (name, psw))

        data = self.cursor.fetchall()

        if len(data) == 0 :
            self.text.setText("There is no such user :(\nPlease try again...")
        else:
            if self.chc.isChecked() == True :
                if a :
                    self.text.setText("Welcome to your sender account {} :)\n Your information has been saved".format(name))
                if b :
                    self.text.setText("Welcome to your receiver account {} :)\n Your information has been saved".format(name))
            else :
                if a :
                    self.text.setText("Welcome to your sender account {} :)".format(name))
                if b :
                    self.text.setText("Welcome to your receiver account {} :)".format(name))



app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())