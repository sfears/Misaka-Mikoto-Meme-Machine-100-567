﻿import discord
from discord.ext.commands import bot
from discord.ext import commands
import random
import os

Client = discord.Client()
bot_prefix= "!"
client = commands.Bot(command_prefix=bot_prefix)
d_token_file = open("Discord Token.txt", "r")
Token = d_token_file.read()
d_token_file.close()
MainChannelID = "367903165993189379"
MainChannel = client.get_channel(MainChannelID)

CritLines = ["Headshot!", "Critical Hit!", "Booyeah!", "Crit!", "Finish him!", "Get pwn'd!"]
CritFailLines = ["Oof", "Fatality!", "Ouch, ooch, oof your bones!", "That'll hurt in the morning..."]
Roll1D1Lines = ["...What did you think would happen?", "...Why?", "Are you ok?",  "Do you need a doctor?", "What else did you think it would do?"]
MemeLines = ["You.", "I'm running out of memes...", "This entire project.", "Ay, aren't you a funny guy.", "<Insert something cringy here>","tElL mE a mEmE!1!111!!1!!!!one!111!11", "Are you feeling it now mr. crabs?", "1v1 me on rust, howbou dah?"]
StartupLines = ["*Yawn* Hello friends!", "おはようございます!", "おはよう、お父さん", "Ohayō, otōsan!", "Alright, who's ready to die?", "Greetings humans.", "My body is Reggie."]
ShutdownLines = ["Bye!", "Farewell comrades!", "さようなら、お父さん!", "Misaka doesn't wish to leave."]
Character = 'test.txt'

@client.event
async def on_ready():
    print("Hello Nerds")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    #MainChannel = client.get_channel(MainChannelID)
	#await client.send_message(MainChannel, StartupLines[random.randint(0, len(StartupLines)-1 )])

#@client.event
#async def on_message(message):
#        if message.content == "weed" or message.content == "Weed":
#                await client.send_message(message.channel, "I hear that's how people get magic powers or something.")

@client.command(pass_context=True)
async def char(ctx,):
    if os.path.isfile(ctx.message.author.id + ".txt"):
        file = open(ctx.message.author.id + ".txt", 'r+')
        message = file.read()
        print(message)
        await client.say(message)
        file.close

@client.command(pass_context=True)
async def bored(ctx):
    if ctx.message.author.id == "287697603607658496":
        await client.say("Play Magic with someone!")
    else:
        print(ctx.message.author.id + " broke a rule or something")



@client.command(pass_context=True)
async def newchar(ctx, name):
    if os.path.isfile(ctx.message.author.id + ".txt"):
        await client.say("Ayy lmao you already got a character!")
    else:
        char = open(ctx.message.author.id + ".txt", 'w+')
        char.write(name)
        print("done")
        char.close()
        await client.say("And thus " + name + " was born")

@client.command(pass_context=True)
async def delchar(ctx,):
    if os.path.isfile(ctx.message.author.id + ".txt"):
        file = open(ctx.message.author.id + ".txt", 'r+')
        await client.say("Gonna delet " + file.read() + ".")
        file.close()
        os.remove(ctx.message.author.id + ".txt")
    else:
        await client.say("Ain't got no character you deadbeat!")

@client.command(pass_context=True)
async def ping(ctx):
        print (ctx.message.author.id + " pinged") 
        await client.say("Pong!")

@client.command(pass_context=True) #coinflip stuff
async def coinflip(ctx):
        HeadTails = random.randint(1,2)
        if HeadTails == 1:
                await client.say("Tails, but you're dead either way")
        else:
                await client.say("Heads, but you're dead either way")

@client.command(pass_context=True)
async def weeb(ctx):
    await client.say("He's not a weeb!")

