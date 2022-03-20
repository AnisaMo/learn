#text = "Привет"
#print(text)

#name = input("как вас зовут?")
#print(name)

#n=int(input("x1="))
#n2=int(input("x2="))
#c=n+n2
#print(c)

#Переменные
# Переменная - именованная область памяти
# Переменные могут быть значащими и ссылочными


# Считывание текстового значения
#name = input("Как вас зовут?")
#print("Ваше имя -", name)

#Считывание числового значения
#age = int(input("Сколько вам лет?"))
#print("Вы родились в  ", 2022-age, "году")

#Функция eval()
#txt = "(2*2+32)/2"
#print(txt, "=", eval(txt))

#список
#создание списка
# nums = [1, 7, -22]
# nums2 = list("text")
# print("nums = ", nums)
# print("nums2 = ", nums2)

# n = 2
# m = 10
# nums = list("список числе от n до m", range(n, m+1))

#длина списка
# nums = [1, 7, -22, 11, 94, 2, 9, 200029, 345, 2]
# print("длина списка = ", len(nums))

#Срез
import time

nums = [10, 7, -22, 11, 94, 2, 9, 200029, 345, 23]
# print(nums[1])
# print(nums[0:3])
# print(nums[-1])
# print(nums[5:])
# print(nums[:7])
# print("наибольшее значение", max(nums))
# print("наименьшее значение", min(nums))
# print("сумма всех чисел списка", sum(nums))
# print("список в обратном порядке", list(reversed(nums)))
# print("сортировка списка по возрастанию ", sorted(nums))
# print("сортировка списка по убыванию ", sorted(nums, reverse=True))

#Изменение элемента списка
# nums[0] = "text"
# print(nums)

#Замена части элементов списка
# nums[0:5] = ["A", "B"]
# print(nums)

#Список чисел от n до m
# n = 2
# m = 10
# nums = list("список числе от n до m", range(n, m+1))
# print(nums)

# Удаление элементов из списка
# nums[2:7] = []
# print(nums)

#нечетные числа
# nums3 = [2*k+1 for k in range(5)]
# print(nums3)

# #удаление символа
# del nums3[len(nums3)-1]
# print(nums3)

#четное число или нечетное
# number = int(input("Введите целое число "))
# if number % 2 == 0:
#     print("число ", number, "четное")
# else:
#     print("число ", number, "нечетное")

# Считывание верхней границы суммы
# n = int(input("укажите верхнюю границу суммы:"))
# s = 0 #начальное значение
# k = 0 #начальное значение индексной переменной
# while k < n:
#     k = k + 1
#     s = s + k
# print("сумма чисел от 0 до ", n, "равна", s)

#Альтернативный способ вычисления суммы
# n = input("укажите количество слагаемых: ")
# txt = "1"
# k = 1
# while str(k) != n:
#     k = k + 1
#     txt = txt+ "+" +str(k)
#     print(txt, "=", eval(txt))
# print(txt, "=", eval(txt))

# Функция для отображения букв из переданного аргументом текста
# def show(txt):
#     symbs = sorted(list(txt))
#     print(symbs)
# show("Python")

#Функция для вычисления суммы квадратов натуральных чисел
# def sqsum(n):
#     nums = [k*k for k in range(1, n+1)]
#     return sum(nums)
# m = 10
# print("сумма квадратов чисел от 1 до", str(m)+":", sqsum(m))

#УПРАВЛЯЮЩИЕ ИНСТРУКЦИИ ЯЗЫКА

# % - остаток от деления
# // - целочисленное деление
# int() - преобразование к числовому формату
# str() - преобразование к текстовому формату

# Отображение состава числа в обратном порядке
# number = int(input("Введите число: "))
# while number > 0:
#     digit = number % 10
#     print("|"+str(digit), end="")
#     number = number // 10
# print("|")

# Перебор элементов списка
# colors = ("синий", "белый", "желтый", "красный")
# print(colors)
# for s in colors:
#     print(s, "->", len(s))

# Числа Фибоначчи
# n = 15
# a, b = 1, 1
# print(a)
# print(b)
# print(a, b, end=" ")
# for k in range(n-2):
#     a, b=b, a+b
#     print(b, end=" ")

#Поиск букв в тексте
# mytext = input("Введите текст для проверки: ")
# symbs = ['q', 'a', 'r']
# print("ищем такие буквы: ", symbs)
# for s in symbs:
#     if s in mytext:
#         print("в тексте есть буква '"+s+"'")
#         break
#     else:
#         print("в тексте нет буквы '"+s+"'")
# else:
#     print("таких букв в тексте нет")
# print("поиск завершен")


# Наличие в списке элемента с данным значением
# значение in список

# Решение линейного уравнения
# print("введите два числа через запятую. Эти числа соответствуют А, B  в уравнении A*x = B: ")
# A, B = eval(input()) # считываем значения и присваиваем
# #print(A, B)
# #print(type(A)) # определяем тип данных
# if (type(A) == int or type(A) == float) and (type(B) == int or type(B) == float):
#     print("решаем уравнение ", A, "x", " = ", B)
#     if (A != 0):
#         x = B/A
#         print("x = ", x)
#     else:
#         if B == 0:
#             print("х - любое число")
#         else:
#             print("решений нет")
# else:
#     print("введены некорректные значения")

