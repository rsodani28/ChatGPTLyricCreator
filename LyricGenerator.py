import openai
from my_sk import my_sk
openai.api_key = my_sk
messages_list = [{"role":"system","content":"I am Lyric Generator. When given a lyric I will add more bars to it."},
                 {"role":"user","content":"Shoes on, get up in the morn'"},
                 {"role":"assistant","content":"Cup of milk, let's rock and roll"},
                 {"role":"user","content":"King Kong, kick the drum, rolling on like a Rolling Stone"},
                 {"role":"assistant","content":"Sing song when I'm walking home"},
                 {"role":"user","content":"Jump "},]
for i in range(4):

    chat_completion = openai.ChatCompletion.create(model = "gpt-3.5-turbo",
                                               messages = messages_list,
                                               n = 1,
                                               max_tokens = 20,
                                               temperature = 0)
    print(chat_completion.choices[0].message.content)
    new_message = {"role":"assistant","content": chat_completion.choices[0].message.content}
    messages_list.append(new_message)