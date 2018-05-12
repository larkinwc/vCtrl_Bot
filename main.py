import discord
import asyncio, aiohttp
import urllib.request as urllib
import requests

import os
from version import Version

client = discord.Client() #create discord client

#this is your GitHub oAuth key
auth_key = ""
if(auth_key == ""):
    auth_key = input("Please enter your Github oAuth key")
g = Version(auth_key)

#this is your discord token for an instance of a bot, you should create one at https://discordapp.com/developers/applications/me
discord_token = ''

try:
    settings = open("settings.txt", 'r')
    line = settings.readline()
    g._dir = line.split(':')[1] + '/'
    print(line.split(':')[1].split('/')[1])
    g._repo = g._token.get_user().get_repo(line.split(':')[1].split('/')[1])
    g._repoName = line.split(':')[1].split('/')[1]
    print(line)
    g._ignore = line.split(':')[1]
    settings.close()
except:
    repo = input("Please input your remote Github repo name that is under this token: ")
    g.setup(repo)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print('------')
    print()

@client.event
async def on_message(message):
    if len(message.attachments) > 0:
        file_list = list()
        for attach in message.attachments:
            img = requests.get(attach["url"])#fetch image
            print('.'+ attach["filename"].split('.')[1])
            if( ('.' + attach["filename"].split('.')[1] ) in g._ignore):
                await client.send_message(message.channel,'Unable to capture attachments, unsupported file types')
            else:   
                write_dir = os.path.join(g._dir, attach["filename"])
                with open(write_dir,'wb') as writer:#open for writing in binary mode
                    writer.write(img.content)#write the image
                    #file_list.append(write_dir) #add to list of images
                    file_list.append(attach["filename"]) #add to list of images
        if(len(file_list)):
            g.do_commit(file_list)
            await client.send_message(message.channel,'Attachment(s) Captured')



    if(message.content.startswith('$status')):
        await client.send_message(message.channel,'Current status:' + g.get_info())
        
        #this will return the current head branch info, last commit, etc. Can use basic github lib for this
        
    if(message.content.startswith('$undo') ):
        await client.send_message(message.channel,'Commit undone?: ' + g.undo_commit())
        #this will run a 1 commit undo, if not possible then will do nothing
        
    if(message.content.startswith('$ignore') ):
        targ = message.content.split(' ')[1]
        g._ignore.append(targ)
        await client.send_message(message.channel,'File type' + targ + ' is now ignored')
        g.write_settings()
        #this will contain a subcommand for the .extension, then it will add it to either memory or the 
        
    
    if(message.content.startswith('$pull') ):
        await client.send_message(message.channel,'Pulling branch')
        #currently unimplemented 
        
    if(message.content.startswith('$help') ):
        await client.send_message(message.channel,'Use "$commands" for a list of commands!. \n\nOfficial vCtrlBot documentation: ')

        
    if(message.content.startswith('$commands') ):
        await client.send_message(message.channel,'You can use the following commands:\n\n$status - gives you info on the currently setup repo \n$ignore - this will contain a subcommand for the .extension, then it will add it to either memory or the settings file \
         \n$pull - this will pull any commits\n$help - you can use $commands to view commands, also heres a link to the documentation for this bot: .')
        
'''for unity builds integration -- get project details https://build-api.cloud.unity3d.com/docs/1.0.0/index.html#operation--projects--projectupid--get

curl
  -X GET
  -H "Authorization: Basic [YOUR API KEY]"
  https://build-api.cloud.unity3d.com/api/v1/projects/{projectuid}

  then format json and take out     "scm": { } ?

'''

''' for slack integration use https://github.com/slackapi/python-slackclient '''

client.run(discord_token)