import Settings, tkinter, PIL
#from tkinter import *
from numpy import concatenate
# =============================================================================
# ----------------------IMAGE CREATION FUNCTIONS------------------------------
# These functions related to creating images that are to be shown in the loop
# =============================================================================
#Creates an array of all images to be randomly looped through
#INPUT: No input required
#RETURNS: Returns all images from a specific folder in an array
def createImageList():
    availList1 = Settings.glob.glob("AhriPink/Zooms/*.png")
    availList2 = Settings.glob.glob("AhriPink/Zooms/*.jpg")
    availList=availList1+availList2
    return availList

def createImageList2():
    tmp = []
    for button in Settings.buttonList:
        if button.getState()==True:
            tmp = tmp+(Settings.glob.glob(button.getName()+"/*.png"))
            tmp = tmp+(Settings.glob.glob(button.getName()+"/*.jpg"))
    Settings.availList = convertToPhoto(tmp)
#Chooses a random image from the image array.
#Functionally just a random select
#INPUT: A list of images to randomly choose from
#OUTPUT: A singular image from that list, randomly chosen
def chooseImage(imageList):
    #Get Random Image
    #Since we choose one at a time, we can shuffle then choose the 0th image
    Settings.random.shuffle(imageList)
    return imageList[0]

#Images loaded by python aren't automatically ready for use with tkinter.
#This function will convert them into PhotoImages which can be used
#INPUT: An array of images to be converted to PhotoImages
#OUTPUT: The same images in a PhotoImage Format
def convertToPhoto(imageList):
    tmp=[]
    #Resize all images to fit within canvas
    for image in imageList:
        #image = Image.open(image)
        image = Settings.ImageTk.PhotoImage(PIL.Image.open(image))
        tmp.append(image)
    
    imageList=tmp
    return imageList

# =============================================================================
# ------------------------TEXT CREATION FUNCTIONS-----------------------------
# These functions relate to creating text that will be shown in the image loop
# =============================================================================
#Creates a randomly colored background to be used for the createText func
#INPUT:Nothing
#OUTPUT: A PIL image of a solid color
def createBackground():
    #We'll choose between pink. cyan, red, green, and white
    Settings.random.shuffle(Settings.colors)
    img = Settings.Image.new('RGB', (1000, 1000), Settings.colors[0])
    #Let's make sure we didnt' pick black
    while(Settings.colors[0] == '#000000'):
        Settings.random.shuffle(Settings.colors)
        img = Settings.Image.new('RGB', (1000, 1000), Settings.colors[0])
    return img,Settings.colors[0]

#Creates a requested number of words over a solid color background
#INPUT: Requested number of words to be created
#OUTPUT: Returns an array of created words
def createText2(imgNumber):
    #Get the specific wordlist we'll use
    wordList = Settings.masterwords[imgNumber-1]
    Settings.random.shuffle(wordList)
    wordList=wordList[0]
    #Array to hold all created images
    createdImgs = []
    for x in range(0,imgNumber):
        #Create background our text will be on
        background,backHex = createBackground()
        #Create canvas to edit the iamge
        Settings.draw = Settings.ImageDraw.Draw(background)
        #Get a random string
        text = wordList
        #Set-up font and text size
        fnt = Settings.ImageFont.truetype(Settings.Font,250)
        #Create random offset along y axis
        yOffset = Settings.random.randint(0,1000-fnt.getsize(text[x])[1])
        xOffset = (1000-fnt.getsize(text[x])[0])/2
        Settings.draw.text((xOffset,yOffset), text[x],font = fnt, fill = Settings.colors[1])
        createdImgs.append(Settings.ImageTk.PhotoImage(background))
 
    return createdImgs
# =============================================================================
# ------------------------ZOOM LOOP FUNCTIONS---------------------------------
# These functions relate to how the program will loop between images and text
# =============================================================================
# =============================================================================
# These WOULD be the correct functions to call but for some reason tkinter 
# throws a hissy fit whenever I try it. It'll stay here just in case I ever 
# feel like trying to debug.
# =============================================================================
#def changeImage(root, availList):
#    global tkpi #need global so that the image does not get derefrenced out of function
#    global delay
#    #get random image
#    tkpi = chooseImage(availList)
#    #Place image  
#    label_image = tkinter.Label(root, image=tkpi).place(x=0,y=0)
#    if(random.randint(1,10)<2):
#       root.after(delay,changeText2(root, availList))
#    else:
#        root.after(delay, changeImage(root, availList))
        
#def changeText2(root, availList):
#    num = random.randint(1,3)
#    randnum = random.randint(0,1)
#    #global tkte
#    #global tkpi
#    #global delay
#    tktes = createText2(num)
#    for x in range(0,num):
#        label_text = tkinter.Label(root, image=tktes[x]).place(x=0,y=0)
#        root.update()
#        time.sleep(delay/1000)
#        if randnum==1:
#            label_image = tkinter.Label(root, image=chooseImage(availList)).place(x=0,y=0)
#            root.update()
#            time.sleep(delay/1000)
#    if(random.randint(1,10)<2):
#       root.after(0,changeText2(root, availList))
#    else:
#        root.after(0, changeImage(root, availList))


# =============================================================================
# -------------------------Misellanious Functions-----------------------------
# =============================================================================
def getFolders():
    global buttonList
    return [ f.name for f in Settings.os.scandir(Settings.os.getcwd()) if f.is_dir() ]

def createButtons(Folders):
    Settings.buttonList = []
    for f in Folders:
        if f != '__pycache__':
            newButton = Application(Settings.root, f, False, False)
            #newButton = tkinter.Button(button_frame, text = f)
            #newButton.grid(row = i, column = j, sticky = tkinter.W + tkinter.E)
            #i+=5
            Settings.buttonList.append(newButton)
    #print(buttonList)
    return Settings.buttonList
        
# =============================================================================
# -----------------------------Classes----------------------------------------
# =============================================================================
class Application(tkinter.Frame):
    def changeState(self):
        self.pressed = not self.pressed
        self.changeRelief()
        
    def changeRelief(self):
        if self.getState()==True:
            self.buttonName.config(relief=tkinter.SUNKEN)
        else:
            self.buttonName.config(relief=tkinter.RAISED)

    def getState(self):
        return self.pressed
    
    def getName(self):
        return self.buttonName["text"]
    
    def createWidgets(self,buttonName, onOffState, Down):
        self.pressed = onOffState
        self.relief = Down
        
        self.buttonName = tkinter.Button(self)
        self.buttonName["text"] = buttonName,
        self.buttonName["command"] = self.changeState

        self.buttonName.pack({"side": "left"})
        

    def __init__(self, master, buttonName, onOffState, Down):
        tkinter.Frame.__init__(self, master)
        self.pack()
        self.createWidgets(buttonName, onOffState, Down)