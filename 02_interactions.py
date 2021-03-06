import turtle
import random

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
#     тортила.setheading(кут_відносно_вертикалі)    # кут_відносно_вертикалі - вимірюється градусами
#                                                   # 90 - дивитись вгору, 0 - праворуч, 270 - вниз, 180 - ліворуч
#     тортила.right(кут_поворота)                   # повернутись праворуч (кут поворота у градусах)
#     тортила.left(кут_поворота)                    # повернутись ліворуч (кут поворота у градусах)
#     тортила.goto(х, у)                            # стрибнути на точку з координатами, [0, 0] - початкова точка
#     тортила.backward(відстань)                    # йти задом наперед  (відстань вимірюється у точках)
#     тортила.forward(відстань)                     # йти вперед (відстань вимірюється у точках)
#     тортила.stamp()                               # лишити слід
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

# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Передмова.
# Змінні та функції, що будуть використовуватись в коді
#

фон_вікна = "lightgreen"
режим_координат = "logo"

форма_черепашки = "turtle"
колір_черепашки = "blue"

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


# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#  Основна частина.
#  Вказуємо дії для потрібних клавіш
#


# - - - - - - - - - - - -  - - - - - - - - - - - - - - - -
# Кінцівка програми.
#
вікно.listen()    # Почати реагувати на клавіші та кліки мишею
вікно.mainloop()  # утримувати вікно відкритим
