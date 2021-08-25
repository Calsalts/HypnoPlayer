# HypnoPlayer
Since as of right now there is no exe for this you will need IDLE or some Python IDE to run this script from.

Running the program:
- Take the images you want the player to use and put them in folders however you please (yes, they must be in folders). It can be in one folder or you can split it up into      different folders however you please.
  
- Take the 3 .py files in the github and place them in the same folder.
  It should look something like this 
  
  ![File Structure](https://i.imgur.com/WB06DEn.png)
  
- Open zoomloop.py in IDLE or your IDE of choice and run the program. Once on the main window, there will be buttons corresponding to your folder names. Click the ones you want, press 'load image', then press "Clicky Clicky" at the bottom to start the program
  
About Settings.Py
- As is implied you can modify how the player functions by changing....
  - Delay: Modifies how fast the player will switch between images/text in milliseconds.
  - windowWidth and windowHeight: Changes how large the window of the hypnoplayer is
  - Colors: The player will choose from these hexcodes to decide the color of the text and background on text frames
  - Words: Modify this to change which words the player will display during text frames.
    - Make sure to keep double words in lengths of 2 words, triple words in lengths of 3, and single words in lengths of 1
  - Font: You can change what font the player will use by declaring a directory to a font in your font folder here

Things to know
- Python is a slow program, so the player unfortunately won't be completely smooth. This can be abated by
  - Using JPG's instead of PNG's
  - Increasing Delay works(?)
  - Decreasing window size should work as well.
  - ***YOU MUST DECLARE A FONT***. An unfortunate result of the way I coded this/a possible limitation of tkinter is that the program *requires* you to declare a font in Settings.py.
    - If you're on windows I believe the font I have setup is a default font already.
  - The images you put in the folders *will not* be resized. If the image the player is trying to display is 800x800 and you've set your window size to be 1000x1000, it will not fill out the entire image. Similarly, if the image to be displayed is 1200x1200 and the window is 1000x1000, the window will cut off the image. My preferred method was to take it into gimp/paint 

Possible quick updates?
I think I want to rewrite this in C++ for faster speed, but I may fix some of these (hopefully) quick to fix isses.
- Have everything in Settings.py read from some kind of config file
  - Dubious use considering that, since this is source code and not an exe file, Settings.py is always available to modify at any time.
- Lift the strict requirement of the user declaring a font in Settings.py
- Reinstate the rescaling and centering functions already present in the code
  - This would allow all the images in folders to be unmodified and still sit within the window by having the program rescale the images before the image loop starts.
    - It sounds convenient but I still didn't like it, even when I had the functions in use. Images still only *kinda* fit since they're expanded to fit the height or width, still leaving borders on whichever one it isn't scaled to. Still, some people would prefer that rather than have to take *every image* they want to loop through into gimp and edit it.
