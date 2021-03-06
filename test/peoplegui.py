from tkinter import *
from tkinter.messagebox import showerror
import shelve
shelvename = 'class-shelve'
fieldnames = ('name','age','job','pay')
def makeWidgets():
    global entries
    window = Tk()
    window.title('People Shelve')
    form = Frame(window)
    form.pack()
    entries = {}
    for (ix,label) in enumerate(('key',)+fieldnames):
        lab = Label(form, text=label)
        ent = Entry(form)
        lab.grid(row=ix, column=0)
        ent.grid(row=ix, column=1)
        entries[label] = ent
    Button(window,text='Fetch', command=(lambda:fetchRecord())).pack(side=LEFT)
    Button(window, text='Update', command=updateRecord).pack(side=LEFT)
    Button(window, text='Close', command=window.quit()).pack(side=RIGHT)

def fetchRecord():
    key = entries['key'].get()
    try:
        record = db[key]
    except:
        showerror(title='erroe',message='no such key!')
    else:
        for field in fieldnames:
            entries[field].delete(0, end)
            entries[field].insert(0, repr(getattr(record,  field)))

def updateRecord():
    key = entries['key'].get()
    if key in db:
        record = db[key]
    else:
        from test.person import Person
        record = Person(name='?', age='?')
    for field in fieldnames:
        setattr(record,field,eval(entries[field].get()))
    db[key] = record

db = shelve.open(shelvename)
window = makeWidgets(),mainloop()