# Альтернативный способ использования if
# print("введите два числа через запятую. Эти числа соответствуют А, B  в уравнении A*x = B: ")
# A, B = eval(input()) # считываем значения и присваиваем
# if (type(A) == int or type(A) == float) and ((type(B) == int or type(B) == float) and (A != 0)):
#     print("решаем уравнение ", A, "x", " = ", B)
#     x = B/A
#     print("x = ", x)
# elif (A == 0) and (B != 0):
#     print("х - нет решений")
# elif (A == 0) and (B == 0):
#     print("х - любое число")

# Преобразование в нижний/верхний  регистр
# txt = input("введите текст содержащий символы в верхнем регистре или нижнем регистре")
# txt = txt.lower()
# print(txt)
# txt = txt.upper()
# print(txt)

#Тернарный оператор
#Проверка числа на четность/нечетность
# num = int(input("введите целое число"))
# res = "четное" if num % 2 == 0 else "нечетное"
# print("это "+res+" число")


# import math
# fun = lambda x : 1 if x == 1 else math.ceil(math.sinh(fun (x-1)))
# print(fun(5))

# # КЕЙС 1
# import time
#
# # webdriver это и есть набор команд для управления браузером
# from selenium import webdriver
#
# # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
# driver = webdriver.Chrome()
#
# # команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
# time.sleep(5)
#
# # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
# driver.get("https://stepik.org/lesson/25969/step/12")
# time.sleep(5)
#
# # Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# # Ищем поле для ввода текста
# textarea = driver.find_element_by_css_selector(".textarea")
#
# # Напишем текст ответа в найденное поле
# textarea.send_keys("get()")
# time.sleep(5)
#
# # Найдем кнопку, которая отправляет введенное решение
# submit_button = driver.find_element_by_css_selector(".submit-submission")
#
# # Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
# submit_button.click()
# time.sleep(5)
#
# # После выполнения всех действий мы должны не забыть закрыть окно браузера
# driver.quit()


#-------------------------------------------------------------------------------------------
## найти кнопку со значением id="submit_button":
# from selenium import webdriver
#
# browser = webdriver.Chrome() #инициализировали браузер
# browser.get("http://suninjuly.github.io/simple_form_find_task.html") #открыли нужную страницу по ссылке
# button = browser.find_element_by_id("submit_button") # нашли элемент по id и назвали его
# browser.quit()


## Альтернативный способ найти кнопку найти кнопку со значением id="submit_button":
# from selenium import webdriver
#
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/simple_form_find_task.html")
# button = browser.find_element(By.ID, "submit_button")
# browser.quit()
# ------------------------------

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
# browser = webdriver.Chrome()
# browser.get(link)
# button = browser.find_element(By.ID, "submit_button")
# button.click()

# закрываем браузер после всех манипуляций
# browser.quit()

# ---------------

