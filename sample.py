import random
def fun1():
    print("Hello Keshav")
fun2 = fun1
del fun1

def execute(fun):
    fun("Hello")


def captcha_required(fun):
    def exe():
        a = random.randint(1,99)
        b = random.randint(1,99)
        x = int(input("%s + %s : "%(a,b)))
        if x==a+b:
            fun()
        else:
            print("Invalid Captcha")
    return exe

@captcha_required
def run():
    print("Shi hai")

run()