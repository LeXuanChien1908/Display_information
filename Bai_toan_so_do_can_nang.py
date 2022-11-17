a = float(input("Nhập cân nậng của bạn: "))
b = float(input("Nhập chiều cao của bạn: "))
c = a/(b*b)
print("Chỉ số BMI của bạn là: "+str(round(c,1)))
print('Phân loại: ',end="")
if c<18.5:
       print("Gày")
elif c<=24.9:
       print("Bình thường")
elif c<=29.9:
       print("Hơi béo")
elif c<=34.9:
       print("Béo phì cấp độ 1")
elif c<=39.9:
       print("Béo phì cấp độ 2")
else:
       print("Béo phì cấp độ 3")