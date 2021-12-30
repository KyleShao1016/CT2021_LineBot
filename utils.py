import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage

import urllib.request as req
from bs4 import BeautifulSoup

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""


def scrape_preseason_schedule():
    url = "https://pleagueofficial.com/schedule-pre-season"
    request = req.Request(url, headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    root = BeautifulSoup(data, "html.parser")

    # stadium / game number / date / day_of_weak / time 
    stadiums = root.find_all("h5", class_= "fs12 mb-0")
    game_num = root.find_all("h5", class_= "fs14 mb-2")
    date = root.find_all("h5", class_= "fs16 mt-2 mb-1")
    day_of_weak = root.find_all("h5", class_= "fs12 mb-2")
    time = root.find_all("h6", class_= "fs12")
    teams = root.find_all("h6", class_= "fs12 mb-2 PC_only") 
    scores = root.find_all("h6", class_ = "PC_only ff8bit fs20")

    stadiums_arr = []
    game_num_arr = []
    date_arr = []
    day_of_weak_arr = []
    time_arr = []
    team_arr = []
    score_arr = []

    for stadium in stadiums:
        stadiums_arr.append(stadium.string)
        
    for num in game_num:
        game_num_arr.append(num.string)
        
    for d in date:
        date_arr.append(d.string)
        
    for day in day_of_weak:
        day_of_weak_arr.append(day.string)
        
    for t in time:
        if t.string:
            time_arr.append(t.string)
        
    for team in teams:
        text = str(team.text)
        n = 0
        for i, char in enumerate(text):
            if char == '\n':
                n += 1
                if n == 1:
                    front = i + 1
                elif n == 2:
                    end = i - 1
        mid = (front + end) // 2
        text = text[:mid + 1] + text[end + 1:]
        team_arr.append(text)

    for score in scores:
        score_arr.append(score.string)
            
    j = 0
    data = str()
    for i in range(len(stadiums_arr)):
        data += stadiums_arr[i] + ' ' + game_num_arr[i] + ' ' + date_arr[i] + ' ' + day_of_weak_arr[i] + ' ' + time_arr[i] + '\n'
        data += team_arr[j] + score_arr[j] + '\n'
        data += team_arr[j + 1] + score_arr[j + 1] + '\n'
        data += '----------------------------------\n'
        j += 2
        
    return data
        
        
def scrape_regular_season_schedule():
    url = "https://pleagueofficial.com/schedule-regular-season"
    request = req.Request(url, headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
            

    root = BeautifulSoup(data, "html.parser")
    # print(root)

    # stadium / game number / date / day_of_weak / time 
    stadiums = root.find_all("h5", class_= "fs12 mb-0")
    game_num = root.find_all("h5", class_= "fs14 mb-2")
    date = root.find_all("h5", class_= "fs16 mt-2 mb-1")
    day_of_weak = root.find_all("h5", class_= "fs12 mb-2")
    time = root.find_all("h6", class_= "fs12")
    teams = root.find_all("h6", class_= "fs12 mb-2 PC_only") 
    scores_right = root.find_all("h6", class_ = "MOBILE_only fs12 ff8bit")
    scores_left = root.find_all("h6", class_ = "MOBILE_only ff8bit fs12 text-left")


    stadiums_arr = []
    game_num_arr = []
    date_arr = []
    day_of_weak_arr = []
    time_arr = []
    team_arr = []

    for stadium in stadiums:
        stadiums_arr.append(stadium.string)
            
    for num in game_num:
        game_num_arr.append(num.string)
        
    for d in date:
        date_arr.append(d.string)
            
    for day in day_of_weak:
        day_of_weak_arr.append(day.string)
            
    for t in time:
        if t.string:
            time_arr.append(t.string)
            
    for team in teams:
        text = str(team.text)
        n = 0
        for i, char in enumerate(text):
            if char == '\n':
                n += 1
                if n == 1:
                    front = i + 1
                elif n == 2:
                    end = i - 1
        mid = (front + end) // 2
        text = text[:mid + 1] + text[end + 1:]
        team_arr.append(text)

    score_arr = [''] * (len(stadiums_arr) * 2)
    i = 0
    for score in scores_right:
        score_arr[i] = score.string
        i += 2

    i = 1
    for score in scores_left:
        score_arr[i] = score.string
        i += 2
    print(score_arr)
                
                
    j = 0 
    data = str()
    for i in range(len(stadiums_arr)):
        data += stadiums_arr[i] + ' ' + game_num_arr[i] + ' ' + date_arr[i] + ' ' + day_of_weak_arr[i] + ' ' + time_arr[i] + '\n'
        data += team_arr[j] + score_arr[j] + '\n'
        data += team_arr[j + 1] + score_arr[j + 1] + '\n'
        data += '----------------------------------\n'
        j += 2
            
    return data
        
def scrape_team_ranking():
    url = "https://pleagueofficial.com/standings"
    request = req.Request(url, headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
        

    root = BeautifulSoup(data, "html.parser")
    # print(root)

    infos = root.find_all("tr", class_= "bg-deepgray text-light")
    ranking_info_arr = []


    for info in infos:
        text = str(info.text)
        ranking_info_arr.append(text.strip().split('\n'))

    res = ''
    res += ('{} {:>2} {:>3} {}'.format('排名', '隊伍', '勝W', '敗L')) + '\n'

    for ele in ranking_info_arr:
        if ele[1] == '新北國王':
            ele[1] = '國王'
        elif ele[1] == '新竹街口攻城獅':
            ele[1] = '攻城獅'
        elif ele[1] == '臺北富邦勇士':
            ele[1] = '勇士'
        elif ele[1] == '福爾摩沙台新夢想家':
            ele[1] = '夢想家'
        elif ele[1] == '高雄鋼鐵人':
            ele[1] = '鋼鐵人'
        else:
            ele[1] = '領航猿'
        del ele[2]
        del ele[4:]
        if len(ele[1]) == 2:
            res += ('{} {:>8} {:>5} {:>6}'.format(ele[0], ele[1], ele[2], ele[3])) + '\n'
        else:
            res += ('{} {:>8} {:>2} {:>6}'.format(ele[0], ele[1], ele[2], ele[3])) + '\n'
            
    return res
    
def scrape_player_ranking():
    url = "https://pleagueofficial.com/stat-ranking/2021-22"
    request = req.Request(url, headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
        
    root = BeautifulSoup(data, "html.parser")
    # print(root)

    labels = []

    infos = root.find_all("tr", class_= "fs12")
    for i in infos:
        lab = str(i.text)
        labels.append(lab[1:])

    player_stat_arr = []

    infos = root.find_all("tr", "dark_gradient")

    for info in infos:
        text = str(info.text)
        player_stat_arr.append(text.strip().split('\n'))
            
    for stat in player_stat_arr:
        for i, c in enumerate(stat[1]):
            if c == '臺' or c == '新' or c == '福' or c == '桃' or c == '高':
                stat[1] = stat[1][:i] + '(' + stat[1][i:] +')'
                if stat[1][i+1 : len(stat[1])-1] == '臺北富邦勇士':
                    stat[1] = stat[1][:i] + '(勇士)'
                elif stat[1][i+1 : len(stat[1])-1] == '桃園領航猿':
                    stat[1] = stat[1][:i] + '(領航猿)'
                elif stat[1][i+1 : len(stat[1])-1] == '新竹街口攻城獅':
                    stat[1] = stat[1][:i] + '(攻城獅)'
                elif stat[1][i+1 : len(stat[1])-1] == '福爾摩沙台新夢想家':
                    stat[1] = stat[1][:i] + '(夢想家)'
                elif stat[1][i+1 : len(stat[1])-1] == '高雄鋼鐵人':
                    stat[1] = stat[1][:i] + '(鋼鐵人)'
                else:
                    stat[1] = stat[1][:i] + '(國王)'
                break
            
    res = ''    

    for i in range(1, 9):
        res += ("{} {:>8} {:>3}".format('排名', '球員(所屬球隊)', labels[i - 1]))
        for j in range(3):
            rank, player, stat = player_stat_arr[(i - 1) * 10 + j]
            res += ("{} {:>14} {:>6}".format(rank, player, stat)) + '\n'
        res += '\n'
        
    return res
    
         
def scrape_fubon_team_intro():
    url = "https://pleagueofficial.com/team/1#player_info"
    request = req.Request(url, headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
        

    root = BeautifulSoup(data, "html.parser")
    # print(root)

    team_intro = str()
    n = 0

    infos = root.find_all("table", class_ = "table mt-4 mb-5 team_intro")


    for i in infos:
        text = str(i.text)
        team_info = text[2 : 547]
    
    return team_info
    
def scrape_fubon_member_list():
    url = "https://pleagueofficial.com/team/1#player_info"
    request = req.Request(url, headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
        

    root = BeautifulSoup(data, "html.parser")
    # print(root)

    # fubon crew member
    s = str()

    s += 'coach team / GM\n'

    titles = root.find_all("h3", class_ = "fs12 my-1 pt-2 text-black")

    names = root.find_all("p", class_ = "fs14 my-0 text-dark")

    crew_title_arr = []
    crew_name_arr = []

    for title in titles:
        crew_title_arr.append(title.string)
        
    for name in names:
        crew_name_arr.append(name.string)
        
    for i in range(len(crew_name_arr)):
        s += crew_title_arr[i] + '\n'
        s += crew_name_arr[i] + '\n'
        s += '\n'

    s += '\n'
    #fubon player 
    s += 'player'
    player_infos = root.find_all("div", class_ = "MOBILE_only bg-light text-black mt-2")

    for info in player_infos:
        s += info.text + '\n'
        
    return s
                
def scrape_kings_team_intro():
    url = "https://pleagueofficial.com/team/6#player_info"
    request = req.Request(url, headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
        

    root = BeautifulSoup(data, "html.parser")
    # print(root)

    team_intro = str()
    n = 0

    infos = root.find_all("table", class_ = "table mt-4 mb-5 team_intro")


    for i in infos:
        text = str(i.text)
        team_info = text[2 : 496]
        
    return team_info
    
def scrape_kings_member_list():
    url = "https://pleagueofficial.com/team/6#player_info"
    request = req.Request(url, headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
        

    root = BeautifulSoup(data, "html.parser")
    # print(root)

    # kings crew member
    s = str()

    s += 'coach team / GM\n'

    titles = root.find_all("h3", class_ = "fs12 my-1 pt-2 text-black")

    names = root.find_all("p", class_ = "fs14 my-0 text-dark")

    crew_title_arr = []
    crew_name_arr = []

    for title in titles:
        crew_title_arr.append(title.string)
        
    for name in names:
        crew_name_arr.append(name.string)
        
    for i in range(len(crew_name_arr)):
        s += crew_title_arr[i] + '\n'
        s += crew_name_arr[i] + '\n'
        s += '\n'

    s += '\n'
    #fubon player 
    s += 'player'
    player_infos = root.find_all("div", class_ = "MOBILE_only bg-light text-black mt-2")

    for info in player_infos:
        s += info.text + '\n'
        
    return s
        
def scrape_pilots_team_intro():
    url = "https://pleagueofficial.com/team/2#player_info"
    request = req.Request(url, headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
        

    root = BeautifulSoup(data, "html.parser")
    # print(root)

    team_intro = str()
    n = 0

    infos = root.find_all("table", class_ = "table mt-4 mb-5 team_intro")


    for i in infos:
        text = str(i.text)
        team_info = text[2 : 720]
        
    return team_info
    
def scrape_pilots_member_list():
    url = "https://pleagueofficial.com/team/2#player_info"
    request = req.Request(url, headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
        

    root = BeautifulSoup(data, "html.parser")
    # print(root)

    # pilots crew member
    s = str()

    s += 'coach team / GM\n'

    titles = root.find_all("h3", class_ = "fs12 my-1 pt-2 text-black")

    names = root.find_all("p", class_ = "fs14 my-0 text-dark")

    crew_title_arr = []
    crew_name_arr = []

    for title in titles:
        crew_title_arr.append(title.string)
        
    for name in names:
        crew_name_arr.append(name.string)
        
    for i in range(len(crew_name_arr)):
        s += crew_title_arr[i] + '\n'
        s += crew_name_arr[i] + '\n'
        s += '\n'

    s += '\n'
    #fubon player 
    s += 'player'
    player_infos = root.find_all("div", class_ = "MOBILE_only bg-light text-black mt-2")

    for info in player_infos:
        s += info.text + '\n'
        
    return s

def scrape_lioneers_team_intro():
    url = "https://pleagueofficial.com/team/3#player_info"
    request = req.Request(url, headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
        

    root = BeautifulSoup(data, "html.parser")
    # print(root)

    team_intro = str()
    n = 0

    infos = root.find_all("table", class_ = "table mt-4 mb-5 team_intro")


    for i in infos:
        text = str(i.text)
        team_info = text[2 : 436]
        
    return team_info

def scrape_lioneers_member_list():
    url = "https://pleagueofficial.com/team/3#player_info"
    request = req.Request(url, headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
        

    root = BeautifulSoup(data, "html.parser")
    # print(root)

    # lioneers crew member
    s = str()

    s += 'coach team / GM\n'

    titles = root.find_all("h3", class_ = "fs12 my-1 pt-2 text-black")

    names = root.find_all("p", class_ = "fs14 my-0 text-dark")

    crew_title_arr = []
    crew_name_arr = []

    for title in titles:
        crew_title_arr.append(title.string)
        
    for name in names:
        crew_name_arr.append(name.string)
        
    for i in range(len(crew_name_arr)):
        s += crew_title_arr[i] + '\n'
        s += crew_name_arr[i] + '\n'
        s += '\n'

    s += '\n'
    #fubon player 
    s += 'player'
    player_infos = root.find_all("div", class_ = "MOBILE_only bg-light text-black mt-2")

    for info in player_infos:
        s += info.text + '\n'
        
    return s
        
def scrape_dreamers_team_intro():
    url = "https://pleagueofficial.com/team/4#player_info"
    request = req.Request(url, headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
        

    root = BeautifulSoup(data, "html.parser")
    # print(root)

    team_intro = str()
    n = 0

    infos = root.find_all("table", class_ = "table mt-4 mb-5 team_intro")


    for i in infos:
        text = str(i.text)
        team_info = text[2 : 408]
    
    return team_info 
    
def scrape_dreamers_member_list():
    url = "https://pleagueofficial.com/team/4#player_info"
    request = req.Request(url, headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
        

    root = BeautifulSoup(data, "html.parser")
    # print(root)

    # formosa taishin dreamers crew member
    s = str()

    s += 'coach team / GM\n'

    titles = root.find_all("h3", class_ = "fs12 my-1 pt-2 text-black")

    names = root.find_all("p", class_ = "fs14 my-0 text-dark")

    crew_title_arr = []
    crew_name_arr = []

    for title in titles:
        crew_title_arr.append(title.string)
        
    for name in names:
        crew_name_arr.append(name.string)
        
    for i in range(len(crew_name_arr)):
        s += crew_title_arr[i] + '\n'
        s += crew_name_arr[i] + '\n'
        s += '\n'

    s += '\n'
    #fubon player 
    s += 'player'
    player_infos = root.find_all("div", class_ = "MOBILE_only bg-light text-black mt-2")

    for info in player_infos:
        s += info.text + '\n'
        
    return s
        
def scrape_steelers_team_intro():
    url = "https://pleagueofficial.com/team/5#player_info"
    request = req.Request(url, headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
        

    root = BeautifulSoup(data, "html.parser")
    # print(root)

    team_intro = str()
    n = 0

    infos = root.find_all("table", class_ = "table mt-4 mb-5 team_intro")


    for i in infos:
        text = str(i.text)
        team_info = text[2 : 324]
        
    return team_info
    
def scrape_steelers_member_list():
    url = "https://pleagueofficial.com/team/5#player_info"
    request = req.Request(url, headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
        

    root = BeautifulSoup(data, "html.parser")
    # print(root)

    # kaohsiung steelers crew member
    s = str()

    s += 'coach team / GM\n'

    titles = root.find_all("h3", class_ = "fs12 my-1 pt-2 text-black")

    names = root.find_all("p", class_ = "fs14 my-0 text-dark")

    crew_title_arr = []
    crew_name_arr = []

    for title in titles:
        crew_title_arr.append(title.string)
        
    for name in names:
        crew_name_arr.append(name.string)
        
    for i in range(len(crew_name_arr)):
        s += crew_title_arr[i] + '\n'
        s += crew_name_arr[i] + '\n'
        s += '\n'

    s += '\n'
    #fubon player 
    s += 'player'
    player_infos = root.find_all("div", class_ = "MOBILE_only bg-light text-black mt-2")

    for info in player_infos:
        s += info.text + '\n'
        
    return s
