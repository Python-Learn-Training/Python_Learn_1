# 抓取 PTT電影版的網頁原始碼(HTML)
import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"
# 建立一個 Request 物件，附加 Request Headers 的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")


###########################################

# 解析原始碼(HTML)，取得每篇文章的標題
# 安裝pip beautifulsoup4 指令:pip install beautifulsoup4
import bs4
root=bs4.BeautifulSoup(data, "html.parser") # 讓 BeautifulSoup 協助解析HTML格式文件
# print(root.title.string)
titles=root.find_all("div", class_="title") # 尋找 class="title" 的 div 標籤
for title in titles:
    if title.a != None: # 如果標題包含 a 標籤(沒有刪除)，就印出來
        print(titles.a.string)