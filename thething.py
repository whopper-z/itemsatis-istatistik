import discord
import requests
from bs4 import BeautifulSoup


url = "https://www.itemsatis.com/profil/239549/lames.html"
R = requests.get(url)
soup = BeautifulSoup(R.text,"html5lib")

userName = soup.find("div", {"class":"userDetails"}).h1.text 
userActivity = soup.find("div",{"class":"userDetails"}).small.text
userSuccesfulSells = soup.find("div",{"class":"userPointPositive"}).text
userRatePoint = soup.find("div",{"class":"reviewTotal color-rating-9"}).text
userRatings = soup.find("div",{"class":"reviewCount"}).text
userRegisterDate = soup.find("div",{"class":"userRegister"}).text
userAvatar = soup.find("div",{"class":"userAvatar"}).src

lastComment = soup.find("div",{"class":"postBoxProfile"}).text




client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name=userSuccesfulSells, url="https://www.twitch.tv/ "))
    print("{0.user} Online.".format(client))
    
  

  
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$bilgi'):
        embedmsg = discord.Embed(title="Lames İstatistik Botu", description="Datas:", color=0x00ff00)
        embedmsg.add_field(name="Username", value=userName, inline=False)
        embedmsg.add_field(name="User Register Date", value=userRegisterDate, inline=False)
        embedmsg.add_field(name="Activity", value=userActivity, inline=False)
        embedmsg.add_field(name="Rate Point", value=userRatePoint, inline=False)
        embedmsg.add_field(name="Succesful Sales", value=userSuccesfulSells, inline=False)
        embedmsg.add_field(name="Total Rating", value=userRatings, inline=True)
        embedmsg.add_field(name="Last Sale", value=lastComment, inline=False)
        embedmsg.set_thumbnail(url = message.author.avatar_url)


        await message.channel.send(embed=embedmsg)

        
client.run("ur token goes here")
