
import turtle
import time
import random

# oyun ekranı oluşturma
oyunEkranı = turtle.Screen()
oyunEkranı.tracer(0)
oyunEkranı.setup(600, 600)
oyunEkranı.bgcolor("orange")
#yılanı oluşturma

yılan = turtle.Turtle()
yılan.shape("square")
yılan.color("white")
yılan.speed(0)
yılan.penup()
yılan.goto(-200, 0)
yılan.yön = "dur"

#yemi oluşturma
yem = turtle.Turtle()
yem.shape("square")
yem.color("black")
yem.speed(0)
yem.penup()
yem.goto(0, 0)
yem.yön = "dur"


def yukarı():
    if yılan.yön != "aşagı":
        yılan.yön = "yukarı"


def aşagı():
    if yılan.yön != "yukarı":
        yılan.yön = "aşagı"


def sağa():
    if yılan.yön != "sol":
        yılan.yön = "sağ"


def sola():
    if yılan.yön != "sağ":
        yılan.yön = "sol"

#yön tuşları tanımlama
oyunEkranı.listen()
oyunEkranı.onkeypress(yukarı, "w")
oyunEkranı.onkeypress(aşagı, "s")
oyunEkranı.onkeypress(sağa, "d")
oyunEkranı.onkeypress(sola, "a")

oyunEkranı.onkeypress(yukarı, "Up")
oyunEkranı.onkeypress(aşagı, "Down")
oyunEkranı.onkeypress(sağa, "Right")
oyunEkranı.onkeypress(sola, "Left")


def hareket_et():
    if yılan.yön == "yukarı":
        y = yılan.ycor()
        yılan.sety(y + 20)
    if yılan.yön == "aşagı":
        y = yılan.ycor()
        yılan.sety(y - 20)
    if yılan.yön == "sağ":
        x = yılan.xcor()
        yılan.setx(x + 20)
    if yılan.yön == "sol":
        x = yılan.xcor()
        yılan.setx(x - 20)


bölümler = []

while True:
    oyunEkranı.update()

    if yılan.xcor() > 290 or yılan.xcor() < -290 or yılan.ycor() > 290 or yılan.ycor() < -290:
        time.sleep(3)
        yılan.goto(-200, 0)
        yılan.yön = "dur"

        for i in bölümler:
            i.goto(2000, 2000)

        bölümler.clear()

    if yılan.distance(yem) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        yem.goto(x, y)

        yeniBölüm = turtle.Turtle()
        yeniBölüm.speed(0)
        yeniBölüm.shape("square")
        yeniBölüm.penup()
        yeniBölüm.color("white")
        bölümler.append(yeniBölüm)

    for i in range(len(bölümler) - 1, 0, -1):
        x = bölümler[i - 1].xcor()
        y = bölümler[i - 1].ycor()
        bölümler[i].goto(x, y)

    if len(bölümler) > 0:
        x = yılan.xcor()
        y = yılan.ycor()
        bölümler[0].goto(x, y)

    hareket_et()

    for i in bölümler:
        if i.distance(yılan) < 20:
            time.sleep(1)
            yılan.goto(-200, 0)
            yılan.yön = "dur"

            for i in bölümler:
                i.goto(2000, 2000)

            bölümler.clear()

    time.sleep(0.1)