#@client.command(pass_context=True)  yeah turns out this rolls multiples of 3 from 3 to 18, so it's not useful
#async def stats(ctx):
    #await client.say("**```prolog" + "\n" +
       # "Strength:     " + str(random.randint(1,6)*3) + "\n" +
       # "Intelligence: " + str(random.randint(1,6)*3) + "\n" +
       # "Wisdom:       " + str(random.randint(1,6)*3) + "\n" +
       # "Dexterity:    " + str(random.randint(1,6)*3) + "\n" +
       # "Constitution: " + str(random.randint(1,6)*3) + "\n" +
       # "Charisma:     " + str(random.randint(1,6)*3) + "```**"
    #)

@client.command()
async def stats(Quantitystr: str=3, Setstr: str=7):#currently the default is 3, but optionally one can use another as so: "!stats 4" becomes 6 sets of 4d6
        Invalid = False
        try:
                Quantity = int(Quantitystr)
        except ValueError:
                Invalid = True
        try:
                Set = int(Setstr)
        except ValueError:
                Invalid = True
        if Invalid == True:
                await client.say("...I have no idea what you meant by that. \n Usage: !stats (Number of dice per stat) (Number of stats) \n (If you use more than three dice per stat, only the top 3 will be used.)")
                return
        
        if Quantity >100:
                await client.say("WHAAA! I can't roll that many dice, you do it!")
                return

        if Set >10:
                await client.say("I'm not gonna roll that many stats, do it yourself!")
                return#rolling stuff all over the place
        print("Rolling " + str(Set) + " sets of " + str(Quantity) + " 6-sided dice.")
        StatRound = 0
        Strength = 0
        Intelligence = 0
        Wisdom = 0
        Dexterity = 0
        Constitution = 0
        Charisma = 0
        Comeliness = 0
        while StatRound < Set:
                Total = 0
                i = 0
                Numbers = [0,0,0]
                while i < Quantity:
                        Roll = random.randint(1,6)
                        Numbers.extend([Roll])
                        print("Rolled " + str(Roll) + ".")
                        i = i + 1
                        if i == Quantity:
                                x = 0
                                while x < 3:
                                        Total += max(Numbers)
                                        Numbers.remove(max(Numbers))
                                        x = x + 1
                                if Strength == 0:
                                        Strength = Total
                                        print("Strength = " + str(Strength))
                                else:
                                        if Intelligence == 0:
                                                Intelligence = Total
                                                print("Strength = " + str(Strength))
                                        else:
                                                if Wisdom == 0:
                                                        Wisdom = Total
                                                        print("Intelligence = " + str(Intelligence))
                                                else:
                                                        if Dexterity == 0:
                                                                Dexterity = Total
                                                                print("Dexterity = " + str(Dexterity))
                                                        else:
                                                                if Constitution == 0:
                                                                        Constitution = Total
                                                                        print("Constitution = " + str(Constitution))
                                                                else:
                                                                        if Charisma == 0:
                                                                                Charisma = Total
                                                                                print("Charisma = " + str(Charisma))
                                                                        else:
                                                                                if Comeliness == 0:
                                                                                        Comeliness = Total
                                                                                        print("Comeliness = " + str(Comeliness))
                                StatRound = StatRound + 1
        await client.say("**```css" + "\n" + "Strength:     " + str(Strength) + "\n" + "Intelligence: " + str(Intelligence) + "\n" + "Wisdom:       " + str(Wisdom) + "\n" + "Dexterity:    " + str(Dexterity) + "\n" + "Constitution: " + str(Constitution) + "\n" + "Charisma:     " + str(Charisma) + "\n" + "Comeliness    " + str(Comeliness) + "```**")

