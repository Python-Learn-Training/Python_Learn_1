#判斷式
x=input("Please input number : ") #取得字串
X=int(x) #將字串轉成數字
if X>200:
    print("X<200")
elif X>100:
    print("X>100 X<200")
else:
    print("X<= 100")