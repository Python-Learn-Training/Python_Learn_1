# 網路連線
# import urllib.request as request
# src="https://www.ntu.edu.tw/"
# with request.urlopen(src) as response:
#     data=response.read().decode("utf-8") # 取得網站的原始碼(HTML、CSS、JS)
# print(data)

###########################################

# 串接、擷取公開資料
import urllib.request as request
import json
src="https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=296acfa2-5d93-4706-ad58-e83cc951863c" # 網路連線
with request.urlopen(src) as response:
    data=json.load(response) # 利用json模組處理jsaon資料格式
# print(data)
# 將公司名稱列表出來
clist=data["result"]["results"] # 列表
# print(clist)
with open("data.txt",mode="w",encoding="utf-8") as file: # 將公司名稱抓出來後寫入data.txt檔
    for company in clist:
        file.write(company["公司名稱"]+"\n")