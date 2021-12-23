import urllib.request as req
import bs4
from tabulate import tabulate



# formosa taishin dreamers intro.
# url = "https://pleagueofficial.com/team/4#player_info"
# request = req.Request(url, headers = {
#     "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
# })
# with req.urlopen(request) as response:
#     data = response.read().decode("utf-8")
    

# root = bs4.BeautifulSoup(data, "html.parser")
# # print(root)

# team_intro = str()
# n = 0

# infos = root.find_all("table", class_ = "table mt-4 mb-5 team_intro")


# for i in infos:
#     text = str(i.text)
#     team_info = text[2 : 297]
# print(team_info)



# # formosa taishin dreamers members
# url = "https://pleagueofficial.com/team/4#player_info"
# request = req.Request(url, headers = {
#     "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
# })
# with req.urlopen(request) as response:
#     data = response.read().decode("utf-8")
    

# root = bs4.BeautifulSoup(data, "html.parser")
# # print(root)

# # formosa taishin dreamers crew member
# print("coach team / GM\n")
# titles = root.find_all("h3", class_ = "fs12 my-1 pt-2 text-black")

# names = root.find_all("p", class_ = "fs14 my-0 text-dark")

# crew_title_arr = []
# crew_name_arr = []

# for title in titles:
#     crew_title_arr.append(title.string)
    
# for name in names:
#     crew_name_arr.append(name.string)
    
# for i in range(len(crew_name_arr)):
#     print(crew_title_arr[i])
#     print(crew_name_arr[i])
#     print("\n")

# # formosa taishin dreamers player 
# print("player")
# player_infos = root.find_all("div", class_ = "MOBILE_only bg-light text-black mt-2")

# for info in player_infos:
#     print(info.text)