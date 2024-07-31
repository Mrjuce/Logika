from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import randint

app = QApplication([]) #програма
#основне вікно
main_win = QWidget() 
main_win.resize(400, 400)
main_win.setWindowTitle("Лотерея")

#віджети головного вікна
button = QPushButton("Випробувати удачу") #кнопка 
text = QLabel("Натисни, щоб взяти участь")
num1 = QLabel("?")
num2  = QLabel("?")
#розташування віджетів 
line = QVBoxLayout() #вертикальна лінія (макет)
line.addWidget(text, alignment = Qt.AlignCenter) 
line.addWidget(num1, alignment = Qt.AlignCenter)
line.addWidget(num2, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)

#передамо макет на головне вікно
main_win.setLayout(line)

#функція яка генерує числа і показує їх
def generate():
    n1 = randint(0,9)
    n2 = randint(0,9)
    num1.setText(str(n1))
    num2.setText(str(n2))
    if n1==n2:
        text.setText("Ви виграли! Зіграйте знову")
    else:
        text.setText("Ви програли! Зіграйте знову")

button.clicked.connect(generate)









main_win.show()
app.exec_()