from http import client
import tkinter 
import time 
import  socket
import threading
from tkinter import *

root = Tk()
root.geometry("300x500")
root.config(bg="white")

def func():
    t=threading.Thread(target=recv)
    t.start()

def recv():
    listensocket=socket.socket()
    port=3050
    maxconnection=99
    ip=socket.gethostname()
    
    listensocket.bind(('',port))
    listensocket.listen(maxconnection)
    (clientsocket,address)=listensocket.accept()
    
    
    while  True:
        sendermessage=clientsocket.recv(1024).decode()
        if not sendermessage=="":
            time.sleep(5)
            lstbox.insert(0,"client : "+ sendermessage)
            
            
xr=0           
            
def sendmsg():
    global xr
    if xr==0:
        s=socket.socket()
        #ENTER THE OTHER PC'S NAME 
        hostname='DESKTOP-SM09E3C'
        port=4050
        s.connect((hostname,port))
        msg=messagebox.get()
        lstbox.insert(0,"You : " + msg)
        s.send(msg.encode())
        xr=xr+1
        
        
        
    else:
        msg=messagebox.get()
        lstbox.insert(0,"You : "+msg)
        s.send(msg.encode())
    
    
    
                
            
def threadsendmsg():
    th=threading.Thread(target=sendmsg)
    th.start()
            
        


startchatimage=PhotoImage(file='start2.png')
buttons=Button(root,image=startchatimage,command=func,borderwidth=0)
buttons.place(x=90,y=10)

message=StringVar()
messagebox=Entry(root,textvariable=message,font=('calibre',10,'normal'),border=2,width=32)
messagebox.place(x=10,y=444,width=250,height=40)

sendmessageimg=PhotoImage(file='send2.png')

sendmessagebutton=Button(root,image=sendmessageimg,command=threadsendmsg,borderwidth=0)
sendmessagebutton.place(x=255,y=440)

lstbox=Listbox(root,height=20,width=43)
lstbox.place(x=15,y=80)


root.mainloop()

