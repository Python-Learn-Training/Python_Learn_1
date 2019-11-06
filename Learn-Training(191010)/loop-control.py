# break 強制結束迴圈
# n=0
# while n<5:
#     if n==3:
#         break
#     print("迴圈中 n =",n) #印出迴圈中的 n
#     n+=1
# print("最後 n= :",n) #印出迴圈結束後的 n

# continue 範例 
# n=0
# for x in [0,1,2,3]:
#     if x%2==0: #X是偶數
#         continue
#     print("迴圈中 x =",x)
#     n+=1
# print("最後 n= :",n)

# else 範例
# sum=0
# for n in range(11):
#     sum+=n
# else:
#     print(sum) #印出 0+1+2...+10的結果

# 綜合範例: 找出整數平方根
# 輸入9 得到3
# 輸入11 得到 [沒有] 整數的平方根
n=input("input number(輸入正整數):")
n=int(n) #轉換輸入成數字
for i in range(n): # i 從 0 ~ n-1
    if i*i==n:
        print("整數平方根",i)
        break #用break 強制結束迴圈時，不會執行else 區塊
else:
        print("[沒有] 整數平方根")
