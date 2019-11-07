# Point 實體物件的設計: 平面座標上的點
# class Point:
#     def __init__(self,x,y): # 初始化參數
#         self.x=x
#         self.y=y
# # 建立第一個實體物件
# p1=Point(3,4) # 建立
# print(p1.x,p1.y) # 使用
# # 建立第二個實體物件
# p2=Point(5,6)
# print(p2.x,p2.y)

###########################################

# FullName 實體物件的設計:分開紀錄姓、名資料的全名
class FullName:
    def __init__(self,first,last):
        self.first=first
        self.last=last
name1=FullName("H.Y.","Chen")
print(name1.first,name1.last)
name2=FullName("Z.Y.","Yang")
print(name2.first,name2.last)