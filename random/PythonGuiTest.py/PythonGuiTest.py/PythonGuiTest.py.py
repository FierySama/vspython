from tkinter import *

# Making a very basic window

#root = blank windows from here on out
root = Tk() #kinter class we imported, root is our custom name
theLabel = Label(root, text="This is too easy")
theLabel.pack() # just puts the text anywhere it can

root.mainloop() # this repeats the window showing, though may not be necessary on py 3

