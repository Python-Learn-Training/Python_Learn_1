# 第一支程式 
# 190804 副檔名用.py
# 執行程式: python 檔案名稱.py
# 清空終端機的資料：cls
print ("Hello Python")

#data: 程式基本單位
#有順序、可變動列表 List
[3,4,5]
["Hello","World"]
#有順序、不可變動列表 Tuple
(3,4,5)
("Hello","World")
#集合 Set
{3,4,5}
{"Hello","World"}
#字典 Dictionary {"鍵1":"值1","鍵2":"值2"}
{"banana":"香蕉","data":"資料"}

#變數: 用來儲存資料的自訂名稱
#變數名稱=資料
x=3
data=4
#print(資料)
print(x)

x=True #取代舊資料 X變true
print(x)

#有序可變動列表 List
#印出所有列表
grades =[60,80,90,70]
print(grades)
#印出指定欄位的列表值 grades[欄位]
grades =[60,80,90,70]
print(grades[3])
#印出所有列表 grades[欄位]=更新值
grades =[60,80,90,70]
grades[0]=55
print(grades)
#取列表中特定的值 grades[欄位:欄位]
grades =[60,80,90,70]
print(grades[1:3]) #取出列表中從編號1到編號3(不包括編號3)的資料
#刪除列表中特定的值 grades[欄位:欄位]
grades =[60,80,90,70]
grades[1:3]=[] #連續刪除列表中從編號1到編號3(不包括編號3)的資料
print(grades)
#原來列表加新的列表 grades=grades+[新列表]
grades =[60,80,90,70]
grades=grades+[11,33]
print(grades)
#印出列表長度 len
grades =[60,80,90,70]
length=len(grades)
print(length)
#巢狀列表
data=[ [3,4,5], [6,7,8] ]
print(data[0][0]) #data[第一層][第一層的第一個(3)列表]
#資料取代
data=[ [3,4,5], [6,7,8] ]
print(data)
data[0][0:2]=[8,8,8]
print(data)
