from fsm import TocMachine

def create_machine():
    machine = TocMachine(
        states =["user", "menu", "fsm", "ranking", "team_ranking", "player_ranking", "schedule", "preseason_schedule", "regular_season_schedule", "team_introduction",
                "Fubon", "Fubon_introduction", "Fubon_member_list",
                "Kings", "Kings_introduction", "Kings_member_list",
                "Pilots", "Pilots_introduction", "Pilots_member_list",
                "Lioneers", "Lioneers_introduction", "Lioneers_member_list",
                "Dreamers", "Dreamers_introduction", "Dreamers_member_list",
                "Steelers", "Steelers_introduction", "Steelers_member_list",
                "cancel"],
        transitions =[
            {
                "trigger": "advance",
                "source": "user",
                "dest": "menu",
                "conditions": "is_going_to_menu",
            },
            
            # forward
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "fsm",
                "conditions": "is_going_to_fsm",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "ranking",
                "conditions": "is_going_to_ranking",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "schedule",
                "conditions": "is_going_to_schedule",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "team_introduction",
                "conditions": "is_going_to_team_introduction",
            },
            
            # backward
            {
                "trigger": "advance",
                "source": "fsm",
                "dest": "menu",
                "conditions": "is_going_to_menu",
            },
            {
                "trigger": "advance",
                "source": "ranking",
                "dest": "menu",
                "conditions": "is_going_to_menu",
            },
            {
                "trigger": "advance",
                "source": "schedule",
                "dest": "menu",
                "conditions": "is_going_to_menu",
            },
            {
                "trigger": "advance",
                "source": "team_introduction",
                "dest": "menu",
                "conditions": "is_going_to_menu",
            },
            
            # forward    
            {
                "trigger": "advance",
                "source": "ranking",
                "dest": "team_ranking",
                "conditions": "is_going_to_team_ranking",
            },
            {
                "trigger": "advance",
                "source": "ranking",
                "dest": "player_ranking",
                "conditions": "is_going_to_player_ranking",
            },
            
            # backward
            {
                "trigger": "advance",
                "source": "team_ranking",
                "dest": "ranking",
                "conditions": "is_going_to_ranking",
            },
            {
                "trigger": "advance",
                "source": "player_ranking",
                "dest": "ranking",
                "conditions": "is_going_to_ranking",
            },
            
            # forward
            {
                "trigger": "advance",
                "source": "schedule",
                "dest": "preseason_schedule",
                "conditions": "is_going_to_preseason_schedule",
            },
            {
                "trigger": "advance",
                "source": "schedule",
                "dest": "regular_season_schedule",
                "conditions": "is_going_to_regular_season_schedule",
            },
            
            
            # backward
            {
                "trigger": "advance",
                "source": "preseason_schedule",
                "dest": "schedule",
                "conditions": "is_going_to_schedule",
            },
            {
                "trigger": "advance",
                "source": "regular_season_schedule",
                "dest": "schedule",
                "conditions": "is_going_to_schedule",
            },
            
            
            # fubon
            {
                "trigger": "advance",
                "source": "team_introduction",
                "dest": "Fubon",
                "conditions": "is_going_to_Fubon",
            },
            {
                "trigger": "advance",
                "source": "Fubon",
                "dest": "team_introduction",
                "conditions": "is_going_to_team_introduction",
            },
            
            # Kings
            {
                "trigger": "advance",
                "source": "team_introduction",
                "dest": "Kings",
                "conditions": "is_going_to_Kings",
            },
            {
                "trigger": "advance",
                "source": "Kings",
                "dest": "team_introduction",
                "conditions": "is_going_to_team_introduction",
            },
            
            # Pilots
            {
                "trigger": "advance",
                "source": "team_introduction",
                "dest": "Pilots",
                "conditions": "is_going_to_Pilots",
            },
            {
                "trigger": "advance",
                "source": "Pilots",
                "dest": "team_introduction",
                "conditions": "is_going_to_team_introduction",
            },
            
            # Lioneers
            {
                "trigger": "advance",
                "source": "team_introduction",
                "dest": "Lioneers",
                "conditions": "is_going_to_Lioneers",
            },
            {
                "trigger": "advance",
                "source": "Lioneers",
                "dest": "team_introduction",
                "conditions": "is_going_to_team_introduction",
            },
            
            # Dreamers
            {
                "trigger": "advance",
                "source": "team_introduction",
                "dest": "Dreamers",
                "conditions": "is_going_to_Dreamers",
            },
            {
                "trigger": "advance",
                "source": "Dreamers",
                "dest": "team_introduction",
                "conditions": "is_going_to_team_introduction",
            },
            
            # Steelers
            {
                "trigger": "advance",
                "source": "team_introduction",
                "dest": "Steelers",
                "conditions": "is_going_to_Steelers",
            },
            {
                "trigger": "advance",
                "source": "Steelers",
                "dest": "team_introduction",
                "conditions": "is_going_to_team_introduction",
            },
            
            # fubon(forward)
            {
                "trigger": "advance",
                "source": "Fubon",
                "dest": "Fubon_introduction",
                "conditions": "is_going_to_Fubon_introduction",
            },
            {
                "trigger": "advance",
                "source": "Fubon",
                "dest": "Fubon_member_list",
                "conditions": "is_going_to_Fubon_member_list",
            },
            
            
            # fubon(backward)
            {
                "trigger": "advance",
                "source": "Fubon_introduction",
                "dest": "Fubon",
                "conditions": "is_going_to_Fubon",
            },
            {
                "trigger": "advance",
                "source": "Fubon_member_list",
                "dest": "Fubon",
                "conditions": "is_going_to_Fubon",
            },
            
            
            # kings(forward)
            {
                "trigger": "advance",
                "source": "Kings",
                "dest": "Kings_introduction",
                "conditions": "is_going_to_Kings_introduction",
            },
            {
                "trigger": "advance",
                "source": "Kings",
                "dest": "Kings_member_list",
                "conditions": "is_going_to_Kings_member_list",
            },
            
            # kings(backward)
            {
                "trigger": "advance",
                "source": "Kings_introduction",
                "dest": "Kings",
                "conditions": "is_going_to_Kings",
            },
            {
                "trigger": "advance",
                "source": "Kings_member_list",
                "dest": "Kings",
                "conditions": "is_going_to_Kings",
            },
            
            
            # pilots(forward)
            {
                "trigger": "advance",
                "source": "Pilots",
                "dest": "Pilots_introduction",
                "conditions": "is_going_to_Pilots_introduction",
            },
            {
                "trigger": "advance",
                "source": "Pilots",
                "dest": "Pilots_member_list",
                "conditions": "is_going_to_Pilots_member_list",
            },
            
            # pilots(backward)
            {
                "trigger": "advance",
                "source": "Pilots_introduction",
                "dest": "Pilots",
                "conditions": "is_going_to_Pilots",
            },
            {
                "trigger": "advance",
                "source": "Pilots_member_list",
                "dest": "Pilots",
                "conditions": "is_going_to_Pilots",
            },
            
            
            # lioneers(forward)
            {
                "trigger": "advance",
                "source": "Lioneers",
                "dest": "Lioneers_introduction",
                "conditions": "is_going_to_Lioneers_introduction",
            },
            {
                "trigger": "advance",
                "source": "Lioneers",
                "dest": "Lioneers_member_list",
                "conditions": "is_going_to_Lioneers_member_list",
            },
            
            # lioneers(backward)
            {
                "trigger": "advance",
                "source": "Lioneers_introduction",
                "dest": "Lioneers",
                "conditions": "is_going_to_Lioneers",
            },
            {
                "trigger": "advance",
                "source": "Lioneers_member_list",
                "dest": "Lioneers",
                "conditions": "is_going_to_Lioneers",
            },
            
            
            # dreamers(forward)
            {
                "trigger": "advance",
                "source": "Dreamers",
                "dest": "Dreamers_introduction",
                "conditions": "is_going_to_Dreamers_introduction",
            },
            {
                "trigger": "advance",
                "source": "Dreamers",
                "dest": "Dreamers_member_list",
                "conditions": "is_going_to_Dreamers_member_list",
            },
            
            # dreamers(backward)
            {
                "trigger": "advance",
                "source": "Dreamers_introduction",
                "dest": "Dreamers",
                "conditions": "is_going_to_Dreamers",
            },
            {
                "trigger": "advance",
                "source": "Dreamers_member_list",
                "dest": "Dreamers",
                "conditions": "is_going_to_Dreamers",
            },
            
            
            # Steelers(forward)
            {
                "trigger": "advance",
                "source": "Steelers",
                "dest": "Steelers_introduction",
                "conditions": "is_going_to_Steelers_introduction",
            },
            {
                "trigger": "advance",
                "source": "Steelers",
                "dest": "Steelers_member_list",
                "conditions": "is_going_to_Steelers_member_list",
            },
            
            # Steelers(backward)
            {
                "trigger": "advance",
                "source": "Steelers_introduction",
                "dest": "Steelers",
                "conditions": "is_going_to_Steelers",
            },
            {
                "trigger": "advance",
                "source": "Steelers_member_list",
                "dest": "Steelers",
                "conditions": "is_going_to_Steelers",
            },
            
            # go to cancel
            {
                "trigger": "advance",
                "source": "fsm",
                "dest": "cancel",
                "conditions": "is_going_to_cancel",
            },
            {
                "trigger": "advance",
                "source": "team_ranking",
                "dest": "cancel",
                "conditions": "is_going_to_cancel",
            },
            {
                "trigger": "advance",
                "source": "player_ranking",
                "dest": "cancel",
                "conditions": "is_going_to_cancel",
            },
            {
                "trigger": "advance",
                "source": "preseason_schedule",
                "dest": "cancel",
                "conditions": "is_going_to_cancel",
            },
            {
                "trigger": "advance",
                "source": "regular_season_schedule",
                "dest": "cancel",
                "conditions": "is_going_to_cancel",
            },
            
            
            {
                "trigger": "advance",
                "source": "Fubon_introduction",
                "dest": "cancel",
                "conditions": "is_going_to_cancel",
            },
            {
                "trigger": "advance",
                "source": "Fubon_member_list",
                "dest": "cancel",
                "conditions": "is_going_to_cancel",
            },
            {
                "trigger": "advance",
                "source": "Kings_introduction",
                "dest": "cancel",
                "conditions": "is_going_to_cancel",
            },
            {
                "trigger": "advance",
                "source": "Kings_member_list",
                "dest": "cancel",
                "conditions": "is_going_to_cancel",
            },
            {
                "trigger": "advance",
                "source": "Pilots_introduction",
                "dest": "cancel",
                "conditions": "is_going_to_cancel",
            },
            {
                "trigger": "advance",
                "source": "Pilots_member_list",
                "dest": "cancel",
                "conditions": "is_going_to_cancel",
            },
            {
                "trigger": "advance",
                "source": "Lioneers_introduction",
                "dest": "cancel",
                "conditions": "is_going_to_cancel",
            },
            {
                "trigger": "advance",
                "source": "Lioneers_member_list",
                "dest": "cancel",
                "conditions": "is_going_to_cancel",
            },
            {
                "trigger": "advance",
                "source": "Dreamers_introduction",
                "dest": "cancel",
                "conditions": "is_going_to_cancel",
            },
            {
                "trigger": "advance",
                "source": "Dreamers_member_list",
                "dest": "cancel",
                "conditions": "is_going_to_cancel",
            },
            {
                "trigger": "advance",
                "source": "Steelers_introduction",
                "dest": "cancel",
                "conditions": "is_going_to_cancel",
            },
            {
                "trigger": "advance",
                "source": "Steelers_member_list",
                "dest": "cancel",
                "conditions": "is_going_to_cancel",
            },
            {"trigger": "go_back", "source": ["cancel"], "dest": "user"},
        ],
        initial = "user",
        auto_transitions = False,
        show_conditions =  True,
    )
    return machine
    