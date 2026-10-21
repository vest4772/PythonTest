# Задача №1
# Тема: Срезы списков
#
# Создай список `test_results` со значениями:
# "PASSED", "FAILED", "PASSED", "SKIPPED", "PASSED", "FAILED"
#
# Используя срезы списка:
# 1. Выведи первые три элемента.
# 2. Выведи последние два элемента.
# 3. Выведи элементы с индексами от 1 до 4, не включая индекс 4.
# 4. Выведи список в обратном порядке.
#
# Ожидаемый результат:
# ['PASSED', 'FAILED', 'PASSED']
# ['PASSED', 'FAILED']
# ['FAILED', 'PASSED', 'SKIPPED']
# ['FAILED', 'PASSED', 'SKIPPED', 'PASSED', 'FAILED', 'PASSED']

# Напиши своё решение ниже:

print("---------- Задача №1 ----------")

test_results = ["PASSED", "FAILED", "PASSED", "SKIPPED", "PASSED", "FAILED"]

print(test_results[0:3])

print(test_results[-2:])

print(test_results[1:4])

print(test_results[::-1])


# Задача №2
# Лекция №3: Списки в Python
# Тема: Добавление элементов в конкретное место списка
#
# Создай список `test_cases` со значениями:
# "Login", "Logout", "Registration"
#
# 1. Добавь элемент "Payment" на индекс 1.
# 2. Выведи получившийся список.
# 3. Добавь элемент "Search" на индекс 0.
# 4. Выведи обновлённый список.
#
# Ожидаемый результат:
# ['Login', 'Payment', 'Logout', 'Registration']
# ['Search', 'Login', 'Payment', 'Logout', 'Registration']

# Напиши своё решение ниже:

print("---------- Задача №2 ----------")
test_cases = ["Login", "Logout", "Registration"]
test_cases.insert(1,"Payment")
print(test_cases)
test_cases.insert(0,"Search")
print(test_cases)


# Задача №3
# Лекция №3: Списки в Python
# Тема: Удаление элементов из списка
#
# Создай список `test_statuses` со значениями:
# "PASSED", "FAILED", "SKIPPED", "FAILED", "PASSED"
#
# 1. Удали первое вхождение элемента "FAILED" по его значению.
# 2. Выведи список.
# 3. Удали элемент с индексом 1.
# 4. Выведи обновлённый список.
# 5. Очисти список полностью.
# 6. Выведи пустой список.
#
# Ожидаемый результат:
# ['PASSED', 'SKIPPED', 'FAILED', 'PASSED']
# ['PASSED', 'FAILED', 'PASSED']
# []

# Напиши своё решение ниже:

print("---------- Задача №3 ----------")

test_statuses =["PASSED", "FAILED", "SKIPPED", "FAILED", "PASSED"]
test_statuses.remove("FAILED")
print(test_statuses)
test_statuses.pop(1)
print(test_statuses)
test_statuses.clear()
print(test_statuses)

# Задача №4
# Лекция №3: Списки в Python
# Тема: Замена элементов списка
#
# Создай список `test_names`:
# "Login", "Search", "Checkout", "Profile"
#
# 1. Замени элемент с индексом 1 на "Registration".
# 2. Замени последний элемент на "Logout".
# 3. Выведи итоговый список.
# 4. Выведи количество элементов в списке.
#
# Ожидаемый результат:
# ['Login', 'Registration', 'Checkout', 'Logout']
# 4

# Напиши своё решение ниже:
print("---------- Задача №4 ----------")
test_names = ["Login", "Search", "Checkout", "Profile"]
test_names[1]= "Registration"
test_names[-1]= "Logout"
print(test_names)
print(len(test_names))

# Задача №5
# Лекция №3: Списки в Python
# Тема: Добавление элементов в конец списка
#
# Создай список `test_tools` со значениями:
# "Pytest", "Selenium"
#
# 1. Добавь в конец списка "Requests".
# 2. Добавь в конец списка "Playwright".
# 3. Выведи итоговый список.
# 4. Выведи количество элементов в списке.
#
# Ожидаемый результат:
# ['Pytest', 'Selenium', 'Requests', 'Playwright']
# 4

# Напиши своё решение ниже:

print("---------- Задача №5 ----------")
test_tools = ["Pytest", "Selenium"]
test_tools.append("Requests")
test_tools.append("Playwright")
print(test_tools)
print(len(test_tools))

# Задача №6
# Лекция №3: Списки в Python
# Тема: Объединение списков
#
# Создай два списка:
# `smoke_tests` = ["Login", "Logout"]
# `api_tests` = ["Get User", "Create User"]
#
# 1. Объедини оба списка в новый список `all_tests`.
# 2. Выведи `all_tests`.
# 3. Выведи количество элементов в `all_tests`.
# 4. Убедись, что исходные списки остались без изменений.
#
# Ожидаемый результат:
# ['Login', 'Logout', 'Get User', 'Create User']
# 4
# ['Login', 'Logout']
# ['Get User', 'Create User']

# Напиши своё решение ниже:

print("---------- Задача №6 ----------")

smoke_tests = ["Login", "Logout"]
api_tests = ["Get User", "Create User"]

all_tests = smoke_tests + api_tests
print(all_tests)
print(len(all_tests))
print(smoke_tests)
print(api_tests)

# Задача №7
# Лекция №3: Списки в Python
# Тема: Получение элементов и замена по индексу
#
# Создай список `test_cases`:
# "Login", "Search", "Payment", "Logout", "Registration"
#
# 1. Выведи первый элемент списка.
# 2. Выведи последний элемент списка.
# 3. Замени элемент с индексом 2 на "Checkout".
# 4. Выведи первые три элемента списка.
# 5. Выведи итоговый список целиком.
#
# Ожидаемый результат:
# Login
# Registration
# ['Login', 'Search', 'Checkout']
# ['Login', 'Search', 'Checkout', 'Logout', 'Registration']

# Напиши своё решение ниже:

print("---------- Задача №7 ----------")

test_cases =["Login", "Search", "Payment", "Logout", "Registration"]
print(test_cases[0])
print(test_cases[-1])
test_cases[2] ="Checkout"
print(test_cases[:3])
print(test_cases)

