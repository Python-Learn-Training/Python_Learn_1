#判斷式
#x=input("Please input number : ") #取得字串
#X=int(x) #將字串轉成數字
#if X>200:
#    print("X<200")
#elif X>100:
#    print("X>100 X<200")
#else:
#    print("X<= 100")

#四則運算
n1=int(input("Please input number :"))
n2=int(input("Please input number :"))
op=input("Please input : +, =, *, / :")
if op=="+":
    print("n1+n2 =" , n1+n2)
elif op=="-":
    print("n1-n2 =" , n1-n2)
elif op=="*":
    print("n1*n2 =" , n1*n2)
elif op=="/":
    print("n1/n2 =" , n1/n2)
else:
    print("error")