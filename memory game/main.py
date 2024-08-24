from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from menu_window import*
from main_window import*      #підключення модулів

from random import choice, shuffle # Вибір рандомного елемента зі списку \ перемішує  елементи списку 
from time import sleep 

app = QApplication([])

#main_winn = QWidget()
#main_winn.resize(400, 300)
#main_winn.move(300, 300)
#main_winn.setWindowTitle("Menu")

class Question(): 
    def __init__(self,question, answer, wrong_answer1, wrong_answer2, wrong_answer3 ):
        self.question = question                #питання
        self.answer = answer                    #відповідь
        self.wrong_answer1 = wrong_answer1      # непр відп 1 ...
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3

        self.actual = True # чи актуальне питання 
        self.attempts =  0 # кіл спроб
        self.correct = 0 # кіл прав відп

    def got_right(self):
        '''Зміеюємо статистику, отримавши відповідь'''
        self.attempts += 1 
        self.correct  += 1
    
    def got_wrong(self):
        '''Змінює статистику,отримавши неправильну відповідь'''
        self.attempts += 1 

#(Сеул, Париж, Київ , Париж, Рим, Сідней , Лондон , Пекін, Веллінгтон, Амстердам, Ріо-де-Жанейро, Каїр, Пекін, Вашингтон, Мадрид )
q1 = Question("Яка столиця відома своїм фестивалем ліхтарів і є столицею Південної Кореї?" , "Сеул", "Рим", "Піза","Париж ") #
q2 = Question("Яка столиця має знамениту вежу, відому як Ейфелева вежа?","Париж" ,"Афіни","Берлін", "Токіо" ) #
q3 = Question("В якій столиці найглибший метрополітен в світі ?","Київ" ,"Пекін","Вашингтон", "Рим") # 
q4 = Question("В якій столиці знаходиться найвідоміша картина Леонардо да Вінчі 'Мона Ліза'" ,"Париж" ,"Мехіко","Відень","Ріо-де-Жанейро") # 
q5 = Question("Яка столиця відома своєю історією та Колізеєм?","Рим" ,"Лондон","Сеул", "Бангкок") #  
q6 = Question("Яка столиця знаменита своєю оперою у формі черепашки?","Сідней" ,"Доха","Флоренція", "Абу-Дабі") #
q7 = Question("Яка столиця відома своєю знаменитою годинниковою вежею Біг-Бен?","Лондон" ,"Нью-Йорк","Париж", "Ліма") # 
q8 = Question("Яка столиця є дочимом для знаменитої площі Тяньаньмень?","Пекін" ,"Кейптаун","Катманду", "Канберра") #
q9 = Question("Яка столиця розташована найближче до Південного полюса?","Веллінгтон" ,"Сан-Марино","Дубай", "Ріо-де-Жанейро") #
q10 = Question("Яка столиця світу відома своїми каналами та будинками на воді?","Амстердам" ,"КаЇр","Лісабон", "Венеція") #
q11 = Question("Яка столиця відома своїм величезним стадіоном 'Маракана'?","Ріо-де-Жанейро" ,"Флоренція","Неаполь", "Афіни") #
q12 = Question("В якій столиці можна знайти найдовшу міську річку у світі?", "Каїр","Лондон" ,"Париж","Київ") #
q13 = Question("В якій столиці проживає найбільше людей?", "Пекін","Вашингтон" ,"Рим","Піза") #
q14 = Question("В якій столиці знаходиться білий дім?", "Вашингтон","Бразиліа" ,"Мехіко","Нью-Йорк") #
q15 = Question("В честь якої столиці названо футбольну команду?", "Мадрид","Кишинів" ,"Монако","Кіто") #

#Списокз перемикачів кнопок та питань
radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

questions = [q1, q2 , q3 , q4 , q5 , q6 , q7 , q8 , q9 , q10 , q11 , q12 , q13 , q14 , q15]

# функція що обирає випадкове запитання зі списку 
def new_question():
    global cur_question
    cur_question = choice(questions)                         #вибирає рандомне запитання 

    Ib_Question.setText(cur_question.question)               #встановлює теекст(відповіді та запитання) на віджети
    lb_Correct.setText(cur_question.answer) 

    shuffle(radio_list)                                      #перемішує кнопки
    
    radio_list[0].setText(cur_question.wrong_answer1)        #розміщуємо на них знову питання
    radio_list[1].setText(cur_question.wrong_answer2)
    radio_list[2].setText(cur_question.wrong_answer3)        #в новому порядку
    radio_list[3].setText(cur_question.answer)


# функця для перевірки результату відповіді 

def check_results():
    for ans_btn in radio_list:
        if ans_btn.isChecked():
            




# функція для кнопки 'відпочити' 
def rest():
    main_win.hide()
    n = box_Minutes.value() * 60
    sleep(n)
    main_win.show()


# функція для кнопки панелі - дод питання та статистика 

def show_menu():                # відкриває меню 
    menu_win.show()
    main_win.hide()

def back_menu():            # відкриває гол вікно
    menu_win.hide()
    main_win.show()

def clear():                        #очищає
    txt_Question.clear()
    txt_Answer.clear()
    txt_Wrong1.clear()
    txt_Wrong2.clear()
    txt_Wrong3.clear()


#підключення виклику функції до кнопок


new_question()

btn_Menu.clicked.connect(show_menu)
btn_back.clicked.connect(back_menu)
btn_clear.clicked.connect(clear)
btn_Sleep.clicked.connect(rest)
btn_OK.clicked.connect(switch_screen)
btn_add_q.clicked.connect(add_question)












main_win.show()
app.exec()
