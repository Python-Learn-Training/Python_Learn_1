# 安裝flask套件: pip install Flask
from flask import Flask
app=Flask(__name__) # __name__ 代表目前執行的模塊 ，建立app物件

@app.route("/") # 函式的裝飾 (Decorator): 以函式為基礎，提供附加的功能
def home():
    return "Hello!This is home page."

@app.route("/test") # 代表要處理的網站路徑
def test():
    return "This is Test Page."

@app.route("/Z.Y.Y") # 代表要處理的網站路徑
def zyy():
    return "How are you ?"

if __name__=="__main__": # 如果以主程式(__main__)執行
    app.run() # 立刻啟動伺服器