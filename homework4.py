# Задача №1
# Лекция №4: Условные операторы
# Тема: Оператор if
#
# 1. Создай переменную `status_code` со значением 200.
# 2. Если `status_code` равен 200, выведи сообщение "Test passed".
# 3. Если условие не выполняется, программа ничего не должна выводить.
#
# Ожидаемый результат:
# Test passed

# Напиши своё решение ниже:

print("---------- Задача №1 ----------")

status_code = 200

if status_code == 200:
    print("Test passed")

# Задача №2
# Лекция №4: Условные операторы
# Тема: Логические операции в условиях
#
# 1. Создай переменную `status_code` со значением 200.
# 2. Создай переменную `response_time` со значением 1.5.
# 3. Если `status_code` равен 200 И `response_time` меньше 2,
#    выведи сообщение "Test passed".
# 4. Иначе выведи сообщение "Test failed".
#
# Ожидаемый результат:
# Test passed

# Напиши своё решение ниже:

print("---------- Задача №2 ----------")

status_code = 200
response_time =1.5
if status_code == 200 and response_time < 2:
    print("Test passed")
else:
    print("Test failed")

# Задача №3
# Лекция №4: Условные операторы
# Тема: Оператор elif
#
# 1. Создай переменную `status_code` со значением 404.
# 2. Если `status_code` равен 200, выведи "Success".
# 3. Если `status_code` равен 404, выведи "Not found".
# 4. Во всех остальных случаях выведи "Unknown status".
#
# Ожидаемый результат:
# Not found

# Напиши своё решение ниже:

print("---------- Задача №3 ----------")
status_code = 404
if status_code == 200:
    print("Success")
elif status_code == 404:
    print("Not found")
else:
    print("Unknown status")

# Задача №4
# Лекция №4: Условные операторы
# Тема: Тернарный оператор
#
# Дано:
# test_status = "PASSED"
#
# Используя тернарный оператор:
# 1. Если test_status равен "PASSED", присвой переменной result значение "Success".
# 2. Иначе присвой result значение "Failure".
# 3. Выведи result.
#
# Ожидаемый результат:
# Success

test_status = "PASSED"

# Напиши своё решение ниже:

print("---------- Задача №4 ----------")

result = "Success" if test_status == "PASSED" else "Failure"
print(result)

# Задача №5
# Лекция №4: Условные операторы
# Тема: Логические операции or и not
#
# Дано:
# browser = "Firefox"
# is_supported = False
#
# 1. Если browser равен "Chrome" ИЛИ is_supported равен True,
#    выведи "Browser accepted".
# 2. Во всех остальных случаях выведи "Browser rejected".
#
# Ожидаемый результат:
# Browser rejected

browser = "Firefox"
is_supported = False

# Напиши своё решение ниже:

print("---------- Задача №5 ----------")

if browser == "Chrome" or is_supported == True:
    print("Browser accepted")
else :
    print("Browser rejected")

# Задача №6
# Лекция №4: Условные операторы
# Тема: Логические операции в условиях
#
# Дано:
# attempts = 2
# is_locked = False
#
# 1. Если количество попыток меньше 3 И аккаунт НЕ заблокирован,
#    выведи "Login allowed".
# 2. Во всех остальных случаях выведи "Login denied".
#
# Ожидаемый результат:
# Login allowed

attempts = 2
is_locked = False

# Напиши своё решение ниже:
print("---------- Задача №6 ----------")

if attempts <  3 and is_locked == False:
    print("Login allowed")
else:
    print("Login denied")

# Задача №7
# Лекция №4: Условные операторы
# Тема: Логические операции and, or, not
#
# Дано:
# status_code = 200
# response_time = 3.5
# is_blocked = False
#
# 1. Если status_code равен 200 И response_time меньше 3,
#    ИЛИ аккаунт не заблокирован,
#    выведи "Test passed".
# 2. Иначе выведи "Test failed".
#
# Ожидаемый результат:
# Test passed

status_code = 200
response_time = 3.5
is_blocked = False

# Напиши своё решение ниже:

print("---------- Задача №7 ----------")

if status_code == 200 and response_time < 3 or is_blocked == False:
    print("Test passed")
else:
    print("Test failed")