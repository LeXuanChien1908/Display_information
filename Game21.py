import random

sum = 0
while (sum <= 21):
    if (sum == 0):
        r = random.randint(0,1)
        if (r == 0):
            current_player = "human"
        else:
            current_player = "computer"
    if(current_player == "computer"):
        value = random.randint(1,3)
        print("Máy tính chọn:", value)
        current_player = "human"
    else:
       value = int(input("Người chơi nhập số muốn chọn:"))
       while (value < 1 and value < 3):
           print("số bạn vừa nhập không thuộc 1,3")
           value = int(input("Nhập lại số muốn chọn:")
       current_player = "computer"
    sum += value
    print("Tổng hiện tại là :", sum)
print("Kết thúc trò chơi")
if (current_player == "human"):
    winner = "human"
else:
    winner = "computer"
print("người thắng cuộc là :", winner)   
     
            