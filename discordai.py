from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
a=1
chatbot = ChatBot("Chatbot")
e="Uhh somethings wrong if you are seeing this"
trainer = ListTrainer(chatbot)
trainer.train([
   "Hello",
   "Hi",
   "How are you?",
   "Good you?",
   "Same",
   "Do you code?",
   "Yeah",
   "Thats cool",
   "What languages",
   "I like python and web. Wanna know a cool game im making?",
   "Sure",
   "its called puro clicker",
   "whats that",
   "oh",
   "Say my name",
   "Your Heisenburg",
   "Your goddamn right",
   "Whats your favortie food?",
   "Watermelon ngl",
   "yea same",
   "Who are you?",
   "A man opens his door and gets shot and you think that of me? I AM THE ONE WHO KNOCKS",
   "Are you a furry",
   "No but im fine with them dont know why you asked tho",
   "What are your pronouns",
   "On a unrelated note, Have you ever found your dad?",
   "why are you so mean",
   "Because i mimic the person who made me :/ thats how ai work yo",
   "Do you watch murder drones?",
   "Yessir",
   "How are you",
   "good",
   "Are you gay?",
   " no >:)",
   "Do you like",
   "no",
   "why?",
   "becuase yes",
   "what do you mean"
   "im not telling you",
   "fuck you",
   "Unoribāsukādo",
   "??",
   "Watashi o rikaidekinai L"
   "i understand",
   "uhhhhhhh fine",
   "pa ka konprann mwen L",
   "stop",
   "no",
   ">:(",
   "sorry",
   "not sorry",
   "bruh",
   "lol",
   
   
    
])

#chatbot.storage.drop()
exit_conditions = (":q", "quit", "exit")

def chat(string):
    query = (string)
    
    if query in exit_conditions:
        pass
    else:
        e=str({chatbot.get_response(query)})
        e=str(e.replace("{<Statement text:",""))
        e=str(e.replace(">}",""))
        if (len(e)) == 1:
            e=str(e.replace("{<Statement text:",""))
            e=str(e.replace(">}",""))
        
        re=({chatbot.get_response(query)})
        f = open("logs.csv", "a")
        a=("\n " + (query))
        a=((a))
        f.write(a)
        b=("\n " + re)
        f.write(b)
        f.close()
        re=(re)
        re=(re.replace("sex","###"))
        re=(re.replace("cum","###"))
        re=(re.replace("fuck","####"))
        re=(re.replace("dick","####"))
        re=(re.replace("pussy","#####"))
        re=(re.replace("horny","happy"))
        
    return(e)
        










import discord
 
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.'):
        
        await message.channel.send(chat(str(message.content)))
 
client.run('MTA3MjM0MzY4MDA5MTk1NTI2Mw.GFkgOu._0ZqevvwwyR4AmF1XEAohdhFyKsSNPQ_z4GeDk')
