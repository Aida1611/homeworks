##return-возвращать-кайтаруу-дайыма функциянын ичине жазылат
##1
def add(a, b):
    return a + b
res = add(1, 2)
print(res)

##2
def add(a, b):
    ## a = 1
    ## b = 2
    print(a + b)
res = add(1, 2)
print(res)

##3
def weather(celsius):
    if celsius < 0:
        return "Аба ырайы суук"
    elif 0< celsius < 20:
        return "Аба ырайы жылуу"
    else:
        return "Аба ырайы ысык"
print(weather(25))
print(weather(1))
print(weather(-4))
