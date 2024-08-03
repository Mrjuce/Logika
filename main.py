from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

def win():
    victory_win = QMessageBox()
    victory_win.setText("Правильно!😊")
    victory_win.exec_()



def lose():
    victory_lose = QMessageBox()
    victory_lose.setText("Неправильно!😥")
    victory_lose.exec_()


app = QApplication([]) #програма
#основне вікно
main_win = QWidget() 
main_win.resize(400, 200)
main_win.setWindowTitle("Конкурс😋")

#віджети головного вікна
quest = QLabel("В якому році канал отримав  золоту кнопку від YouTube? 🕐") #кнопка 
btn1 = QPushButton("2005🤩")
btn2 = QPushButton("2010😲")
btn3  = QPushButton("2015🤐")
btn4 =  QPushButton("2020😷")


#3 горизонтальны лінії 
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()

layoutV1 = QVBoxLayout()

#горизонтальні лінії 
layoutH1.addWidget(quest, alignment= Qt.AlignCenter)
layoutH2.addWidget(btn1,  alignment= Qt.AlignCenter)
layoutH2.addWidget(btn2, alignment= Qt.AlignCenter)
layoutH3.addWidget(btn3 ,  alignment= Qt.AlignCenter)
layoutH3.addWidget(btn4 , alignment= Qt.AlignCenter)

# вертикальна  лінія 
layoutV1.addLayout(layoutH1)
layoutV1.addLayout(layoutH2)
layoutV1.addLayout(layoutH3)

main_win.setLayout(layoutV1)

btn1.clicked.connect(lose)
btn2.clicked.connect(lose)
btn3.clicked.connect(win)
btn4.clicked.connect(lose)
    

main_win.show()
app.exec_()