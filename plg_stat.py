import urllib.request as req
import bs4
from tabulate import tabulate
# # team ranking / stat. (例行賽戰績排行)
# url = "https://pleagueofficial.com/stat-ranking/2021-22"
# request = req.Request(url, headers = {
#     "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
# })
# with req.urlopen(request) as response:
#     data = response.read().decode("utf-8")
    

# root = bs4.BeautifulSoup(data, "html.parser")
# # print(root)

# infos = root.find_all("tr", class_= "bg-deepgray text-light")
# ranking_info_arr = []


# for info in infos:
#     text = str(info.text)
#     ranking_info_arr.append(text.strip().split('\n'))

# tabulate.PRESERVE_WHITESPACE = True
# print(tabulate(ranking_info_arr, headers=['排名', '隊伍', '已賽', '勝W', '敗L', '勝率', '勝差', '連勝連敗'], tablefmt = 'rst'))


# # player ranking / stat. (例行賽球員排行)
url = "https://pleagueofficial.com/stat-ranking/2021-22"
request = req.Request(url, headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
    

root = bs4.BeautifulSoup(data, "html.parser")
# print(root)

labels = []

infos = root.find_all("tr", class_= "fs12")
for i in infos:
    labels.append(i.text)

player_stat_arr = []

infos = root.find_all("tr", "dark_gradient")

for info in infos:
    text = str(info.text)
    player_stat_arr.append(text.strip().split('\n'))
    
# print(player_stat_arr)

for stat in player_stat_arr:
    for i, c in enumerate(stat[1]):
        if c == '臺' or c == '新' or c == '福' or c == '桃' or c == '高':
            stat[1] = stat[1][:i] + '(' + stat[1][i:] +')'
            break
        
s = str()
        

for i in range(1, 9):
    tabulate.PRESERVE_WHITESPACE = False
    s += tabulate(player_stat_arr[(i - 1) * 10:i * 10], headers=['排名', '球員(所屬球隊)', labels[i - 1]], tablefmt = 'rst')
    s += '\n'
    
print(s)

