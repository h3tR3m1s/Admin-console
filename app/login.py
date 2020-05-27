import tkinter as tk
import json
import os
import sys
import time
path = os.getcwd()
root = tkinter.Tk()
class LoginScreen:
    def __init__(self, master):
        def create_window():
            Mainwindow = Toplevel()
        with  open(path + '\Data.json','r') as data:
            loaded = json.load(data)
        if loaded["NewUser"] == True:
            usernameinput = tk.StringVar()
            passwordinput = tk.StringVar()
            confirmpassword = tk.StringVar()
            tk.Label(root, text='Create new account').grid(row=0,column=1)
            tk.Label(root, text='Username:').grid(row=1,column=1)
            tk.Label(root, text='Password:').grid(row=2,column=1)
            tk.Label(root, text='Confirm Password:').grid(row=3,column=1)
            tk.Entry(root, textvariable = usernameinput,bd=5).grid(row=1,column=2)
            tk.Entry(root,show="*", textvariable = passwordinput,bd=5).grid(row=2,column=2)
            tk.Entry(root,show="*", textvariable = confirmpassword,bd=5).grid(row=3,column=2)
            def logincomm():
                if passwordinput.get() == confirmpassword.get() and not passwordinput.get() == None and not usernameinput.get() == None:
                    with  open(path + '\Data.json','w') as data:
                        data.write(json.dumps({
                            "UserName":usernameinput.get(),
                            "Password":passwordinput.get(),
                            "NewUser": False
                        }))
                else:
                    tk.Label(root,fg='red', text="Passwords don't match").grid(row=0,column=0)        
            tk.Button(root,command=login, text='logincomm').grid(row=4,column=2)
        else:
            usernameinput = tk.StringVar()
            passwordinput = tk.StringVar()
            tk.Label(root, text='Username').grid(row=0,column=0)
            tk.Label(root, text='Password').grid(row=1,column=0)
            tk.Entry(root, textvariable = usernameinput,bd=5).grid(row=0,column=1)
            tk.Entry(root,show="*",textvariable = passwordinput,bd=5).grid(row=1,column=1)
            def login():
                if usernameinput.get()== loaded['UserName'] and passwordinput.get() == loaded['Password']:
                    print('login succesful')       
                    create_window()         
            tk.Button(root, text='Login', command=login).grid(row=2,column =1)
class Main:
    def __init__(self, master):
        tk.Label(Mainwindow, text='Create new account').grid(row=0,column=1)
root.mainloop()
