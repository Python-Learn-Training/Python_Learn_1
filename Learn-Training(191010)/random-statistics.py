# 隨機模組
import random

###########################################

# 隨機選取 choice&sample
# data=random.choice([1,4,6,10,20]) #隨機選取
# data=random.sample([1,4,6,10,20],3) #隨機選取3筆
# print(data)

###########################################

# 隨機調換順序(洗牌) shuffle
# data=[1,5,6,10]
# random.shuffle(data)
# print(data)

###########################################

# 隨機取得亂數 random&uniform
# data=random.random() #0 ~ 1之間的隨機亂數
# data=random.uniform(0.0 ,1.0) #0.0 ~ 1.0 之間的隨機亂數 代表0.0~1.0之間的數字出現是相等的
# data=random.uniform(60 ,100)
# print(data)

###########################################

# 取得常態分配亂數 normalvariate
# 平均數100 , 標準差10 , 得到的資料 [多數] 在90 ~ 110之間
# data=random.normalvariate(100,10)
# print(data)

# 平均數0 , 標準差5 , 得到的資料 [多數] 在 -5 ~ 5之間
# data=random.normalvariate(0,5)
# print(data)

###########################################

# 統計模組 statistics
import statistics as stat
# data=stat.median([1,2,3,4,5,4,100]) #中位數 median
data=stat.stdev([1,2,3,4,5,4,100]) #標準差 stdev
print(data)