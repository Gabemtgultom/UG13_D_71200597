# turtle menampilkan index 0 nama depan
import turtle
import random
import time

# input nama untuk mengambil huruf pertama nama depan dan belakang
nama = 'Gabe Maruli'
nama_depan = nama.split()[0]
nama_belakang = nama.split()[1]

# mengambil huruf pertama nama depan dan belakang
huruf_depan = nama_depan[0]
huruf_belakang = nama_belakang[0]
# tampilkan input nama
print(f'Nama: {nama} Huruf yang dipakai adalah {huruf_depan},{huruf_belakang}')

# mengambil 3 angka terakhir dari NIM yang diinput
nim = '71200597'
nim3a= nim[-3:]
nim1 = nim[-3]
nim2 = nim[-2]
nim3 = nim[-1]
# tampilkan input nim
print(f'NIM: {nim},Angka yang dipake adalah {nim3a}')

turtle.bgcolor("#7000FF")
turtle.color("#FFFFFF")

turtle.penup()
turtle.setx(-5)
turtle.sety(100)
turtle.write(huruf_depan,font=("calibri",50,"bold"))

turtle.setx(-10)
turtle.sety(-100)
turtle.write(huruf_belakang,font=("calibri",50,"bold"))

turtle.setx(-100)
turtle.sety(0)
turtle.write(nim1,font=("calibri",50,"bold"))

turtle.setx(0)
turtle.sety(0)
turtle.write(nim2,font=("calibri",50,"bold"))

turtle.setx(100)
turtle.sety(0)
turtle.write(nim3,font=("calibri",50,"bold"))

turtle.exitonclick()
