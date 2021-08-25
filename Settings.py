#Imports
from PIL import Image, ImageDraw, ImageFont, ImageTk
import random, glob, tkinter, time, os

root = tkinter.Tk()
button_frame = tkinter.Frame(root)
buttonList = ['aqaaaaaa']
availList = []
#Setup Vars used throughout the program
tkte = None
tkpi = None
delay = 150
windowWidth=1000
windowHeight=1000

colors = ['#fc8edf','#3bb4ed','#f76c8a','#6cf793','#ffffff','#000000']
singlewords = [['Stare'],['Goon'],['Submit'],['Slave'],['Stroke'],['Obey'],['Cum'],['Forever']]
doublewords = [['Mind','Empty'],['Drop','Deeper'],['Good','Boy'],['Keep','Stroking'],['Forever','Mine']]
triplewords = [['Fuck','My','Tits'],['My','New','Toy'],['Call','Me','Mommy'],["You're",'My','Slave']]
masterwords = (singlewords,doublewords,triplewords)
Font = 'C:/Windows/Fonts/NotoSans-Bold.ttf'
