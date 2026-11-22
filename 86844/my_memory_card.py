# MEMORY CARD
import sys
from random import shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,
                             QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel)

class Question():
    def __init__(
        self, question, right_answer,
        wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


# список вопросов (в исходнике его не было — был только один тестовый вопрос "1","2","3","4","5")
questions_list = []
questions_list.append(Question('больше всего используемый язык мирабольше всего используемый язык мира','Английский','русский','Испанский','Французский'))
questions_list.append(Question('численность населения россии','146 119 928 человек','820000 человек','2000000 человек','89452 человек'))
questions_list.append(Question('смертность в год в россии','1,8 миллиона человек','256 миллиона человек','0.56 миллиона человек','896 миллиона человек'))


app = QApplication([]) # создаём приложение (всегда первым)


btn_OK = QPushButton('Ответить') # кнопка
lb_Question = QLabel('Самый сложный вопрос в мире!') # текст вопроса

# Три строки окна
layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)  # stretch=2: кнопка шире
layout_line3.addStretch(1)


# ФОРМА ОТВЕТА
RadioGroupBox = QGroupBox("Варианты ответов")

rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

layout_line2.addWidget(RadioGroupBox)


AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)

AnsGroupBox.setLayout(layout_res)

layout_line2.addWidget(AnsGroupBox)

AnsGroupBox.hide()

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')

    RadioGroup.setExclusive(False) # сняли ограничения, чтобы сбросить выбор радиокнопок
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # вернули ограничения: выбрана может быть только одна кнопка

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers) # перемешали кнопки: правильный ответ каждый раз окажется на новом месте
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)

    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')


# ЗАДАЁМ СЛЕДУЮЩИЙ ВОПРОС (этой функции в исходнике не было)
def next_question():
    ''' задаёт следующий вопрос из списка '''
    window.cur_question = window.cur_question + 1 # переходим к следующему вопросу
    if window.cur_question >= len(questions_list):
        window.cur_question = 0 # если вопросы закончились — начинаем сначала
    q = questions_list[window.cur_question]
    ask(q) # спросили

def click_OK():
    ''' решает, что делать по нажатию кнопки: проверить ответ или показать следующий вопрос '''
    if btn_OK.text() == 'Ответить':
        check_answer() # проверка ответа
    else:
        next_question() # следующий вопрос


#ОБЩАЯ ЧАСТЬ: собираем окно (не менять)
layout_card = QVBoxLayout()  # главная полка: строки друг под другом

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)                       
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

window = QWidget()               # создаём окно
window.setLayout(layout_card)    # кладём главную полку в окно
window.setWindowTitle('Memory Card')  # заголовок окна

# номер текущего вопроса храним как свойство окна, чтобы менять его из функций
# (в исходнике этой строки не было, из-за неё next_question() не мог работать)
window.cur_question = -1

btn_OK.clicked.connect(click_OK) # в исходнике кнопка была привязана только к check_answer,
                                 # поэтому после ответа тест всегда «зависал» на одном вопросе

# всё настроено — задаём первый вопрос и показываем окно
next_question()
window.resize(400, 300)
window.show()                    # показываем окно

app.exec_()  # запуск. Без этой строки окно сразу закроется
