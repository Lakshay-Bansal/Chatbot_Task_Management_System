'''
Source: https://github.com/xtekky/gpt4free
'''
import g4f

g4f.debug.logging = True # enable logging
g4f.check_version = False # Disable automatic version checking
print(g4f.version) # check version
print(g4f.Provider.Ails.params)  # supported args

# Automatic selection of provider

# streamed completion
# response = g4f.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[{"role": "user", "content": "I have meeting on Monday at 2pm and Metting on tuesday at 3pm, Now I received a another meeting at 3pm what should I do. Provide that information to me in a day wise calendre format. Give me a data in Calendre = Monday: pm: [], am: [], Tuesday: pm: [], am: [], Similarly for other days}"}],
#     stream=True,
# )

# response = g4f.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[{"role": "user", "content": "Update a calendre with meeting on thursday at 4 am."}],
#     stream=True,
# )

# for message in response:
#     print(message, flush=True, end='')

# normal response
response = g4f.ChatCompletion.create(
    model=g4f.models.gpt_4,
    messages=[{"role": "user", "content": "Update my calendre as I have a meeting at 2 pm on MOnday"}],
)  # alternative model setting

print(response)