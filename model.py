# def custom_sum (a, b):
#     print(a + b)
#
# def custom_sub(a, b):
#     print(a -b)

def custom_sum (a, b):
    return a+ b

def custom_sub(a, b):
    return a-b

def season(month):
    if 1 <= month <= 2 or month == 12:
        return "Зима"
    elif 3 <= month <= 5:
        return "Весна"
    elif 5 < month < 9:
        return "Лето"
    elif 9 <= month <= 11:
        return "Осень"
    else:
        return "Другое"


lang = {
    'ru': 'Привет',
    'en': 'Hello',
    'es': 'Hola',
    'fr': 'Bonjour',
    'de': 'Hallo',
    'it': 'Ciao',
    'zh': '你好',
    'ja': 'こんにちは'
}
def greet (language_code):
   if language_code in lang:
       return lang[language_code]
   else:
       return 'Язык не поддерживается'


user_data = []
def add_user(username):
    user_data.append(username)
    return f'Пользователь {username} добавлен'

def get_user():
    return user_data

def delete_user(username):
    if username in user_data:
        user_data.remove(username)
        return f'Пользователь {username} удален'
    else:
        return f'Пользователь {username} не ненайден'
