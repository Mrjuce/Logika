# Підключення модулів
from menu_window import *
from main_window import *

from random import choice, shuffle #виб. ранд. ел.зі списку \ перемішує елементи списку
from time import sleep

# CSS - стилі
# CSS - стилі 
wins = [main_win, menu_win] 
for win in wins: 
    win.setStyleSheet(''' 
                      color: #00151c; 
                      background-color: #E19CD8; 
                      border: 4px double #b21f1f; 
                      font-size: 19px; 
                      font-family: Bold  ; 
                      border: 1.5px solid #834F7C ;
                      border-radius: 10px; 
                      text-align: center; 
                     
                       
                     
                       
                          
                         ''') 
lb_Result.setStyleSheet('margin: 20px;')

# клас Питання 
class Question():

    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question             # питання
        self.answer = answer                 # відповідь
        self.wrong_answer1 = wrong_answer1   # непр.відп.1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3

        self.actual = True  # чи актуальне питання
        self.attempts = 0   # кільк. спроб
        self.correct = 0    # кільк. прав.відп.

    def got_right(self):
        ''' змінює статистику, отримавши правильну відповідь'''
        self.attempts += 1
        self.correct += 1

    def got_wrong(self):
        ''' змінює статистику, отримавши неправильну відповідь'''
        self.attempts += 1

# питання
#(Сеул, Париж, Київ , Париж, Рим, Сідней , Лондон , Пекін, Веллінгтон, Амстердам, Ріо-де-Жанейро, Каїр, Пекін, Вашингтон, Мадрид )
q1 = Question("Яка столиця відома своїм фестивалем ліхтарів і є столицею Південної Кореї?" , "Сеул", "Рим", "Піза","Париж ") #
q2 = Question("Яка столиця має знамениту вежу, відому як Ейфелева вежа?","Париж" ,"Афіни","Берлін", "Токіо" ) #
q3 = Question("В якій столиці найглибший метрополітен в світі ?","Київ" ,"Пекін","Вашингтон", "Рим") # 
q4 = Question("В якій столиці знаходиться найвідоміша картина Леонардо да Вінчі 'Мона Ліза?'" ,"Париж" ,"Мехіко","Відень","Ріо-де-Жанейро") # 
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

# --------------------------------------
#    Функції для кнопок головного вікна
# --------------------------------------

#       (функція що обирає випадкове запитання зі списку та показує його на екрані)
def new_question():
    global cur_question
    cur_question = choice(questions)                   #вибирає рандомне запитання

    lb_Question.setText(cur_question.question)         #встановлює текст(відповіді та запитання) на віджети
    lb_Correct.setText(cur_question.answer)

    shuffle(radio_list)                                 #перемішує кнопки(щоб не на 1 шій була завжди прав.відпов.)- змінюючи позицію в списку
    
    radio_list[0].setText(cur_question.wrong_answer1)   #розмішюємо на них знову питання
    radio_list[1].setText(cur_question.wrong_answer2)
    radio_list[2].setText(cur_question.wrong_answer3)   #в новому порядку
    radio_list[3].setText(cur_question.answer)


#       (функція для перевірки результату відповіді)
def check_result():
    for ans_btn in radio_list:
        if ans_btn.isChecked():                         # вибраний вірних перемикач?
            if ans_btn.text() == lb_Correct.text():     # чи збігається текст на вибр.кпонці та текст прав.відповіді?
                cur_question.got_right()                # збільшити кільк.спроб +1
                lb_Result.setText('Правильно!')
                update_statistics()        
                break
    else:
        cur_question.got_wrong()                 #якщо не вибр.прав.відп.
        lb_Result.setText('Неправильно! :)')     #змінити надпис на НЕПРАВИЛЬНО
        update_statistics()

#       (функцію для Відпочити)
def rest():
    main_win.hide()                 # приховати головний віджет    
    n = box_Minutes.value() * 60    # бере знач.від корситвача і множить на кільк. секунд
    sleep(n)                        # спить
    main_win.show()                 # потім знову показує


# -----------------------------------------
#      Функції для кнопок панелі меню 
# ----------------------------------------

def show_menu():      
    menu_win.show()
    main_win.hide()

def back_menu():
    menu_win.hide()
    main_win.show()

def clear():
    txt_Question.clear()
    txt_Answer.clear()
    txt_Wrong1.clear()
    txt_Wrong2.clear()
    txt_Wrong3.clear()

def add_question():
    newq = Question(txt_Question.text(), txt_Answer.text(), txt_Wrong1.text(), txt_Wrong2.text(), txt_Wrong3.text())
    questions.append(newq)
    clear()

#   функція зміни екранів
def switch_screen():
    if btn_OK.text() == 'Відповісти':
        check_result()   #
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn_OK.setText('Наступне запитання')
    else:
        new_question() #
        RadioGroupBox.show()
        AnsGroupBox.hide()
        btn_OK.setText('Відповісти')
                                            # скинути вибрану радіо-кнопку
        RadioGroup.setExclusive(False) # зняли обмеження, щоб можна було скинути вибір радіокнопки
        rbtn_1.setChecked(False)
        rbtn_2.setChecked(False)
        rbtn_3.setChecked(False)
        rbtn_4.setChecked(False)
        RadioGroup.setExclusive(True) # повернули обмеження, тепер лише одна радіокнопка може бути вибрана

#   функція оновлює показници статистики
def update_statistics():
    total_attempts = sum(q.attempts for q in questions)
    total_correct = sum(q.correct for q in questions)
    lbl_statistics.setText(f"Статистика:\nПравильних відповідей: {total_correct}\nЗагальна кількість спроб: {total_attempts}")



# ----------------------------------------------------------
#  Пікючення виклику функції - до кнопок
# ----------------------------------------------------------

# - згеневувати питання з самого початку
new_question()

btn_Menu.clicked.connect(show_menu)
btn_Sleep.clicked.connect(rest)
btn_OK.clicked.connect(switch_screen)
btn_add_q.clicked.connect(add_question)
btn_clear.clicked.connect(clear)
btn_back.clicked.connect(back_menu)




# - відображення вікон
main_win.show()
app.exec_()