@client.command()#I changed it to Quantity'D'Sides because that's the data in the string and it makes sense okay
async def roll(QuantityDSides: str):
	
	#Identify Devider
        #You know it's spelled 'Divider,' right?
	Devider = 0
	i = 0
	while i < len(QuantityDSides):
		letter = QuantityDSides[i]
		if letter == "D" or letter == "d":
			Devider = i
		i = i + 1

	#Check formatting and tell you to screw off
	Invalid = False
	if Devider == 0:
		Invalid = True
	Quantity = 0
	Sides = 0

	try: #"try:" tries to do the given action and if there's a non-lethal error run the code in "except ValueError" instead of crying in the output. 
		Quantity = int(QuantityDSides[:Devider])		#Identify Quantity
	except ValueError:
		Invalid = True

	try: #so right now it's testing if Quantity and Sides are actually numbers and not people trying to hurt senpai.
		Sides    = int(QuantityDSides[Devider+1:])	#Identify Sides
	except ValueError:
		Invalid = True

	if Invalid == True:
		await client.say("'{}'? That's not how you roll a dice, silly! Use '!roll xDy'. \n x = Number of dice, \n y = Dice sides. \n ie: '!roll 2D6'.".format(QuantityDSides))
		return

	#Check dice quantity
	if Quantity > 100:
		print("Too many dice detected. WTF?")
		await client.say("WHAAA! I can't roll that many dice, you do it!")
		return

	#Actually roll the dice
	print("Rolling " + str(Quantity)+ " " +str(Sides) + " sided dice.")
	Total = 0
	TotalCrits = 0
	i = 0
	while i < Quantity:
		global Canceling
		Roll = random.randint(1,Sides)
		print("Rolled " + str(Roll) + ".")
		if Roll == Sides:
			TotalCrits = TotalCrits + 1
			print("Crit!")
		Total += Roll
		i = i + 1

	#Say the result
	print("Total is " + str(Total) + " with " + str(TotalCrits) + " crits!")
	await client.say(str(Total))# + " with " + str(TotalCrits) + " crits!")
	if Quantity == 1 and Total == Sides and not Sides == 1:
		await client.say(CritLines[random.randint(0, len(CritLines)-1 )])
	if Quantity == 1 and Total == 1 and not Sides == 1:
		await client.say(CritFailLines[random.randint(0, len(CritFailLines)-1 )])
	if Total == 69:
		await client.say("Nice.")
	if Quantity == 1 and Sides == 1:
		await client.say(Roll1D1Lines[random.randint(0, len(Roll1D1Lines)-1 )])
	if Total == 7 or Total == 77 or Total == 777 or Total == 7777:
		await client.say("Seben is my FABORIT number! But my faborit FABORIT number is seben BILLION!")
	if Quantity == 9 and Sides == 11:
		await client.say("Bush did it!")
      
@client.command(pass_context=True) #You want the books? Well too bad here they are. 
async def handbook(ctx):
    await client.say("Here's the PDF: \n http://archmagev.com/1st_Ed/Rulebooks/TSR02010B%20-%20Player's%20Handbook%20(Revised%20Cover%20-%20Orange%20Spine).pdf")

@client.command(pass_context=True)
async def dmsguide(ctx):
    await client.say("Here's the PDF: \n http://archmagev.com/1st_Ed/Rulebooks/TSR02011A%20-%20Dungeon%20Master's%20Guide%20(Original%20Cover).pdf \n No metagaming!")

@client.command(pass_context=True)
async def booklist(ctx):
    await client.say("Here's the index: \n http://archmagev.com/1st_Ed/Rulebooks/ \n No metagaming!")

@client.command()
async def TellMeAMeme():
    await client.say(MemeLines[random.randint(0, len(MemeLines)-1 )])
    
@client.command(pass_context=True)
async def headpat(ctx):
    if ctx.message.author.id == "287697603607658496":
        await client.say(ShutdownLines[random.randint(0, len(ShutdownLines)-1 )])
        client.logout()
        raise SystemExit
    else:
        await client.say(Roll1D1Lines[random.randint(0, len(Roll1D1Lines) - 1)])

@client.command()#Why is this still here it's less productive than a squirrel in winter.
async def push(remote: str, branch: str):
    await client.say('Pushing to {} {}'.format(branch, remote))

client.run(Token)
