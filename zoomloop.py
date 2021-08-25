import zoomfunctions
import Settings

#Calculate x and y offsets to get center of image
###Deprecated code from pre-zoom era
#def centerCalc(image):
#    xOffset = (1000-image.width())/2
#    yOffset=(1000-image.height())/2
#    return xOffset, yOffset

#Stretch image to window while maintaining ratio
#def imageStretch(image):
#    ratio = image.size[0]/image.size[1]
#    if(image.size[0]-windowWidth>image.size[1]-windowHeight):
#        xSize = windowWidth
#        ySize = int(xSize/ratio)
#    else:
#        ySize = windowHeight
#        xSize = int(ySize*ratio)
#   return xSize,ySize

def changeImage():
    #global tkpi #need global so that the image does not get derefrenced out of function
    #get random image
    Settings.tkpi = zoomfunctions.chooseImage(Settings.availList)
    #Place image  
    label_image = Settings.tkinter.Label(Settings.root, image=Settings.tkpi).place(x=0,y=0)
    #Decide if we're going to display a text image or standard image next
    if(zoomfunctions.Settings.random.randint(1,10)<3):
       Settings.root.after(Settings.delay,changeText2)
    else:
        Settings.root.after(Settings.delay, changeImage)

#Proof of Concept before merging with changeText1
def changeText2():
    #This random num determines which wordlist we'll pull from
    num = 1
    #This random num determines if multi-word texts will display sequentially or broken up
    randnum = Settings.random.randint(0,1)
    #Create our sequence of text images
    tktes = zoomfunctions.createText2(num)
    #I should probably seperate out multiple text displays as their own functions since they're faster
    #But that's not generalizable AND I'm lazy
    for x in range(0,num):
        #Put text in a label tkinter can use
        label_text = Settings.tkinter.Label(Settings.root, image=tktes[x]).place(x=0,y=0)
        #Disaply text
        Settings.root.update()
        #Can't use root.delay LOL
        Settings.time.sleep(Settings.delay/1000)
        #Are we displaying the text images interspersed with standard images?
        if randnum==1:
            #Create standard image
            label_image = Settings.tkinter.Label(Settings.root, image=zoomfunctions.chooseImage(Settings.availList)).place(x=0,y=0)
            #Show the image
            Settings.root.update()
            #Still can't use root.delay LMAO
            Settings.time.sleep(Settings.delay/1000)
    #Choose whether to send a standard image next, or a text image
    if(Settings.random.randint(1,10)<3):
       Settings.root.after(0,changeText2)
    else:
        Settings.root.after(0, changeImage)

#Event function to handle right click to close
def key(event):
    Settings.root.destroy() 


def main():
    #Get dimensions to make root window
    geometry = "%dx%d" % (Settings.windowWidth, Settings.windowHeight)
    Settings.root.geometry(geometry)
    
    #This button frame will cover the root window and display
    Settings.button_frame.pack(fill=Settings.tkinter.X, side = Settings.tkinter.TOP)
    
    #Get all folders in CWD
    Folders = zoomfunctions.getFolders()
    #Turn Folder filenames into buttons
    buttonList2 = zoomfunctions.createButtons(Folders)
    #Create Button that will let us load the images to make
    loadButton = Settings.tkinter.Button(Settings.root, text = "Load Images", command=zoomfunctions.createImageList2)
    loadButton.pack()
    

    
    #availList = convertToPhoto(createImageList())
    startButton = Settings.tkinter.Button(Settings.root, text = "Clicky Clicky", command=changeImage)
    startButton.pack(side = Settings.tkinter.BOTTOM)
    #Main text for the image loop
    #Start image loop
    #changeImage()
    #Bind Left Click To Closing Window
    Settings.root.bind("<Button-3>", key)
    Settings.root.mainloop()

main()