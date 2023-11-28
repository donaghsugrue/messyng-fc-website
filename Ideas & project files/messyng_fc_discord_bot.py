########## IMPORTS ##########
from colorama import Fore                                               # Dumb ass color library that prints to console in colours
import os                                                               # OS library, used to encrypt token in .env file
import discord                                                          # Discord.py library                                     #
from discord.ext import commands, tasks                                 # 
from discord.ext.commands import has_permissions, MissingPermissions    # 
from datetime import datetime                                           # Date & time



########## ENVIRONMENT STUFF ##########
token = os.getenv("token")                                              # Hides token in a .env file
prefix = "?"                                                            # In discord, what prefix do they need to put before a command to call a bot.
intents = discord.Intents.all()                                         #

intents = discord.Intents.default() # Dunno what the difference between all and default is
intents.message_content = True      # Dunno if this should be here

bot = commands.Bot(command_prefix = prefix, intents = intents)          #
client = discord.Client(intents = intents)                              #
# Create a "client" instance


Application_ID = 1080211621248507915
Public_key = "0e84ba795163aa9167885cd35e4d31005bc2b702d8cbe9babcb4f43cdcf254b4"


########## VARIABLES ##########
role_dictionary = {                                                     # Dictionary of reactions with lists of the roles they create and the comments that they must be applied to
  # reaction: role, comment_id,
  "bin-bin-react": ["1054144251367276664", ""],                         # Join the Church of Bin Bin
  "wantwant": ["1054144251367276664", ""],                              # Join the Church of Want Want
  "hammer-and-sickle": ["1054144251367276664", ""]                      # Sign up for the communist reading & fitness club
}

server_id = "1049369893755170816"                                      # Server ID for Messyng FC HQ. Do I want this to be a string or an int?



##########################################################################################################################################################
########## READY MESSAGE ##########
"""
@bot.event                                                                        # Discord.py's event decorator
async def on_ready():                                                             # Function for "on ready" 
  print(discord.__version__)                                                      # test prints the version of discord.py
  print(f"READY! Logged in as {Fore.PURPLE}{bot.user}")                           # Prints the bot's name and ID in the console


@bot.event
async def on_ready():
    print(f"{Fore.GREEN}The bot is online!")
    pipreminder.start()


@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client.user))

"""

########## REACTION MESSAGES ##########

### ADD REACTION ### 
@bot.event                                                                        # Discord.py's event decorator
async def on_raw_reaction_add(payload):                                           # Not sure what "payload" is, but it's needed. "on_raw_reaction_add" is specifically when a reaction is added to a comment that
    guild = discord.utils.find(lambda g : g.id == payload.guild_id, bot.guilds)   # "guild" and "server" are the same thing, so this is just a way to define the server

    if payload.emoji.name == "bin-bin-react" and payload.message_id:              # If a certain reaction is applied to a certain comment is the one you want
        role = discord.utils.get(guild.roles, name="bin-bin-react")               # Defin the role that you want to ole
        if role is not None:                                                      # If the role exists
            member = discord.utils.find()                                         # Define the member that you want to add the role to
            if member is not None:                                                # If the member exists
                await member.add_roles(role)                                      # Add the role to the user   
                print("Role added!")
    print("Reaction added!")


    if payload.guild_id is None:
        return  # Reaction is on a private message
    guild = client.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)

### REMOVE REACTION ###



"""
###  ###
@bot.command
async def react(ctx):
    
    react_message await message.send(message)
"""
























"""
        
##########  ##########

@bot.command()
@has_permissions(kick_members=True)
async def kick(ctx, kick_member:discord.Member,*, reason=None):
    if kick_member == bot.user:
        await ctx.send("You can't kick me :angry:")

    elif kick_member.top_role >= ctx.author.top_role:
        await ctx.send("This person's role is higher or equal to yours!")

    else:
        await kick_member.kick(reason=reason)

@kick.error
async def kick_error(message, error):
    if isinstance(error, MissingPermissions):
        await message.send("You don't have permissions to kick this member")





@bot.event
async def on_message(ctx):
    if ctx.author == bot.user:
        pass
    else:
        full = ctx.content
        if "pip" in full:
            await ctx.channel.send("If you're having any issues with pip, check out <#895483227244994641>")
        else:
            pass
        if ".gg" in full:
            await ctx.delete()
            await ctx.channel.send("Server invites aren't allowed here! {}".format(ctx.author.mention))
    await bot.process_commands(ctx)




##########  ##########
counter = 0
@tasks.loop(hours=3)
async def pipreminder():
    global counter
    # ID = Whatever channel u want (this sends auto message into channel every 3 hours, but doesn't stack [No duplication])
    channel = bot.get_channel(894746091382272000)
    messages = await channel.history(limit=2).flatten()

    for msg in messages:
        if msg.author == bot.user:
            counter +=1
    if counter >= 1:
        print(f"{Fore.RED}Duplicate detected, ignoring new message request\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Fore.RESET}")
        counter = 0
    else:
        await channel.send("If you're having any issues with pip, check out <#895483227244994641>\n`Automated Message`")
        print(f"{Fore.GREEN}Sent pip reminder to {Fore.MAGENTA}{channel}\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Fore.RESET}")





########## SEND MESSAGE ON MBR JOIN ##########
@bot.event
async def on_member_join(member):
    
    # Welcome message channel id
    wlc_channel = bot.get_channel(898420446125490186)
    
    # Role we want to add automatically
    wlc_role = "Member"
    role = discord.utils.get(member.guild.roles, name=wlc_role)
    await member.add_roles(role)

   
    embed = discord.Embed(title=f"Welcome {member.name}!", color = discord.Color.from_rgb(255,192,203)).set_author(name=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
    embed.add_field(name="Thank you for joining the server!", value=f"If you have any questions please check out <#895483227244994641> before asking in any support channels, also, please read\
    your code before asking, it saves ours and your time. If you're having an error with any code from a video, please ask in <#894746091382272000> -- Thank you :)", inline=True)
    embed.set_footer(icon_url=f"{member.guild.icon_url}", text=f"The server now has {member.guild.member_count} members!\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    await wlc_channel.send(embed=embed)
    msg = await wlc_channel.send(f"{member.mention}")
    await msg.delete()

"""

########## MUSIC BOT ##########
"""
@bot.event
async def on_member_join(member):
    
    # if voice channel empty
      # turn off bot
    # if voice channel not empty
      # if there is songs in the queue
        # play song
      # if there is no songs in the queue
        # play ddr
"""
  



##########################################################################################################################################################
########## RUN COMMANDS ##########

client.run(token)      # not sure what the difference between bot and client is, probably don't need both
bot.run(token)