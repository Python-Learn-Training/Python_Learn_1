# 安裝 pandas 套件： pip install pandas

# 載入 pandas 模組
import pandas as pd

###########################################

# 建立 Series (單維度)
data=pd.Series([20,10,15])
# 基本 Series 操作
# print(data)
# print("Max",data.max()) # 最大值
# print("Median",data.median()) # 中位數
# data=data*2
# print(data)
# data=data==20
# print(data)

###########################################

# 建立 DataFrame (雙維度)
data=pd.DataFrame({
    "name":["Fish","Eddie"],
    "sex":["F","M"],
    "salary":[60000,70000]
})
# 基本 DataFrame 操作
# print(data)

# 取得特定欄位
# print(data["name"])

# 取得特定的列
print(data)
print("====================")
print(data.iloc[0]) # 印出第一列