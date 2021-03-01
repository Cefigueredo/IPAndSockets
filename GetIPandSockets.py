import sys
import socket
from tkinter import *
from tkinter import messagebox
from time import sleep
#-----------------------------------------------------------------------------
"""Initializing window"""
root = Tk()
root.title("Ip and Sockets")
root.iconbitmap("gato.ico")
root.geometry("300x140")
root.resizable(0, 0)

#The frame
myFrame=Frame(root, width=300, height=100)
myFrame.pack()


#Label of comment
commentL = Label(myFrame, text="Let the program run until finished.")
commentL.grid(row = 0, column = 0)


#Gets the host and IP
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
#First label for desktop name
firstLabel = Label(myFrame, text="Your desktop name is: ")
firstLabel.grid(row = 1, column = 0)
#First label for your IP
secondLabel = Label(myFrame, text="Your IP direction is: ")
secondLabel.grid(row = 2, column = 0)
#First label for Insert IP
thirdLabel = Label(myFrame, text="Insert IP to search opened sockets: ")
thirdLabel.grid(row = 3, column = 0)


#First test for desktop name
firstText=Text(myFrame, width=12, height=1)
firstText.insert(END, hostname)
firstText.configure(state=DISABLED)
firstText.grid(row = 1, column = 1)
#First test for your ip
secondText=Text(myFrame, width=12, height=1)
secondText.insert(END, ip)
secondText.configure(state=DISABLED)
secondText.grid(row = 2, column = 1)

dirIP = StringVar()
#Textbox to insert an IP to search for opened sockets
textBox=Entry(myFrame, width=16, textvariable=dirIP)
textBox.grid(row=3, column=1)

#Update the number of socket
var = StringVar()
var.set(0)

l = Label(myFrame, text = "# Socket: ")
l.grid(row=4, column=0)

t = Label(myFrame, textvariable = var)
t.grid(row=4, column=1)
#It helps to cancel the method
boolean=False
#Methods----------------------------------------------------------------------
def searchSockets():
    boolean=False
    try:
        openedSockets=[]
        
        for port in range (1, 150):
            if boolean==True:
                break
            s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)  
            resultado = s.connect_ex((textBox.get(), port))
            var.set(port)
            root.update_idletasks()
            if resultado == 0:
                print("The socket {} is open.".format(port))
                openedSockets.append(format(port))
            s.close()
                
            
            
        messagebox.showinfo("Opened Sockets", openedSockets)
    except:
        print("\nSaliendo...")
        sys.exit(0)
def cancel():
    boolean=True
#EndMethods-------------------------------------------------------------------

button0 = Button(myFrame, text="Insert", command=searchSockets)
button0.grid(row=5, column=0)
button1 = Button(myFrame, text="Cancel", command=cancel)
button1.grid(row=5, column=1)
root.mainloop() 






            
    



  