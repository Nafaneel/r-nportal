from tkinter import *

root = Tk()
root.geometry('280x400')
root.title('R_N Portal')


maintitle = Label(root, text=" N&R PORTAL")
maintitle.config(font=("Courier", 30))
maintitle.grid(row=1, column=2)


def rodrep():
    import webbrowser
    webbrowser.open('https://repl.it/@rodriveira2007/ArcticSteepEnvironment#main.py', new=2)
    root.quit()

def natrep():
    import webbrowser
    webbrowser.open('https://repl.it/@Nafaneel/PartnerFing#main.py', new=2)
    root.quit()


def clearscrn():
    sp = Label(root, text=" ")
    sp.grid(row=13, column=2)
    rod = Button(root, text="Rodrigo Rep.it", command=rodrep, borderwidth=5, width=16)
    rod.grid(row=14, column=2)
    sp1 = Label(root, text=" ")
    sp1.grid(row=15, column=2)
    nat = Button(root, text="Nathan Rep.it", command=natrep, borderwidth=5, width=16)
    nat.grid(row=16, column=2)

#    space = Label(root, text="                                                    ")
#    space.grid(row=1, column=2)
#    space1 = Label(root, text="                                                   ")
#    space1.grid(row=2, column=2)
#    space2 = Label(root, text="                                                   ")
#    space2.grid(row=3, column=2)
#    space3 = Label(root, text="                                                   ")
#    space3.grid(row=4, column=2) 
#    space4 = Label(root, text="                                                   ")
#    space4.grid(row=5, column=2)
#    space5 = Label(root, text="                                                   ")
#    space5.grid(row=6, column=2)
#    space6 = Label(root, text="                                                   ")
#    space6.grid(row=7, column=2)
#    space7 = Label(root, text="                                                   ")
#    space7.grid(row=8, column=2)
#    space8 = Label(root, text="                                                   ")
#    space8.grid(row=9, column=2)
#    space9 = Label(root, text="                                                   ")
#    space9.grid(row=10, column=2)
#    space10 = Label(root, text="                                                  ")
#    space10.grid(row=11, column=2)
#    space11 = Label(root, text="                                                  ")
#    space11.grid(row=12, column=2)
#    space12 = Label(root, text="                                                  ")
#    space12.grid(row=13, column=2)


def login():
    log = logentry.get()
    try:
        if log == "NC":
            logval = True
            pas = passwordentry.get()
            if pas == "1234":
                pasval = True
                if logval and pasval == True:
                    space2 = Label(root, text=" ")
                    space2.grid(row=11, column=2)
                    logged = Label(root, text="Loged In!", bg="lime green", fg="white", width=30)
                    logged.grid(row=12, column=2)
                    clearscrn()
                else:
                    logged = Label(root, text="Error!", bg="tomato", fg="white", width=30)
                    logged.grid(row=12, column=2)
                    
            else:
                space4 = Label(root, text=" ")
                space4.grid(row=11, column=2)           
                logged1 = Label(root, text="Error!", bg="tomato", fg="white", width=30)
                logged1.grid(row=12, column=2) 


         
        else:
            space3 = Label(root, text=" ")
            space3.grid(row=11, column=2)           
            logged1 = Label(root, text="Error!", bg="tomato", fg="white", width=30)
            logged1.grid(row=12, column=2) 
            



        if log == "RO":
            logval = True
            pas = passwordentry.get()
            if pas == "1234":
                pasval = True
                if logval and pasval == True:
                    space2 = Label(root, text=" ")
                    space2.grid(row=11, column=2)
                    logged = Label(root, text="Loged In!", bg="lime green", fg="white", width=30)
                    logged.grid(row=12, column=2)
                    clearscrn()
                else:
                    logged = Label(root, text="Error!", bg="tomato", fg="white", width=30)
                    logged.grid(row=12, column=2)
                    
            else:
                space4 = Label(root, text=" ")
                space4.grid(row=11, column=2)           
                logged1 = Label(root, text="Error!", bg="tomato", fg="white", width=30)
                logged1.grid(row=12, column=2) 


         
        else:
            space3 = Label(root, text=" ")
            space3.grid(row=11, column=2)           
            logged1 = Label(root, text="Error!", bg="tomato", fg="white", width=30)
            logged1.grid(row=12, column=2) 
    except:
        error = Label(root, text="Error!", bg="tomato", fg="white", width=30)
        error.grid(row=12, column=2)





logintext = Label(root, text="Login:")
logintext.grid(row=4, column=2)
logentry = Entry(root, borderwidth=5)
logentry.grid(row=5, column=2)
passtext = Label(root, text="Password:")
passtext.grid(row=6, column=2)
passwordentry = Entry(root, borderwidth=5)
passwordentry.grid(row=7, column=2)
space = Label(root, text=" ")
space.grid(row=8, column=2)
space1 = Label(root, text=" ")
space1.grid(row=9, column=2)
loginbutton = Button(root, text="Login", borderwidth=5, width=16, command=login)
loginbutton.grid(row=10, column=2)




root.mainloop()        

    