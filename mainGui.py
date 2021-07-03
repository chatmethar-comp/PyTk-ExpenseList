from tkinter import *
from tkinter import ttk,messagebox
import datetime
import csv

root = Tk()
root.title('Expense note author zizzer')
root.geometry('500x600+100+100')


tab = ttk.Notebook(root)
T1 = Frame(tab)
T2 = Frame(tab)
tab.pack(fill=BOTH,expand =1)

iconT1 = PhotoImage(file='wallet.png')
iconT2 = PhotoImage(file='cash.png').subsample(2)


tab.add(T1,text = f'{"add Expense":^{30}}',image=iconT1,compound='top')
tab.add(T2,text= f'{"all Expense":^{30}}',image=iconT2,compound='top')

f1 = Frame(T1)
f1.pack()


def save(event=None):
    try:
        expense = v_expense.get()
        price = costexpense.get()
        piece = pieceExpense.get()
        dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
        print('list:',expense,'\tcost:',price,'\tpiece:',piece)
        text = 'list:',expense,'\tcost:',price,'\tpiece:',piece,'\nTOTAL:',price*piece
        v_result.set(text)
        with open('ExpeseList.csv','a',encoding='utf-8',newline='') as f:
            #with automatic open
            #'a' save and save 'w' write again(delete old)
            fw = csv.writer(f)
            data = [dt,expense,price,piece,price*piece]
            fw.writerow(data)
    except Exception as e:
        print('error')
        messagebox.showerror('Error','Invalid number in price or piece')
        #messagebox.showwaring('Error',e)
        #messagebox.showinfo('Error',e)
    v_expense.set('')
    costexpense.set('')
    pieceExpense.set('')
    entry1.focus()  

root.bind('<Return>',save)
Font1 = (None,20)
Fonttitle = (None,30)

iconHeadT1 = PhotoImage(file='bbanknote.png')

mainicon =Label(f1,image=iconHeadT1)
mainicon.pack()
TitleT1 = Label(f1,text='Expense List',font=(None,30))
TitleT1.pack()
#--------------------------------------------
L = ttk.Label(f1,text = 'list name',font=Font1)
L.pack()

v_expense = StringVar()

entry1 = ttk.Entry(f1,textvariable=v_expense,font=Font1)#input text
entry1.pack()

#--------------------------------------------
costexpense = IntVar()

L2 = ttk.Label(f1,text='price',font=Font1)
L2.pack()

entrycost = ttk.Entry(f1,textvariable=costexpense,font=Font1)
entrycost.pack()

#--------------------------------------------
pieceExpense = IntVar()

L3 = ttk.Label(f1,text='piece',font=Font1)
L3.pack()

entryPiece = ttk.Entry(f1,textvariable=pieceExpense,font=Font1)
entryPiece.pack()

iconSave = PhotoImage(file='floppy.png').subsample(2)
button1 = ttk.Button(f1,text='Save',command = save,image=iconSave,compound='left')
button1.pack(ipadx=20,ipady=10)

v_result = StringVar()
v_result.set('---result---')
result = ttk.Label(f1,textvariable=v_result,font=Font1)
result.pack(pady=20)

root.mainloop()
