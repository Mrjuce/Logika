from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


app = QApplication([])

menu_win = QWidget()
menu_win.resize(400, 300)
menu_win.move(300, 300)
menu_win.setWindowTitle("Menu")

txt_Question = QLineEdit("")
txt_Answer = QLineEdit("")
txt_Wrong1 = QLineEdit("")
txt_Wrong2 = QLineEdit("")
txt_Wrong3 = QLineEdit("")

#текстові рядки:
layout_form = QFormLayout() #форма для макету ліній 
layout_form.addRow("Введіть запитання:",txt_Question )
layout_form.addRow("Введіть відповідь:",txt_Answer )
layout_form.addRow("Введіть хибну відповідь №1 :",txt_Wrong1 )
layout_form.addRow("Введіть хибну відповідь №2 :",txt_Wrong2 )
layout_form.addRow("Введіть хибну відповідь №3 :",txt_Wrong3 )

#кнопки:
btn_add_q  = QPushButton("Додати запитання")
btn_back = QPushButton("Назад")
btn_clear = QPushButton("Очистити")

#Статистика:
lbl_statics = QLabel("")

lbl_statics = QLabel("Статистика:\nПравильних відповідей: 0 \n Загальна кількість спроб: 0 ")

hbtn = QHBoxLayout()
hbtn.addWidget(btn_back)
hbtn.addWidget(btn_add_q)
hbtn.addWidget(btn_clear)


vline = QVBoxLayout()
vline.addLayout(layout_form)
vline.addLayout(hbtn)
vline.addWidget(lbl_statics)

menu_win.setLayout(vline)















menu_win.show()
app.exec_()