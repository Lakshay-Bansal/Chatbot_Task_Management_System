'''
Source: https://github.com/xtekky/gpt4free
'''
import g4f
import json

def create_new_user_calender(user_name):
    new_user_calender = {"Monday": {"am": [] , "pm": [] },
                    "Tuesday": {"am": [], "pm": []},
                    "Wednesday": {"am": [], "pm": []},
                    "Thursday": {"am": [], "pm": []},
                    "Friday": {"am": [], "pm": []},
                    "Saturday": {"am": [], "pm": []},
                    "Sunday": {"am": [], "pm": []}
                    }
    
    with open(f'./services/jsons/{user_name}_calender.json', 'w') as json_file:
        json.dump(new_user_calender, json_file)
    

user_calender = {"Monday": {"am": [{"1": "Meeting with VP"}, {"6": "Yoga lesson"}] , "pm": [{"2": "Lunch with team"}] },
                 "Tuesday": {"am": [], "pm": []},
                 "Wednesday": {"am": [], "pm": []},
                 "Thursday": {"am": [], "pm": []},
                 "Friday": {"am": [], "pm": []},
                 "Saturday": {"am": [], "pm": []},
                 "Sunday": {"am": [], "pm": []}
                 }




g4f.debug.logging = True # enable logging
g4f.check_version = False # Disable automatic version checking
print(g4f.version) # check version
print(g4f.Provider.Ails.params)  # supported args

def g4_response(web_chat_request):
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": f"{web_chat_request} Extract whether its a update, create or delete command for creating meeting. Also extract the day-time-meeeting name from the message in a formatday-time-meeeting."
                   }],
    )

    print("g4_response", response)