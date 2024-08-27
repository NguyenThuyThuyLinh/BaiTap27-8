# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:28:26 2024

@author: Nguyen Thuy Thuy Linh

#CAU TRUC RE NHANH
"""
#Bai 19:
so1 = int(input("Nhập số nguyên thứ nhất: "))
so2 = int(input("Nhập số nguyên thứ hai: "))
so3 = int(input("Nhập số nguyên thứ ba: "))
so4 = int(input("Nhập số nguyên thứ tư: "))
so_nho_nhat = so1
if so2 < so_nho_nhat:
    so_nho_nhat = so2
if so3 < so_nho_nhat:
    so_nho_nhat = so3
if so4 < so_nho_nhat:
    so_nho_nhat = so4
print("Số nho nhất trong bốn số là:", so_nho_nhat)

#Bai 20:
so1 = int(input("Nhập số nguyên thứ nhất: "))
so2 = int(input("Nhập số nguyên thứ hai: "))
so3 = int(input("Nhập số nguyên thứ ba: "))
so_lon_nhat = so1
if so2 > so_lon_nhat:
    so_lon_nhat = so2
if so3 > so_lon_nhat:
    so_lon_nhat = so3
print("Số lớn nhất trong ba số là:", so_lon_nhat)

#Bai 21:
so = int(input("Nhập một số nguyên: "))
if so == 0:
    print("không")
elif so == 1:
    print("một")
elif so == 2:
    print("hai")
elif so == 3:
    print("ba")
elif so == 4:
    print("bốn")
elif so == 5:
    print("năm")
elif so == 6:
    print("sáu")
elif so == 7:
    print("bảy")
elif so == 8:
    print("tám")
elif so == 9:
    print("chín")
else:
    print("không đọc được")

#Bai 22:
a = float(input("Nhap gia tri a:"))
b = float(input("Nhap gia tri b:"))
if a==0:
    if  b==0:
        print("Phuong trinh vo so nghiem")
    else:
        print("Phuong trinh vo nghiem")
else:
    x= -b/a
    print("Phuong trinh co nghiem la x:", x)

#BAi 23:
import math
a = float(input("Nhap gia tri a:"))
b = float(input("Nhap gia tri b:"))
c = float(input("Nhap gia tri c:"))
delta = b * b - 4 * a * c
if a!=0:
    if delta < 0:
        print("Phuong trinh vo nghiem")
    elif delta == 0:
        x = -b / (2 * a)
        print("Phuong trinh co 1 nghiem kep: x =", x)
    else:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print("Phuong trinh co hai nghiem la x1:", x1)
        print("Phuong trinh co hai nghiem la x2:", x2)
        
#Bai 24:
gio = int(input("Nhập giờ: "))
phut = int(input("Nhập phút: "))
giay = int(input("Nhập giây: "))
if 0 <= gio <= 23 and 0 <= phut <= 59 and 0 <= giay <= 59:
    print("Thời gian hợp lệ")
else:
    print("Thời gian không hợp lệ")      
#Bai 25:        
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        