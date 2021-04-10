import turtle
import random
import time
# Методи вікна:
#     вікно.bgcolor(фон_вікна)                      # змінити фон вікна
#     вікно.listen()                                # почати реагувати на клавіші
#     вікно.onkey(функція_із_дією, назва_клавіші)   # зробити дію якщо натиснуто клавішу
#     вікно.onscreenclick(функція_із_дією,          # кномер_кнопки_миші - число від 1 до 3
#                         кномер_кнопки_миші)       # 1 - ліва кнопка
#                                                   # 2 - середня кнопка
#                                                   # 3 - права кнопка
#                                                   # функція_із_дією повинна приймати 2 параметри (x, y)
#
# Методи черепашки:
#     тортила.shape(форма_черепашки)                # встановити форму черепашки
#     тортила.color(колір_черепашки)                # встановити колір черепашки
#     тортила.penup()                               # перестати слідити
#     тортила.pendown()                             # почати слідити
#     тортила.isdown()                              # Перевірити чи залишає слід черепашка
#     тортила.setheading(кут_відносно_вертикалі)    # кут_відносно_вертикалі - вимірюється градусами
#                                                   # 90 - дивитись вгору, 0 - праворуч, 270 - вниз, 180 - ліворуч
#     тортила.right(кут_поворота)                   # повернутись праворуч (кут поворота у градусах)
#     тортила.left(кут_поворота)                    # повернутись ліворуч (кут поворота у градусах)
#     тортила.goto(х, у)                            # стрибнути на точку з координатами, [0, 0] - початкова точка
#     тортила.backward(відстань)                    # йти задом наперед  (відстань вимірюється у точках)
#     тортила.forward(відстань)                     # йти вперед (відстань вимірюється у точках)
#     тортила.stamp()                               # лишити слід
#     рахунок.clear()
#     рахунок.write("Текст")
#     тортила.ycor()
#     тортила.xcor()
#
# можливі кольори:
#     'orange', 'red', 'pink', 'yellow', 'blue', 'green'
#
# можливі відтінки:
#     'light', 'dark'
#
# можливі форми черепашки:
#     'turtle', 'classic', 'arrow', 'circle'
#
# Назви клавіш клавіатури:
#    'Up'    - вгору
#    'Down'  - вниз
#    'Left'  - ліворуч
#    'Right' - праворуч
#    'Enter' - пробіл
#    'Space' - пробіл
#    також можна використовувати те,
#    що написано на самих клавішах
#    взявши його в лапки
#
#  Функція щоб отримати випадковий колір:
#
#  def випадковий_колір():
#      colors = ["red", "blue", "green", "yellow", "black"]
#      return random.choice(colors)
#   random.randint(0, 10)       # віпадкове число від 0 до 10
# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Передмова.
# Змінні та функції, що будуть використовуватись в коді
#
фон_вікна = "lightgreen"
режим_координат = "logo"
форма_черепашки = "turtle"
колір_черепашки = "blue"
група_черепах = []
кількість_черепах = 5
продовжуємо = True
# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Вступ/зав'язок.
# Ініціалізація: створення вікна та черепашки
# (разом вказуємо їх колір та форму)
#
вікно = turtle.Screen()              # Створити вікно
вікно.bgcolor(фон_вікна)             # встановити фон
вікно.mode(режим_координат)
тортила = turtle.Turtle()            # створити черепашку
тортила.shape(форма_черепашки)       # встановити форму черепашки
тортила.color(колір_черепашки)       # встановити колір черепашки
рахунок = turtle.Turtle()
рахунок.ht()
рахунок.penup()
рахунок.goto(-420, 410)
for номер in range(кількість_черепах):
    черепашка = turtle.Turtle()
    черепашка.shape(форма_черепашки)
    черепашка.penup()
    черепашка.goto(номер*50 - ((кількість_черепах-1)*50/2), 50)
    група_черепах.append(черепашка)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#  Основна частина.
#  Вказуємо дії для потрібних клавіш
#
def рухати_черепах():
    for черепашка in група_черепах:
        черепашка.setheading(random.randint(0, 360))
        черепашка.forward(random.randint(20, 200))

def перевірка_дотику():
    for черепашка in група_черепах:
        if черепашка.distance(тортила) < 50:
            черепашка.hideturtle()
def порахувати():
    залишилось = 0
    for черепашка in група_черепах:
            if черепашка.isvisible():
                залишилось = залишилось +1
    print(f"{​​​​​​​​залишилось}​​​​​​​​")
        рахунок.clear()
        рахунок.write(f"{​​​​​​​​залишилось}​​​​​​​​", font=('Courier', 30, 'italic'))
    
def вгору():
    тортила.setheading(0)
    if (тортила.ycor()+100 < 450):
        тортила.forward(100)
        
def вправо():
    тортила.setheading(90)
    if (тортила.xcor()+100 < 450):
        тортила.forward(100)
        
def вниз():
    тортила.setheading(180)
    if (тортила.ycor()-100 > -450):
        тортила.forward(100)
def вліво():
    тортила.setheading(270)
    if (тортила.xcor()-100 > -450):
        тортила.forward(100)
        
def слід():
    if тортила.isdown():
        тортила.penup()
    else:
        тортила.pendown()
        
def квадрат():
    тортила.setheading(0)
    тортила.forward(100)
    тортила.setheading(90)
    тортила.forward(100)
    тортила.setheading(180)
    тортила.forward(100)
    тортила.setheading(270)
    тортила.forward(100)
    
def трикутник():
    тортила.setheading(0)
    тортила.forward(100)
    тортила.setheading(120)
    тортила.forward(100)
    тортила.setheading(240)
    тортила.forward(100)

вікно.onkey(вгору, 'Up')
вікно.onkey(вправо, 'Right')
вікно.onkey(вліво, 'Left')
вікно.onkey(вниз, 'Down')
вікно.onkey(слід, 'space')
вікно.onkey(квадрат, 's')
вікно.onkey(трикутник, 't')



# - - - - - - - - - - - -  - - - - - - - - - - - - - - - -
# Кінцівка програми.
#
вікно.listen()    # Почати реагувати на клавіші та кліки мишею

#вікно.mainloop()  # утримувати вікно відкритим
#Головний цикл програми
while продовжуємо:
    порахувати()
    перевірка_дотику()
    рухати_черепах()
    вікно.update()
