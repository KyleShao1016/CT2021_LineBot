from future import utils
from transitions.extensions import GraphMachine

import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage

from utils import send_text_message

from utils import send_text_message
import utils
import message_template

load_dotenv()

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "start"

    def is_going_to_fsm(self, event):
        text = event.message.text
        return text.lower() == "fsm"
    
    def is_going_to_ranking(self, event):
        text = event.message.text
        return text.lower() == "ranking"
    
    def is_going_to_schedule(self, event):
        text = event.message.text
        return text.lower() == "schedule"
    
    def is_going_to_team_introduction(self, event):
        text = event.message.text
        return text.lower() == "team_introduction"
    
    def is_going_to_cancel(self, event):
        text = event.message.text
        return text.lower() == "cancel"
    
    def is_going_to_team_ranking(self, event):
        text = event.message.text
        return text.lower() == "team_ranking"
    
    def is_going_to_player_ranking(self, event):
        text = event.message.text
        return text.lower() == "player_ranking"
    
    def is_going_to_preseason_schedule(self, event):
        text = event.message.text
        return text.lower() == "preseason_schedule"

    def is_going_to_regular_season_schedule(self, event):
        text = event.message.text
        return text.lower() == "regular_season_schedule"
    
    def is_going_to_Fubon(self, event):
        text = event.message.text
        return text.lower() == "fubon"
    
    def is_going_to_Fubon_introduction(self, event):
        text = event.message.text
        return text.lower() == "fubon_introduction"
    
    def is_going_to_Fubon_member_list(self, event):
        text = event.message.text
        return text.lower() == "fubon_member_list"
    
    def is_going_to_Kings(self, event):
        text = event.message.text
        return text.lower() == "kings"
    
    def is_going_to_Kings_introduction(self, event):
        text = event.message.text
        return text.lower() == "kings_introduction"
    
    def is_going_to_Kings_member_list(self, event):
        text = event.message.text
        return text.lower() == "kings_member_list"

    def is_going_to_Pilots(self, event):
        text = event.message.text
        return text.lower() == "pilots"
    
    def is_going_to_Pilots_introduction(self, event):
        text = event.message.text
        return text.lower() == "pilots_introduction"
    
    def is_going_to_Pilots_member_list(self, event):
        text = event.message.text
        return text.lower() == "pilots_member_list"
    
    def is_going_to_Lioneers(self, event):
        text = event.message.text
        return text.lower() == "lioneers"
    
    def is_going_to_Lioneers_introduction(self, event):
        text = event.message.text
        return text.lower() == "lioneers_introduction"
    
    def is_going_to_Lioneers_member_list(self, event):
        text = event.message.text
        return text.lower() == "lioneers_member_list"
    
    def is_going_to_Dreamers(self, event):
        text = event.message.text
        return text.lower() == "dreamers"
    
    def is_going_to_Dreamers_introduction(self, event):
        text = event.message.text
        return text.lower() == "dreamers_introduction"
    
    def is_going_to_Dreamers_member_list(self, event):
        text = event.message.text
        return text.lower() == "dreamers_member_list"
    
    def is_going_to_Steelers(self, event):
        text = event.message.text
        return text.lower() == "steelers"
    
    def is_going_to_Steelers_introduction(self, event):
        text = event.message.text
        return text.lower() == "steelers_introduction"
    
    def is_going_to_Steelers_member_list(self, event):
        text = event.message.text
        return text.lower() == "steelers_member_list"
    
    
    def on_enter_menu(self, event):
        reply_token = event.reply_token
        message = message_template.main_menu
        message_to_reply = FlexSendMessage("start", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)
        
    def on_enter_cancel(self, event):
        reply_token = event.reply_token
        message = message_template.cancel_menu
        message_to_reply = FlexSendMessage("Finish and return to Main Menu", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)
        self.go_back()
        
        
    def on_enter_ranking(self, event):
        reply_token = event.reply_token
        message = message_template.ranking_menu
        message_to_reply = FlexSendMessage("Team / players ranking", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)
        
    def on_enter_fsm(self, event):
        reply_token = event.reply_token
        message = message_template.show_fsm
        message_to_reply = FlexSendMessage("Fsm", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)
        
    def on_enter_schedule(self, event):
        reply_token = event.reply_token
        message = message_template.schedule_menu
        message_to_reply = FlexSendMessage("Regular Season / Preseason Schedule", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)
        
    def on_enter_team_introduction(self, event):
        reply_token = event.reply_token
        message = message_template.teamintro_menu
        message_to_reply = FlexSendMessage("Team Introduction", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)
        
    def on_enter_team_ranking(self, event):
        userid = event.source.user_id
        team_ranking = utils.scrape_team_ranking()
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.push_message(userid, TextSendMessage(text = team_ranking))
        
    def on_enter_player_ranking(self, event):
        userid = event.source.user_id
        player_ranking = utils.scrape_player_ranking()
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.push_message(userid, TextSendMessage(text = player_ranking))
        
    def on_enter_preseason_schedule(self, event):
        userid = event.source.user_id
        data = utils.scrape_preseason_schedule()
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.push_message(userid, TextSendMessage(text = data))
        
    def on_enter_regular_season_schedule(self, event):
        userid = event.source.user_id
        data = utils.scrape_regular_season_schedule()
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.push_message(userid, TextSendMessage(text = data[:2000]))
        line_bot_api.push_message(userid, TextSendMessage(text = data[2000:4000]))
        line_bot_api.push_message(userid, TextSendMessage(text = data[4000:6000]))
        line_bot_api.push_message(userid, TextSendMessage(text = data[6000:8000]))
        line_bot_api.push_message(userid, TextSendMessage(text = data[8000:10000]))
        line_bot_api.push_message(userid, TextSendMessage(text = data[10000:12000]))
        
    def on_enter_Fubon(self, event):
        reply_token = event.reply_token
        message = message_template.Fubon_menu
        message_to_reply = FlexSendMessage("Fubon", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)
        
    def on_enter_Fubon_introduction(self, event):
        userid = event.source.user_id
        data = utils.scrape_fubon_team_intro()
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.push_message(userid, TextSendMessage(text = data))
        
    def on_enter_Fubon_member_list(self, event):
        userid = event.source.user_id
        data = utils.scrape_fubon_member_list()
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.push_message(userid, TextSendMessage(text = data))
        
    def on_enter_Kings(self, event):
        reply_token = event.reply_token
        message = message_template.Kings_menu
        message_to_reply = FlexSendMessage("Kings", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)
        
    def on_enter_Kings_introduction(self, event):
        userid = event.source.user_id
        data = utils.scrape_kings_team_intro()
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.push_message(userid, TextSendMessage(text = data))
        
    def on_enter_Kings_member_list(self, event):
        userid = event.source.user_id
        data = utils.scrape_kings_member_list()
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.push_message(userid, TextSendMessage(text = data))
        
    def on_enter_Pilots(self, event):
        reply_token = event.reply_token
        message = message_template.Pilots_menu
        message_to_reply = FlexSendMessage("Pilots", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)
        
    def on_enter_Pilots_introduction(self, event):
        userid = event.source.user_id
        data = utils.scrape_pilots_team_intro()
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.push_message(userid, TextSendMessage(text = data))
        
    def on_enter_Pilots_member_list(self, event):
        userid = event.source.user_id
        data = utils.scrape_pilots_member_list()
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.push_message(userid, TextSendMessage(text = data))
        
    def on_enter_Lioneers(self, event):
        reply_token = event.reply_token
        message = message_template.Lioneers_menu
        message_to_reply = FlexSendMessage("Lioneers", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)
        
    def on_enter_Lioneers_introduction(self, event):
        userid = event.source.user_id
        data = utils.scrape_lioneers_team_intro()
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.push_message(userid, TextSendMessage(text = data))
        
    def on_enter_Lioneers_member_list(self, event):
        userid = event.source.user_id
        data = utils.scrape_lioneers_member_list()
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.push_message(userid, TextSendMessage(text = data))
        
    def on_enter_Dreamers(self, event):
        reply_token = event.reply_token
        message = message_template.Dreamers_menu
        message_to_reply = FlexSendMessage("Dreamers", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)
        
    def on_enter_Dreamers_introduction(self, event):
        userid = event.source.user_id
        data = utils.scrape_dreamers_team_intro()
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.push_message(userid, TextSendMessage(text = data))
        
    def on_enter_Dreamers_member_list(self, event):
        userid = event.source.user_id
        data = utils.scrape_dreamers_member_list()
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.push_message(userid, TextSendMessage(text = data))
        
    def on_enter_Steelers(self, event):
        reply_token = event.reply_token
        message = message_template.Steelers_menu
        message_to_reply = FlexSendMessage("Steelers", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)
        
    def on_enter_Steelers_introduction(self, event):
        userid = event.source.user_id
        data = utils.scrape_steelers_team_intro()
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.push_message(userid, TextSendMessage(text = data))
        
    def on_enter_Steelers_member_list(self, event):
        userid = event.source.user_id
        data = utils.scrape_steelers_member_list()
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.push_message(userid, TextSendMessage(text = data))
        
    
    

