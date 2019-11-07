# 儲存檔案 mode="w"

# file = open("data.txt",mode="w",encoding="UTF-8") #開啟 encoding="編碼方式"
# file.write("Hello File \n Second Line\n測試中文") #操作寫入 \n換行
# file.close() #關閉

# with open("data.txt",mode="w",encoding="utf-8") as file:
#     file.write("測試中文")

# with open("data.txt",mode="w",encoding="utf-8") as file:
#     file.write("5\n3")

# 讀取檔案 mode="r"
# 把檔案中的數字資料，一行一行的讀取出來，並計算總合
# sum=0
# with open("data.txt",mode="r",encoding="utf-8") as file:
#     for line in file: # 一行一行的讀取出來
#         sum+=int(line) # 將讀出來的值轉成數字
# print(sum)

# 使用JSON格式讀取、複寫檔案
import json
# 從檔案中讀取JSON資料，放入變數data裡面
with open("config.json",mode="r") as file:
    data=json.load(file)
print(data) #data 是一個字典資料

# print("name: ",data["name"])
# print("version:",data["version"])

data["name"]="New Name" # 修改變數中的資料
#把最新的資料複寫回檔案中
with open("config.json",mode="w") as file:
     json.dump(data,file)