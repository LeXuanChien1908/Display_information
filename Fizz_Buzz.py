dau_vao = input("Nhập vào đây 2 số:")

dau_vao_splited = dau_vao.split(" ")

start = int(dau_vao_splited[0])
end = int(dau_vao_splited[1])
print(start, end)

if (start > end):
    print("số kết thúc cần lớn hơn số bắt đầu!!")
else :
    for i in range(start, end+1):
        if (i%3 == 0 and i%5 == 0):
            print("FizzBuzz")
        elif (i%5 == 0):
            print("Buzz")
        elif (i%3 == 0):
            print("Fizz")
        else:
            print(i)
