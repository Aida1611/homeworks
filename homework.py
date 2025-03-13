#function-созсуз башы dev деп баштала
def func():
    print("Python")
    print("Java")
    print("C++")
    print("#" * 10)

func()
func()
func()  ##канча жолу жазса ошончо жолу чыгат

print()


def func():
    print("Python")
    print("Java")
    print("C++")
    print("#" * 10)
print(func)           # принтке салып койсо функциянын адресин корсотуп коет

def func():
    print("Python")
    print("Java")
    print("C++")
    print("#" * 10)

f = func
f()

def func():
    print("Python")
    print("Java")
    print("C++")
    print("#" * 10)

pr = print
pr("My name is Arsen")

def func():
    print("Python")
    print("Java")
    print("C++")
    print("#" * 10)

def area_circle():
    radius = float(input("Enter the radius: "))
    s = 3.14 * radius ** 2
    print("Аянт =", s)
area_circle()

def area_rectangle(width, height):
    area = width * height                      ##area_rectangle-иштеш учун 2 значения бериш керек
    print("Аянт =", area)

area_rectangle(100, 100)


def area_rectangle(width, height):
    if width < 0 or height < 0:
        print("Торт бурчтуктун жактары терс  сан болбойт")
    else:
        area = width * height
        print("Аянт =", area)

area_rectangle(10, 11)

def names (name):
    print(f"Your name is {name}")
names("Arsen")
names("Aida")
names("Aiana")


name = input("Enter your name: ")
names (name)



