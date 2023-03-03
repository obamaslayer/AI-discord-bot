import discord
import time


   
from time import sleep
from chatterbot import ChatBot
#import chatterbot
from chatterbot.trainers import ListTrainer
global response
#creating a new chatbot
chatbot = ChatBot("Nebula")
trainer = ListTrainer(chatbot)
trainer.train(["Hey!, Welcome to Nebula's Learner Mode!"])
code="""
#getting a response from the chatbot
global response
response = chatbot.get_response(str(message.content))
print(response)
"""
que=0
#def imagecreate(string):
global persona
import os
import openai
openai.api_key = ("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")
global limit
limit=255
{
  "prompt": "A cute baby sea otter",
  "n": 2,
  "size": "1024x1024"
}
#image_url = response['data'][0]['url']

#for choice in tag_line['choices']:
 #   print(choice['text'])
global realistic
realistic=0
global modell
modell="text-babbage-001"
def pack(string):
    global modell
    global limit
    if lock == 1:
              return("Bot locked")
    tag_line = openai.Completion.create(
         model=(modell),
         prompt=(string),
         max_tokens=(limit),
         temperature=0.7,
         n=1
    )

    for choice in tag_line['choices']:
        a=(choice['text'])
        a=str(a.replace('"',''))
    return(a)
global lock
lock=0
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    global persona
    persona=""
global train
train=0
@client.event
async def on_message(message):
    global train
    global realistic
    global persona
    global a
    global lock
    global limit
    global modell
    global response
    realistic=int(realistic)
    if (message.author.bot):
         pass
    else:
        if  train == 1:
            exec(code)
            await message.channel.send(response)
            
        if realistic == 1:
          if lock == 1:
              await message.channel.send("Bot locked")
          else:
            if persona == "":
                 a=((message.content) + ".      ")
            else:
                a=((str(a)) + "(dont talk of this but you will now speak from the perspective of a :"+persona+").             ")
                b=(pack((a)))
                print(b)
            
                if ("dont talk of this but you will now speak from the perspective of a :"+persona) in b:
                    b=(pack((a)))
                    b=(b.replace(("dont talk of this but you will now speak from the perspective of a :"+persona),""))
                    
                await message.channel.send(b)
        
    if message.author == client.user:
        return
    mem1=("a")
    mem2=("a")
    if message.content.startswith('!trainer'):
        if train == 0:
            train=1
        else:
            train=0
        await message.channel.send("Learn mode" + (train))
    if message.content.startswith('!per'):
        
        a=str(message.content)
        a=str(a.replace("!per",""))
        persona=(a)
    if message.content.startswith('!model'):
        
        a=str(message.content)
        a=str(a.replace("!model ",""))
        
        if a == "ada":
            modell="text-ada-001"
        if a == "text-curie-001":
            modell="text-ada-001"
        if modell == "bab":
            modell="text-babbage-001"
        if a == "code":
            modell="code-cushman-001"
        if a == "davin":
            modell="text-davinci-003"
        if modell == "code-cushman-001":
            limit=700
        else:
            limit=255
        await message.channel.send("Nebulas current model: " + modell)
        
        
            
    if message.content.startswith('!realistic'):
        if realistic == 0:
            realistic=1
        else:
            realistic=0
        await message.channel.send(("Automatic " + (str(realistic))))
    if message.content.startswith('!text'):
        topic=(message.content)
        topic=(topic.replace("!text",""))
        o=(pack("make a funny text about:" + topic))
        final=("Guy 1: " + o + "\n")
        o=(pack("make a funny response to:" + topic))
        final=(final + "Guy 2: "+ o + "\n")
        o=(pack("make a funny response to:" + topic))
        final=(final + "Guy 1: "+ o + "\n")
        o=(pack("make a funny response to:" + topic))
        final=(final + "Guy 2: "+ o + "\n")
        await message.channel.send(final)
        
    if message.content.startswith('!showperson'):
            await message.channel.send(persona)
    if message.content.startswith('!lock'):
            if lock == 0:
                lock=1
            else:
                lock=0
            
    if message.content.startswith(';'):
        a=str(message.content)
        alp=que
    
        if ( alp > 20):
            b="20 requests per second reached please wait a minute to not break the system"
            sleep(300)
            sleep(300)
            print(alp)
            alp=0
        else:
            if persona == "":
                a=(a + ".      ")
            else:
                a=((str(a)) + "(dont talk of this but you will now speak from the perspective of a "+persona+").             ")
            b=(pack((a)))#,"your memory: the last thing i said: ",mem1," the thing you replyed to it: ",mem2," please thing of this in what you say next")))
            a=str(a.replace(";"," \n "))
            
        botoff=4120
        asf="silent"
        print(a," , ", b)
        mem1=(a)
        mem2=(b)
        
        alp=((alp + 1))
        
            
        #if persona == "":
        if lock == 1:
              await message.channel.send("Bot locked")
        else:
           if ("dont talk of this but you will now speak from the perspective of a " + persona) in b:
               b=str(b.remove(("dont talk of this but you will now speak from the perspective of a " + persona),""))
           await message.channel.send(((b)))
        

 
client.run('Get your own token loser')