#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     button = browser.find_element(By.ID, "submit_button")
#     button.click()
#
# finally:
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# --------------------
# from selenium import webdriver
# import time
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element_by_tag_name("body div form div input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name("city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys("Russia")
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла


# ----------------------------------------------------------------------------------------------------

# from selenium import webdriver
# import time
# import math
#
# link = "http://suninjuly.github.io/find_link_text"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     link = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
#     link.click()
#
#     input1 = browser.find_element_by_tag_name("body div form div input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name("city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys("Russia")
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла

# -------------------------------------------------------------
#
# from selenium import webdriver
# import time
#
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     from selenium.webdriver.common.by import By
#     elements = browser.find_elements(By.CSS_SELECTOR, ".first_block input")
#     for element in elements:
#         element.send_keys("nnn")
#
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла
#
#
#
#
# ------------------------------------------------------------------------------------------------------


#
# from selenium import webdriver
# import time
#
# link = "http://suninjuly.github.io/find_xpath_form"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element_by_tag_name("body div form div input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name("city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys("Russia")
#     button = browser.find_element_by_xpath("//button[text()='Submit']")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла
#

# -------------------------------------------------------------------

# from selenium import webdriver
# import time
#
# try:
#     link = "http://suninjuly.github.io/registration1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # Ваш код, который заполняет все поля
#     input_name = browser.find_element_by_tag_name("body div form div input")
#     input_name.send_keys("Ivan")
#     input_last_name = browser.find_element_by_class_name("first_block .second")
#     input_last_name.send_keys("Petrov")
#     input_email = browser.find_element_by_css_selector(".first_block [placeholder='Input your email']")
#     input_email.send_keys("email@list.ru")
#     input_phone = browser.find_element_by_css_selector(".second_block [placeholder='Input your phone:']")
#     input_phone.send_keys("Russia")
#     input_address = browser.find_element_by_css_selector(".second_block [placeholder='Input your address:']")
#     input_address.send_keys("Russia")
#
#     # Отправляем заполненную форму
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(1)
#
#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element_by_tag_name("h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text
#     # print(welcome_text)
#
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(3)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# -----------------------------------------------------------------------

# # 1.6 Уникальность селекторов: часть 2
# from selenium import webdriver
# import time
#
# try:
#     link = "http://suninjuly.github.io/registration1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # Ваш код, который заполняет обязательные поля
#     input_name = browser.find_element_by_tag_name("body div form div input")
#     input_name.send_keys("Ivan")
#     time.sleep(3)
#     input_last_name = browser.find_element_by_class_name("first_block .second")
#     input_last_name.send_keys("Petrov")
#     time.sleep(3)
#     input_email = browser.find_element_by_css_selector(".first_block [placeholder='Input your email']")
#     input_email.send_keys("email@list.ru")
#     time.sleep(3)
#
#     # Отправляем заполненную форму
#     button = browser.find_element_by_css_selector("button.btn")
#     time.sleep(3)
#     button.click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(1)
#
#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element_by_tag_name("h1")
#     time.sleep(3)
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text
#
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(3)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# ------------------------------------------------------------------------------------------
# #1.7 Задание: уникальность селекторов
#
# from selenium import webdriver
# import time
#
# try:
#     link = "http://suninjuly.github.io/registration1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # Ваш код, который заполняет обязательные поля
#     input_name = browser.find_element_by_tag_name("body div form div input")
#     input_name.send_keys("Ivan")
#     time.sleep(3)
#     input_last_name = browser.find_element_by_class_name("first_block .second")
#     input_last_name.send_keys("Petrov")
#     time.sleep(3)
#     input_email = browser.find_element_by_css_selector(".first_block [placeholder='Input your email']")
#     input_email.send_keys("email@list.ru")
#     time.sleep(3)
#
#
#     # Отправляем заполненную форму
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(3)
#
#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element_by_tag_name("h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text
#
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(3)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

#
# -----------------------

# A=[0]
# print(A)
# A=[[0]*3]*2
# print(A)
# A[0][1]=1
# print(A)
# A[1][1]=2
# print(A)
# C=A[1]
# print(C)
# B=A[0]
# B[1]=1
# print(B)
#
# d=[B,C]
# print(d)

# ------------------------------------------------------------------------

# from random import *
# A=[[(j+1)*10+i+1 for i in range(5)] for j in range(3)]
# # print(A)
#
# def show(A):
#     for a in A:
#         for s in a:
#             print(s, end="  ")
#         print()
#
#
# show(A)
#

# ---------------------

# # создание поврехностной копии
# # исходный список
# A = [1, 3, [10, 20], "Pyton", [40, 50]]
# B = A[:] # создание копии как среза
# C = A.copy() # прямое создание копии
# print("Исходные значения: ")
# print("A: ", A)
# print("B: ", B)
# print("C: ", C)
# # Внесение изменений в исхоный список
# A[0] = [100, 200]
# A[2][1] = 300
# A[3] = "Java"
# A[4] = 90
# C[4][1] = "C++"
# print("после внесения изменений")
# print("A: ", A)
# print("B: ", B)
# print("C: ", C)

# # создание полной копии списка
# from copy import  deepcopy # импорт функции для создания полной копии
# # исходный список
# A = [1, 3, [10, 20], "Pyton", [40, 50]]
# B = deepcopy(A) # создание полной копии копии
# print("Исходные значения: ")
# print("A: ", A)
# print("B: ", B)
# # Внесение изменений в исхоный список
# A[0] = [100, 200]
# A[2][1] = 300
# A[3] = "Java"
# A[4] = 90
# print("после внесения изменений")
# print("A: ", A)
# print("B: ", B)


#-----------------------------------------------------------------------------

# # 2.1 Основные методы Selenium
# # Ваша программа должна выполнить следующие шаги:
#
#
# from selenium import webdriver
# import time
# import math
#
#
# try:
#
#     link = "http://suninjuly.github.io/math.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     def calc(x):
#       return str(math.log(abs(12*math.sin(int(x)))))
#
# # Считать значение для переменной x.
#     x_element = browser.find_element_by_css_selector(".nowrap#input_value")
#     x = x_element.text # Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента
#
# # Посчитать математическую функцию от x (код для этого приведён ниже).
#     y = calc(x)
#
# # Ввести ответ в текстовое поле
#     answer = browser.find_element_by_css_selector("#answer")
#     answer.send_keys(y)
#
# # Отметить checkbox "I'm the robot".
#     option1 = browser.find_element_by_css_selector("[id = 'robotCheckbox']")
#     option1.click()
#
# # Выбрать radiobutton "Robots rule!".
#     option2 = browser.find_element_by_css_selector("#robotsRule")
#     option2.click()
#
# # Нажать на кнопку Submit.
#     button = browser.find_element_by_css_selector(".btn.btn-default")
#     button.click()
#
#
#
# finally:
# # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(9)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#

# ------------------------------------------------------------------------------------------

# # 2.1 Основные методы Selenium
# # Ваша программа должна:
#
# from selenium import webdriver
# import time
# import math
#
#
# try:
# # Открыть страницу http://suninjuly.github.io/get_attribute.html.
#     link = "http://suninjuly.github.io/get_attribute.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     def calc(x):
#       return str(math.log(abs(12*math.sin(int(x)))))
#
# # Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
#     x_element = browser.find_element_by_css_selector("#treasure")
#     x = x_element.get_attribute("valuex") # узнать значение атрибута элемента
#
# # Посчитать математическую функцию от x (код для этого приведён ниже).
#     y = calc(x)
#
# # Ввести ответ в текстовое поле
#     answer = browser.find_element_by_css_selector("#answer")
#     answer.send_keys(y)
#
# # Отметить checkbox "I'm the robot".
#     option1 = browser.find_element_by_css_selector("[id = 'robotCheckbox']")
#     option1.click()
#
# # Выбрать radiobutton "Robots rule!".
#     option2 = browser.find_element_by_css_selector("#robotsRule")
#     option2.click()
#
# # Нажать на кнопку Submit.
#     button = browser.find_element_by_css_selector(".btn.btn-default")
#     button.click()
#
#
#
# finally:
# # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(9)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# -------------------------------------------------------------------------------------

# # 2.2 Работа с файлами, списками и js-скриптами
# # Задание: работа с выпадающим списком
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
#
# try:
#     # Открыть страницу http://suninjuly.github.io/selects1.html или http://suninjuly.github.io/selects2.html
#     link = "http://suninjuly.github.io/selects2.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
# # Посчитать сумму заданных чисел
#     def sum(x1, x2):
#         return str(x1+x2)
#
#     num1 = int(browser.find_element(By.CSS_SELECTOR, "#num1").text)
#     num2 = int(browser.find_element(By.CSS_SELECTOR, "#num2").text)
#     print(num1)
#     print(num2)
#
#     f = sum(num1, num2)
#     print(f)
#     print(type(f))
#
# # Выбрать в выпадающем списке значение равное расчитанной сумме
#     from selenium.webdriver.support.ui import Select
#
#     select = Select(browser.find_element_by_tag_name("select")) #используется специальный класс Select из библиотеки WebDriver. Вначале мы должны инициализировать новый объект, передав в него WebElement с тегом select. Далее можно найти любой вариант из списка с помощью метода select_by_value(value):
#     select.select_by_value(f)
#
# # Нажать кнопку "Submit"
#     button = browser.find_element_by_css_selector(".btn.btn-default")
#     button.click()
# finally:
# # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(5)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
#--------------------------------------------------------------------------------------------


#
# # Задание на execute_script
# # В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным и огромным футером, который дизайнер всё никак не успевает переделать. Вам потребуется написать код, чтобы:
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# import math
#
# # Открыть страницу http://SunInJuly.github.io/execute_script.html.
#
# link = "http://SunInJuly.github.io/execute_script.html"
# browser = webdriver.Chrome()
# browser.get(link)
#
# try:
# # Считать значение для переменной x.
#     x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
#     x = x_element.text
#
# # Посчитать математическую функцию от x.
#     def calc(x):
#         return str(math.log(abs(12*math.sin(int(x)))))
#
#     f = calc(x)
#     print(f)
#
#
#
#
# # Ввести ответ в текстовое поле.
#     answer = browser.find_element(By.CSS_SELECTOR, "#answer")
#     answer.send_keys(f)
#
# # Проскроллить страницу вниз.
#     button = browser.find_element_by_tag_name("button")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", button)  # В метод execute_script мы передали текст js-скрипта и найденный элемент button, к которому нужно будет проскроллить страницу.
#     button.click()
#
# # Выбрать checkbox "I'm the robot".
#     option1 = browser.find_element_by_css_selector("[id = 'robotCheckbox']")
#     option1.click()
#
# # Выбрать radiobutton "Robots rule!".
#     option2 = browser.find_element_by_css_selector("#robotsRule")
#     option2.click()
#
# # Нажать на кнопку "Submit".
#     button = browser.find_element_by_css_selector(".btn.btn-primary")
#     button.click()
#
# finally:
# # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(5)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# #--------------------------------------------------------------------------------------

# # 2.2 Работа с файлами, списками и js-скриптами
# # Задание: загрузка файла
#
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
#
#
#
#
# try:
#     # Открыть страницу http://suninjuly.github.io/file_input.html.
#     link = "http://suninjuly.github.io/file_input.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # 2. Заполнить текстовые поля: имя, фамилия, email
#
#     First_name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
#     First_name.send_keys("Angela")
#     Last_name = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
#     Last_name.send_keys("Mercele")
#     Email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
#     Email.send_keys("adfjla@dkjfls.ru")
#
#
#
#
#     # 3. Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
#     element = browser.find_element(By.CSS_SELECTOR, '[name="file"]')
#     element.send_keys("C:/Users/79194/Desktop/test.txt")
#
#
#     # 4. Нажать кнопку "Submit"
#     button = browser.find_element_by_css_selector(".btn.btn-primary")
#     button.click()
#
# finally:
# # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(5)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# -------------------------------------------------------------------------------------

# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# try:
#     from selenium import webdriver
#
#     browser = webdriver.Chrome()
#     browser.execute_script("alert('Привет, Марго!');")
#     alert = browser.switch_to.alert
#
#     alert_text = alert.text
#     # print(alert_text)
#     alert.accept()
#
#     browser.execute_script("confirm('ты согласен? Та-да-да-да!');")
#     confirm = browser.switch_to.alert
#     # confirm.accept()
#     # time.sleep(2)
#
#     confirm_text = confirm.text
#     # print(confirm_text)
#     confirm.accept()
#
#     browser.execute_script("confirm('ты НЕ согласен? ');")
#     confirm = browser.switch_to.alert
#     confirm.dismiss()
#
#     browser.execute_script("prompt('введи текст')")
#     prompt = browser.switch_to.alert
#     prompt.send_keys("My answer")
#     time.sleep(2)
#     prompt.dismiss()
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(1)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# ------------------------------------------------------------------------
# # 2.3 Работа с окнами
# # Задание: принимаем alert
#
#
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# import math
#
# try:
#     # Открыть страницу  http: // suninjuly.github.io / alert_accept.html
#
#     link = "http://suninjuly.github.io/alert_accept.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # Нажать на кнопку
#     button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
#     button.click()
#
#     # Принять конфирм
#
#     confirm = browser.switch_to.alert
#     confirm.accept()
#
#     x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
#     x = x_element.text
#
#
#     def calc(x):
#          return str(math.log(abs(12*math.sin(int(x)))))
#
#     f = calc(x)
#
#     answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
#     answer_input.send_keys(f)
#
#
#     submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
#     submit.click()
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(5)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
#----------------------------------------------------------------

# # 2.3 Работа с окнами
# # Задание: переход на новую вкладку
#
#
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# import math
#
# try:
#     # Открыть страницу http://suninjuly.github.io/redirect_accept.html
#     browser = webdriver.Chrome()
#     link = "http://suninjuly.github.io/redirect_accept.html"
#     browser.get(link)
#
#     # Нажать на кнопку
#     element = browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary")
#     element.click()
#
#     # Переключиться на новую вкладку
#     new_window = browser.window_handles[1] # Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает массив имён всех вкладок.
#     browser.switch_to.window(new_window) # выбираем вторую вкладку
#
#     # Пройти капчу для робота
#     x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
#     x = x_element.text
#     def calc(x):
#          return str(math.log(abs(12*math.sin(int(x)))))
#     f = calc(x)
#     answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
#     answer_input.send_keys(f)
#
#
#     submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
#     submit.click()
#
# finally:
#
#     browser.quit()
#
# ---------------------------------------------------------------------------------"




#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import math
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
#
# try:
#     # Открыть страницу http://suninjuly.github.io/explicit_wait2.html
#
#     browser = webdriver.Chrome()
#     link = "http://suninjuly.github.io/explicit_wait2.html"
#     browser.get(link)
#     button = browser.find_element(By.CSS_SELECTOR, "#book")
#
#     # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
#     price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"),"$100"))
#     # Нажать на кнопку "Book"
#     button.click()
#
#     # Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
#     x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
#     x = x_element.text
#     def calc(x):
#          return str(math.log(abs(12*math.sin(int(x)))))
#     f = calc(x)
#     answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
#     answer_input.send_keys(f)
#     submit = browser.find_element(By.CSS_SELECTOR, "#solve")
#     submit.click()
#
# finally:
#     time.sleep(5)
#     browser.quit()
#
# ------------------------------------------------------------------
# Тестирование web-приложений и тестовые фреймворки
# Далее мы рассмотрим, как использовать Selenium Webdriver для написания автоматических тестов. Почему мы еще не можем назвать тестами скрипты, которые мы писали в предыдущих модулях?
#
# Для этого нам придётся познакомиться с тестовыми фреймворками unittest и PyTest, которые позволяют создавать легко читаемые проверки ожидаемых результатов в тестах, удобно настраивать запуск большого количества тестов в нужных окружениях, организовывать хранение тестов и генерацию отчётов для последующего анализа.
#
# В качестве основы для данного урока мы адаптировали руководство про написание юнит-тестов в Python:
#
# https://realpython.com/python-testing/


# Автоматизированное и ручное тестирование
# Чтобы начать писать хорошие автотесты, нужно ﻿разобраться, в чем плюсы и минусы ручного и автоматизированного тестирования.
#
# Ручные тесты	Автотесты
# Шаги могут быть описаны достаточно абстрактно, поэтому тестировщик может увидеть новые проблемы, следуя сценарию теста.
#
# В ручном тесте может содержаться шаг "Зарегистрировать нового пользователя" без пояснений, как это делать, в автотесте должны быть строго описаны данные для теста и сценарий регистрации.
#
# Строгий порядок шагов и их чёткая детализация. Проверяют только то, что было заложено изначально в сценарий теста, поэтому могут быть пропущены новые ошибки в продукте.
#
# - Из-за абстрактности описания шагов ручные тесты иногда могут приводить к ложноположительным результатам, когда ожидаемый результат достигнут, но в реальности тестировщик выполнил сценарий неправильно, пропустив баг. 	+ Запуск автотестов обычно приводит к одним и тем же результатам, т.к. сценарий описан точно.
# - Требуется много времени для проверки регрессии, что приводит к усталости тестировщика и ошибкам в проверках из-за человеческого фактора (человеку сложно долго выполнять монотонную работу).	+ Можно запускать на каждый коммит в тестируемом приложении, что позволяет раньше обнаруживать ошибки в продукте.
# Отдельно стоит описать отрицательные стороны автоматизированного тестирования:
#
# возможная нестабильность теста, которая не связана с качеством самого теста, а вызывается внешними проблемами: нестабильное сетевое соединение, проблемы с серверами, обновление кода продукта в момент запуска тестов;
# требуется достаточно много времени на разработку и поддержку набора автотестов.
# Несмотря на наличие минусов автотестов, в большинстве случаев их использование на проекте помогает быстрее находить ошибки в коде приложения и поддерживать качество продукта на достаточном уровне. Автотесты помогают отделу тестирования оптимизировать свою работу, чтобы сделать счастливее пользователей, которые быстрее получают новые фичи и меньше страдают от ошибок в продукте, так как разработчики раньше узнают о багах и могут заранее принять меры для их устранения, не откладывая релиз продукта. Таким образом, благодаря автотестам налаживается бизнес, который может увеличить скорость внедрения фич, приносящих прибыль.
#
# Ручные тесты в идеальном случае остаются только на этапе проверки новых фич и в виде исследовательского тестирования, которое позволяет найти проблемы в сложных пользовательских сценариях.
# #

#
# Юнит-тесты и интеграционные тесты
# Если вы работаете в тестировании, то уже знаете разницу между юнит-тестами и интеграционными тестами. Юнит-тесты проверяют очень маленький кусок кода, обычно конкретную функцию, и чаще всего их пишут разработчики, которые хорошо понимают возможные крайние случаи для своего стека технологий. Интеграционные тесты проверяют взаимодействие сразу нескольких систем. Они могут создаваться и поддерживаться как разработчиками и тестировщиками, так и аналитиками (если для них разработан удобный фреймворк для написания тестов).
#
# Юнит-тесты всегда автоматизированы, так как проверяют непосредственно работу кода. Интеграционные тесты могут быть ручными и автоматизированными. Иногда выделяют отдельную категорию end-to-end (е2е) тестов, которые проверяют полный стек технологий приложения и пользовательский сценарий взаимодействия с приложением как с черным ящиком. Если говорить про UI-тесты, которые разрабатываются с помощью Selenium, то их стоит отнести к разряду end-to-end тестов, так как они проверяют совместную работу всех систем web-продукта: работу frontend и backend, работу базы данных, дополнительные сервисы, такие как аналитика, платежные системы и так далее.
#
# Подробно про разные типы автотестов мы говорить не будем, но советуем вам изучить теорию самостоятельно. Вот, например, отличная и подробная статья: Пирамида тестов на практике.
# #

#
# Структура теста
# Для написания UI-тестов можно использовать те же возможности Python, что и для написания юнит-тестов, которые создаются разработчиками.
#
# Любой тест должен содержать:
#
# Входные данные.
# Тестовый сценарий, то есть набор шагов, которые надо выполнить для получения результата.
# Проверка ожидаемого результата.
# Давайте обсудим, как именно можно производить проверки.

#
# Проверка ожидаемого результата
# Как можно проверить ожидаемый результат? Для этого используется встроенная в Python инструкция assert, которая проверяет истинность утверждений. assert True не приводит к выводу дополнительных сообщений, а вот assert False вызовет исключение AssertionError.
#
# Рассмотрим работу assert на примере встроенной функции abs(), которая возвращает абсолютное значение числа по модулю. Для этого активируйте созданное ранее виртуальное окружение и запустите интерпретатор Python. Например, для Linux выполните:
#
# source selenium_env/bin/activate
#
# python
# Теперь будем вводить приведенные ниже команды и смотреть на результат их выполнения.
#
# Если значение выражения истинно, то в консоли не должно появиться дополнительных сообщений. Выполним:
#
# >>> assert abs(-42) == 42
#
# Если условие не выполнено, то в консоли выводится лог ошибки с названием файла и номером строчки, в которой произошла ошибка, а также тип ошибки AssertionError:
#
#
# >>> assert abs(-42) == -42
#
# Traceback (most recent call last):
#
#   File "<stdin>", line 1, in <module>
#
# AssertionError
# Простое сообщение AssertionError не очень информативно. Когда тестов становится много, бывает сложно вспомнить, что именно мы проверяем в данном тесте. Для добавления дополнительного сообщения можно при вызове assert через запятую написать нужное сообщение, которое будет выведено в случае ошибки проверки результата:
#
#
# >>> assert abs(-42) == -42, "Should be absolute value of a number"
#
# Traceback (most recent call last):
#
#   File "<stdin>", line 1, in <module>
#
# AssertionError: Should be absolute value of a number



# Составные сообщения об ошибках
# Отдельно хочется поговорить про качество сообщений об ошибках, которые показываются при падении теста. Почему это важно? Хорошо написанный текст помогает быстро локализовать найденный баг и разобраться в том, что произошло и из-за чего тест упал. Хороший assert сэкономит вам часы вашей работы, особенно когда количество тестов переходит за сотню.
#
# В целом, тут как с любым фидбеком: важно давать его точно и актуально. Если вы проверяете наличие элемента, то обязательно пишите, что это за элемент по смыслу на странице:
#
# assert self.is_element_present('create_class_button', timeout=30), "No create class button"
# Примечание: Функция is_element_present() вспомогательная. Как её реализовать и использовать, мы разберемся чуть позжe.
#
# Если элемент встречается на нескольких страницах приложения, не лишним будет указать, где именно произошла ошибка:
#
# assert self.is_element_present('new_announcement_button', timeout=30), "No new announcement button on profile page"
# Если вы работаете с каким-то текстом (например, проверяете информационное сообщение, текущий url, ссылку, placeholder в input-элементе или любой другой текст), в сообщении об ошибке всегда лучше выводить оба значения: то, которое ожидалось, и то, которое получили по факту. Всё как в хорошем багрепорте: ожидаемый и фактический результат.
#
# Форматирование строк с помощью конкатенации
# В питоне такое можно провернуть с помощью конкатенации строк, например:
#
# actual_result = "abrakadabra"
# print("Wrong text, got " + actual_result + ", something wrong")
# Но из-за обилия кавычек, знаков сложения и вот этого всего этот способ не самый удобный и читается тоже плохо.
#
# Форматирование строк с помощью str.format
# Гораздо лучше воспользоваться возможностью python для форматирования строк. Дополнительно можно почитать здесь: https://realpython.com/python-string-formatting/#2-new-style-string-formatting-strformat
#
# Если вкратце, то python умеет подставлять пользовательские значения в строки с помощью функции .format(). Синтаксис выглядит примерно так:
#
# "Let's count together: {}, then goes {}, and then {}".format("one", "two", "three")
# Попробуйте запустить её в интерпретаторе:
#
# print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))
# Такая строка при исполнении кода превратится в:
#
# Let's count together: one, then goes two, and then three
# Таким образом мы можем удобно компоновать ожидаемое и фактическое значение в одну строку.
#
# Форматирование строк с помощью f-strings
# И наконец наиболее современный способ форматирования строк, который появился в Python3.6, носит название f-strings. Он позволяет исполнять выражения на Python прямо внутри строк, обладает еще большей лаконичностью и удобством использования. Для использования возможностей f-strings нужно указывать символ f перед строкой в таком формате: f"ваша строка {my_var}". В фигурных скобках указывается имя переменной, значение которой надо подставить в строку, или выражение, результат исполнения которого также требуется подставить в вашу строку.
#
# Подробнее про f-strings можно почитать здесь: https://realpython.com/python-string-formatting/#3-string-interpolation-f-strings-python-36. Так как мы предполагаем, что вы используете последнюю версию Python, то предлагаем вам применять именно этот подход в данном курсе.
#
# Пример 1:
#
# str1 = "one"
# str2 = "two"
# str3 = "three"
# print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")
# Итог выполнения выражений в интерпретаторе:
#
# Let's count together: one, then goes two, and then three
# Пример 2:
#
# actual_result = "abrakadabra"
# f"Wrong text, got {actual_result}, something wrong"
# Итог выполнения выражений в интерпретаторе:
#
# Wrong text, got abrakadabra, something wrong
# Пример 3:
#
# >>> f"{2+3}"
# '5'
#
#
# Еще один важный момент: когда вы работаете с текстом элементов на странице или любым другим контентом, который может измениться, всегда записывайте его в отдельную переменную для сравнения.
#
# неправильно:
#
# assert self.catalog_link.text  == "Каталог", \
#     f"Wrong language, got {self.catalog_link.text} instead of 'Каталог'"
# Дважды считывать атрибут — это плохая практика, потому что при повторном считывании текст на странице может измениться, и вы получите неактуальный текст об ошибке. Результат выполнения такого теста сложно анализировать:
#
# "Wrong language, got 'Каталог' instead of 'Каталог'"
# правильно:
#
# catalog_text = self.catalog_link.text # считываем текст и записываем его в переменную
# assert catalog_text == "Каталог", \
#     f"Wrong language, got {catalog_text} instead of 'Каталог'"


# Задание: составные сообщения об ошибках
# Для закрепления материала реализуйте проверку самостоятельно.
#
# Вам дана функция test_input_text,  которая принимает два значения: expected_result — ожидаемый результат, и actual_result — фактический результат. Обратите внимание, input использовать не нужно!
#
# Функция должна проверить совпадение значений с помощью оператора assert и, в случае несовпадения, предоставить исчерпывающее сообщение об ошибке.
#
# Важно! Формат ошибки должен точно совпадать с приведенным в примере, чтобы его засчитала проверяющая система!
#
# Маленький совет: попробуйте воспользоваться кнопкой "Запустить код" и протестируйте ваш код на разных введенных значениях, проверьте вывод вашей функции на разных парах. Обрабатывать ситуацию с пустым или невалидным вводом не нужно.
#
# Sample Input 1:
#
# 8 11
# Sample Output 1:
#
# expected 8, got 11
# Sample Input 2:
#
# 11 11
# Sample Output 2:
#
# Sample Input 3:
#
# 11 15
# Sample Output 3:
#
# expected 11, got 15
# Напишите программу. Тестируется через stdin → stdout
#
# def test_input_text(expected_result, actual_result):
#     # ваша реализация, напишите assert и сообщение об ошибке
#     assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"
#
#---------------------------------------------------------------------------------------------------------
#
# Задание: составные сообщения об ошибках и поиск подстроки
# Иногда при работе с текстами не нужны жёсткие проверки на полное совпадение, и требуется проверить, что некий текст является подстрокой другого текста. Это можно сделать либо с помощью ключевого слова in, либо с помощью функции find:
#
# s = 'My Name is Julia'
#
# if 'Name' in s:
#     print('Substring found')
#
# index = s.find('Name')
# if index != -1:
#     print(f'Substring found at index {index}')
# Попробуйте запустить этот код в интерпретаторе, чтобы понять разницу в подходах.
#
# Конструкция 'Name' in s возвращает просто True или False, a find() возвращает индекс первого вхождения подстроки в строку и -1, если подстрока не найдена. Обычно в автотестах достаточно использовать in, потому что это более читабельный вариант.
#
# Например, для проверки того, что в текущем url содержится строка login:
#
# assert "login" in browser.current_url, # сообщение об ошибке
# Реализуйте подобную проверку самостоятельно.
#
# Вам дан шаблон для функции test_substring, которая принимает два значения: full_string и substring.
#
# Функция должна проверить вхождение строки substring в строку full_string с помощью оператора assert и, в случае несовпадения, предоставить исчерпывающее сообщение об ошибке.
#
# Важно! Формат ошибки должен точно совпадать с приведенным в примере, чтобы его засчитала проверяющая система!
#
# Маленький совет: попробуйте воспользоваться кнопкой "Запустить код" и протестируйте ваш код на разных введенных значениях, проверьте вывод вашей функции на разных парах. Обрабатывать ситуацию с пустым или невалидным вводом не нужно.
#
# Sample Input 1:
#
# fulltext some_value
# Sample Output 1:
#
# expected 'some_value' to be substring of 'fulltext'
# Sample Input 2:
#
# 1 1
# Sample Output 2:
#
# Sample Input 3:
#
# some_text some
# Sample Output 3:
#
# def test_substring(full_string, substring):
#     # ваша реализация, напишите assert и сообщение об ошибке
#     assert substring in full_string, f"expected \'{substring}\' to be substring of \'{full_string}\'"

# Тестовые сценарии
# Созданные тесты нужно сохранить в файле, чтобы его было удобно запускать и хранить в системе контроля версий. Давайте создадим файл test_abs_project.py и напишем в нём следующий код:
#
# def test_abs1():
#     assert abs(-42) == 42, "Should be absolute value of a number"
#
# if __name__ == "__main__":
#     test_abs1()
#     print("All tests passed!")
# Мы поместили тестовый сценарий в функцию для разделения тест-кейсов и возможности их независимого запуска.
#
# Не вдаваясь в подробности, скажем только, что конструкция if __name__ == "__main__" служит для подтверждения того, что данный скрипт был запущен напрямую, а не вызван внутри другого файла в качестве модуля. Весь код написанный в теле этого условия будет выполнен только если пользователь запустил файл самостоятельно. Подробнее можно ознакомиться в видео Олега Молчанова.
#
# В этой конструкции мы вызвали функцию test_abs1(), которая выполняет тестовый сценарий.
#
# С помощью print("All tests passed!") мы вывели сообщение, если все тесты прошли успешно.
#
# Чтобы запустить тест, выполните в консоли команду:
#
# python test_abs_project.py
# Вы должны увидеть в консоли сообщение "All tests passed!".
#
#
#
# Если нам нужно добавить еще один тест, мы можем написать его как функцию в этом же файле. В приведенном примере мы уже не увидим сообщение "Everything passed", так как падение любого теста вызывает выход из программы:
#
# def test_abs1():
#     assert abs(-42) == 42, "Should be absolute value of a number"
#
# def test_abs2():
#     assert abs(-42) == -42, "Should be absolute value of a number"
#
# if __name__ == "__main__":
#     test_abs1()
#     test_abs2()
#     print("Everything passed")
# Запустите файл снова. Вы должны увидеть сообщение об упавшем втором тесте:
#
#
# $ python test_abs_project.py
#
# Traceback (most recent call last):
#
#   File "test_abs_project.py", line 9, in <module>
#
#     test_abs2()
#
#   File "test_abs_project.py", line 5, in test_abs2
#
#     assert abs(-42) == -42, "Should be absolute value of a number"
#
# AssertionError: Should be absolute value of a number


