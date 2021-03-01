import sys
import socket
from tkinter import *
from tkinter import messagebox

"""Initializing window"""
root = Tk()
root.title("Ip and Sockets")
root.iconbitmap("gato.ico")
root.geometry("300x100")
root.resizable(0, 0)

myFrame=Frame(root, width=300, height=200)
myFrame.pack()


#Gets the host and IP
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

firstLabel = Label(myFrame, text="Your desktop name is: ")
firstLabel.grid(row = 0, column = 0)
secondLabel = Label(myFrame, text="Your IP direction is: ")
secondLabel.grid(row = 1, column = 0)
thirdLabel = Label(myFrame, text="Insert IP to search opened sockets: ")
thirdLabel.grid(row = 2, column = 0)

dirIP = StringVar()

firstText=Text(myFrame, width=12, height=1)
firstText.insert(END, hostname)
firstText.configure(state=DISABLED)
firstText.grid(row = 0, column = 1)

secondText=Text(myFrame, width=12, height=1)
secondText.insert(END, ip)
secondText.configure(state=DISABLED)
secondText.grid(row = 1, column = 1)

textBox=Entry(myFrame, width=16, textvariable=dirIP)
textBox.grid(row=2, column=1)

def searchSockets():
    try:
        messagebox.showinfo("Opened Sockets", "Searching")
        openedSockets=[]
        
        for port in range (1, 26):
            s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            print("PasaTimeout")
            resultado = s.connect_ex((textBox.get(), port))
            print("Pasa resultado")
            if resultado == 0:
                print("The socket {} is open.".format(port))
                openedSockets.append(format(port))
            s.close()
                
            messagebox.close()
            
        messagebox.showinfo("Opened Sockets", openedSockets)
    except:
        print("\nSaliendo...")
        sys.exit(0)

button = Button(root, text="Insertar", command=searchSockets)#.grid(row=3, column=0)
button.pack()
root.mainloop() 
 





            
    



  