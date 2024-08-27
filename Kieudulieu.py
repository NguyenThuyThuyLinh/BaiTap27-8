# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:48:23 2024

@author: Student
"""

#Bài 1:
a=int(input("Nhap a:"))
b=int(input("Nhap b:"))
c=int(input("Nhap c:"))
d=int(input("Nhap d:"))
sum= (a+b+c+d)/4
print("TBC a,b,c,d la:", sum)

#Bài 2:
a=int(input("Nhap a:"))
b=int(input("Nhap b:"))
tong= a+b
hieu= a-b
tich=a*b
thuong= a/b
print("Tong a va b:", tong)
print("Hieu a va b:", hieu)
print("Tich a va b:", tich)
print("Thuong a và b:",round(thuong,2) )

#Bài 3:
a=int(input("Nhap a:"))
b=int(input("Nhap b:"))
nguyen=a//b
du=a%b
print("a chia b bằng:",nguyen )
print("a chia b  :",du)

#Bài 4:
N = int(input("Nhập số nguyên dương N gồm 2 chữ số: "))
if 10 <= N <= 99:
    print("Tổng các chữ số của N là:", (N // 10) + (N % 10))
else:
     print("Số nhập vào không phải là số nguyên dương có 2 chữ số.")

#Bai 5:
gio = int(input("Nhập số giờ: "))
phut = int(input("Nhập số phút: "))
giay = int(input("Nhập số giây: "))
tong_giay = gio * 3600 + phut * 60 + giay
print("Tổng số giây là: " , tong_giay)

#Bai 6:
a=int(input("Nhap tuoi cua ban:"))
b=2024-a
print("Tuoi cua ban nam 2024 la:", b)

#Bai 7:
import math
r = float(input("Nhập bán kính của hình tròn: "))
Cv = 2 * math.pi * r
Dt = math.pi * r * r
print("Chu vi hình tròn:", Cv)
print("Diện tích hình tròn:", Dt)

#Bài 8:
a=int(input(" Nhập cân nặng của bạn(kg):"))
b=int(input(" Nhập chiều cao của bạn(m):"))
BMI=a/(b*b)
print("Chi so BMI cua ban:", BMI)

#Bài 9:
print("MENU ")
print("1. Hu tieu")
print("2. Chao long")
print("3. Banh canh")
print("4. Bun rieu")
print("5. Pho bo")
choice = input("Moi nhap lua chon: ")

#Bai 10: 
a=int(input("Nhap a:"))
b=int(input("Nhap b:"))
c=int(input("Nhap c:"))
d=int(input("Nhap d:"))
print("Bien so xe cua ban:", str(a)+str(b)+str(c)+str(d))
soxe=a+b+c+d
nghin=soxe//1000
tram=soxe//100%10
chuc=soxe//10%10
donvi=soxe%10
e=nghin+tram+chuc+donvi
print("Bien so xe duoc:", e, "nut")

#Bai 11:
chu_thuong = input("Nhập vào một ký tự chữ thường: ")
chu_hoa = chu_thuong.upper()
print("Ký tự chữ hoa tương ứng là:", chu_hoa)

#Bai 12:
#a
import random
def random_number_in_range(start, end):
    return random.randint(start, end)
start = 0
end = 100
print(f"Số ngẫu nhiên trong đoạn [{start}, {end}]:", random_number_in_range(start, end))
#b
import random
def random_number_in_range(start, end):
    return random.randint(start, end)
start = 50
end = 99
print(f"Số ngẫu nhiên trong đoạn [{start}, {end}]:", random_number_in_range(start, end))
#c
import random
def random_number_in_range(start, end):
    return random.randint(start, end)
start = 39
end = 79
print(f"Số ngẫu nhiên trong đoạn [{start}, {end}]:", random_number_in_range(start, end))
#d
import random
def random_number_in_range(start, end):
    return random.randint(start, end)
start = -79
end = 39
print(f"Số ngẫu nhiên trong đoạn [{start}, {end}]:", random_number_in_range(start, end))

#Bai 13:
Ngay= input("Nhap ngay:")
Thang= input("Nhap thang:")
Nam= input("Nhap nam:")
print("a) {0}/{1}/{2}".format(Ngay,Thang,Nam))
print("c) {0}/{1}/{2}".format(Nam,Thang,Ngay))
print("b) {0}/{1}/{2}".format(Ngay,Thang,Nam[2:]))

#Bai 14:
import math
A = (32 **(0.2)) - ((1 / 64) **(-0.25)) + ((8 / 27) **(1 / 3))
A = round(A, 3)
print(f"Kết quả: {A}")

Bai 15:
import math







#Bai 16:
gio = int(input("Nhập số giờ: "))
phut = int(input("Nhập số phút: "))
giay = int(input("Nhập số giây: "))
tong_giay = gio * 3600 + phut * 60 + giay
print("Tổng số giây là: " , tong_giay)

#Bai 17:
a=int(input("Nhap a:"))
b=int(input("Nhap b:"))
c=int(input("Nhap c:"))
print("so lon nhat la:", max(a,b,c))
print("so nho nhat la:", min(a,b,c))


Bai 18:

    
    
    
    