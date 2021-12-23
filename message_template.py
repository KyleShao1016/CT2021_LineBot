main_menu = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://www.timeshighereducation.com/sites/default/files/styles/the_breaking_news_image_style/public/Pictures/web/n/c/o/numbers_on_podium.jpg?itok=-nVlhkPx",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1.25:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "ranking",
              "text": "ranking"
            },
            "height": "md",
            "color": "#ff9900",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://cdn.pixabay.com/photo/2016/10/23/17/06/calendar-1763587_960_720.png",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1.25:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "schedule",
              "text": "schedule"
            },
            "height": "md",
            "color": "#ff6666",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://cdn.pixabay.com/photo/2013/07/12/15/41/basketball-150316_960_720.png",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1.25:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "team_introduction",
              "text": "team_introduction"
            },
            "height": "md",
            "color": "#ff66b3",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://www.researchgate.net/profile/Juerg-Froehlich-2/publication/258377383/figure/fig1/AS:650481118507008@1532098192020/Finite-state-machine-with-three-states-A-B-C-input-symbols-0-1-and-output-symbols.png",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1.25:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "fsm",
              "text": "fsm"
            },
            "height": "md",
            "color": "#b366ff",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    }
  ]
}

show_fsm = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "giga",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/zmofjcD.png",
        "aspectMode": "fit",
        "size": "full",
        "aspectRatio": "2:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Main Menu",
              "text": "start"
            },
            "height": "md",
            "color": "#00cc66",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    }
  ]
}

cancel_menu = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://cdn.pixabay.com/photo/2017/06/10/07/18/list-2389219_1280.png",
    "size": "full",
    "aspectMode": "fit",
    "aspectRatio": "1.25:1"
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "message",
          "label": "Return to the MainMenu",
          "text": "start"
        }
      }
    ]
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}

ranking_menu = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Choose team / players ranking",
            "weight": "bold",
            "align": "center",
            "size": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Team Ranking",
              "text": "team_ranking"
            },
            "height": "md",
            "color": "#00ff80",
            "style": "primary"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Players Ranking",
              "text": "player_ranking"
            },
            "height": "md",
            "color": "#00cc66",
            "style": "primary"
          },
        ],
        "spacing": "lg"
      }
    }
  ]
}

schedule_menu = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Choose regular / preseason schedule",
            "weight": "bold",
            "align": "center",
            "size": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Regular Season Schedule",
              "text": "regular_season_schedule"
            },
            "height": "md",
            "color": "#00ff80",
            "style": "primary"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Preseason Schedule",
              "text": "preseason_schedule"
            },
            "height": "md",
            "color": "#00cc66",
            "style": "primary"
          },
        ],
        "spacing": "lg"
      }
    }
  ]
}

teamintro_menu = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://upload.wikimedia.org/wikipedia/en/c/c8/Fubon_Braves_logo.png",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1.25:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Fubon",
              "text": "Fubon"
            },
            "height": "md",
            "color": "#ff9900",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/xFTkOBw.png",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1.25:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Kings",
              "text": "Kings"
            },
            "height": "md",
            "color": "#ff9900",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/6eEPzFh.png",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1.25:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Pilots",
              "text": "Pilots"
            },
            "height": "md",
            "color": "#ff9900",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/ehcqzOp.png",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1.25:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Lioneers",
              "text": "Lioneers"
            },
            "height": "md",
            "color": "#ff9900",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/nrF7kR5.png",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1.25:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Dreamers",
              "text": "Dreamers"
            },
            "height": "md",
            "color": "#ff9900",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/Qi1OAkV.png",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1.25:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Steelers",
              "text": "Steelers"
            },
            "height": "md",
            "color": "#ff9900",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    }
  ]
}

Fubon_menu = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Choose intro. / crew list",
            "weight": "bold",
            "align": "center",
            "size": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Fubon_introduction",
              "text": "Fubon_introduction"
            },
            "height": "md",
            "color": "#00ff80",
            "style": "primary"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Fubon_member_list",
              "text": "Fubon_member_list"
            },
            "height": "md",
            "color": "#00cc66",
            "style": "primary"
          },
        ],
        "spacing": "lg"
      }
    }
  ]
}


Kings_menu = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Choose intro. / crew list",
            "weight": "bold",
            "align": "center",
            "size": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Kings_introduction",
              "text": "Kings_introduction"
            },
            "height": "md",
            "color": "#00ff80",
            "style": "primary"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Kings_member_list",
              "text": "Kings_member_list"
            },
            "height": "md",
            "color": "#00cc66",
            "style": "primary"
          },
        ],
        "spacing": "lg"
      }
    }
  ]
}

Pilots_menu = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Choose intro. / crew list",
            "weight": "bold",
            "align": "center",
            "size": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Pilots_introduction",
              "text": "Pilots_introduction"
            },
            "height": "md",
            "color": "#00ff80",
            "style": "primary"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Pilots_member_list",
              "text": "Pilots_member_list"
            },
            "height": "md",
            "color": "#00cc66",
            "style": "primary"
          },
        ],
        "spacing": "lg"
      }
    }
  ]
}

Lioneers_menu = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Choose intro. / crew list",
            "weight": "bold",
            "align": "center",
            "size": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Lioneers_introduction",
              "text": "Lioneers_introduction"
            },
            "height": "md",
            "color": "#00ff80",
            "style": "primary"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Lioneers_member_list",
              "text": "Lioneers_member_list"
            },
            "height": "md",
            "color": "#00cc66",
            "style": "primary"
          },
        ],
        "spacing": "lg"
      }
    }
  ]
}

Dreamers_menu = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Choose intro. / crew list",
            "weight": "bold",
            "align": "center",
            "size": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Dreamers_introduction",
              "text": "Dreamers_introduction"
            },
            "height": "md",
            "color": "#00ff80",
            "style": "primary"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Dreamers_member_list",
              "text": "Dreamers_member_list"
            },
            "height": "md",
            "color": "#00cc66",
            "style": "primary"
          },
        ],
        "spacing": "lg"
      }
    }
  ]
}

Steelers_menu = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Choose intro. / crew list",
            "weight": "bold",
            "align": "center",
            "size": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Steelers_introduction",
              "text": "Steelers_introduction"
            },
            "height": "md",
            "color": "#00ff80",
            "style": "primary"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Steelers_member_list",
              "text": "Steelers_member_list"
            },
            "height": "md",
            "color": "#00cc66",
            "style": "primary"
          },
        ],
        "spacing": "lg"
      }
    }
  ]
}
