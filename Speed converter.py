from tkinter import *

root= Tk()

def kphToMph():
    kphValue= float(kphEntry.get())
    mphValue= round(kphValue/1.609,2)
    mph.config(text= f"{mphValue}")
def mphToKph():
    kphValue2= float(mphEntry.get())
    mphValue2= round(kphValue2*1.609,2)
    kph.config(text= f"{mphValue2}")
def clear():
    kphEntry.delete(0, END)
    mphEntry.delete(0, END)
    mph.config(text= "")
    kph.config(text= "")

root.geometry("320x200")
root.resizable(True, True)
root.title("Speed converter")
root.configure(bg= "Light Blue")

frameEntry= Frame(root).grid(row= 0, column= 0, columnspan= 2, padx= 15, pady= 15)

Label(frameEntry, text= "Kph").grid(column=0, row= 0, padx= 5, pady= 5)
kphEntry= Entry(frameEntry, width=15, bg= "White").grid(column=0, row=1, padx= 5, pady= 5)

Label(frameEntry, text= "Mph").grid(column= 2, row= 0, padx= 15, pady= 5)
mph= Label(frameEntry, width= 15, bg= "White").grid(column= 2, row= 1, padx= 5, pady= 5)

Label(frameEntry, text= "Mph").grid(column=0, row= 3, padx= 5, pady= 5)
mphEntry= Entry(frameEntry,width= 15, bg= "White").grid(column= 0, row= 4, padx= 5, pady= 5)

Label(frameEntry, text= "Kph").grid(column=2, row= 3, padx=5, pady=5)
kph= Label(frameEntry, width= 15, bg= "White").grid(column= 2, row= 4, padx= 5, pady= 5)

Button(frameEntry, text= "Convert", command= mphToKph).grid(column=1, row= 4, padx= 5, pady= 5)
Button(frameEntry, text= "Convert", command= kphToMph).grid(column= 1, row= 1, padx= 15, pady= 5)
Button(frameEntry, text= "Clear all", command= clear).grid(column=1, row= 5, padx= 5, pady= 15)

root.mainloop()