from tkinter import *
import tkinter.messagebox
tk=Tk()
tk.title('Tic-Tac-Toe')
pa = StringVar()
pb = StringVar()
p1 = StringVar()
p2 = StringVar()

p1_name = Entry(tk, textvariable=p1, bd=5)
p1_name.grid(row=1, column=1, columnspan=8)
p2_name = Entry(tk, textvariable=p2, bd=5)
p2_name.grid(row=2, column=1, columnspan=8)

click=True
flag=0
def bclick(buttons):
	global click,pa,pb,flag,p1_name,p2_name
	if buttons["text"]==" " and click==True:
		buttons["text"]="X"
		click=False
		flag+=1
		pa=p1.get()+' Wins!'
		pb=p2.get()+' Wins!'
		CheckForWin()
	elif buttons["text"]==" " and click==False:
		buttons["text"]="O"
		click=True
		flag+=1
		CheckForWin()
	else:
		tkinter.messagebox.showinfo('Tic-Tac-Toe','Button already clicked!')
def Disable_buttons():
	button1.config(state=DISABLED)
	button2.config(state=DISABLED)
	button3.config(state=DISABLED)
	button4.config(state=DISABLED)
	button5.config(state=DISABLED)
	button6.config(state=DISABLED)
	button7.config(state=DISABLED)
	button8.config(state=DISABLED)
	button9.config(state=DISABLED)
def CheckForWin():
	if((button1["text"]=='X' and button2["text"]=='X' and button3["text"]=='X')or
	(button4["text"]=='X' and button5["text"]=='X' and button6["text"]=='X') or
	(button7["text"]=='X' and button8["text"]=='X' and button9["text"]=='X') or
	(button1["text"]=='X' and button4["text"]=='X' and button7["text"]=='X') or
	(button2["text"]=='X' and button5["text"]=='X' and button8["text"]=='X') or
	(button3["text"]=='X' and button6["text"]=='X' and button9["text"]=='X') or
	(button1["text"]=='X' and button5["text"]=='X' and button9["text"]=='X') or
	(button3["text"]=='X' and button5["text"]=='X' and button7["text"]=='X')):
		Disable_buttons()
		tkinter.messagebox.showinfo('Tic-Tac-Toe',pa)
	elif((button1["text"]=='O' and button2["text"]=='O' and button3["text"]=='O')or
        (button4["text"]=='O' and button5["text"]=='O' and button6["text"]=='O') or
        (button7["text"]=='O' and button8["text"]=='O' and button9["text"]=='O') or
        (button1["text"]=='O' and button4["text"]=='O' and button7["text"]=='O') or
        (button2["text"]=='O' and button5["text"]=='O' and button8["text"]=='O') or
        (button3["text"]=='O' and button6["text"]=='O' and button9["text"]=='O') or
        (button1["text"]=='O' and button5["text"]=='O' and button9["text"]=='O') or
        (button3["text"]=='O' and button5["text"]=='O' and button7["text"]=='O')):
		Disable_buttons()
		tkinter.messagebox.showinfo('Tic-Tac-Toe',pb)
	elif(flag==8):
		tkinter.messagebox.showinfo('Tic-Tac-Toe',"It's a tie")


label = Label( tk, text="Player 1:", font='Times 20 bold', bg='white', fg='blue', height=1, width=8)
label.grid(row=1, column=0)


label = Label( tk, text="Player 2:", font='Times 20 bold', bg='white', fg='blue', height=1, width=8)
label.grid(row=2, column=0)

button1 = Button(tk, text=" ", font='Times 20 bold', bg='deep sky blue', fg='red', height=4, width=8, command=lambda: bclick(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font='Times 20 bold', bg='deep sky blue', fg='red', height=4, width=8, command=lambda: bclick(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ',font='Times 20 bold', bg='deep sky blue', fg='red', height=4, width=8, command=lambda: bclick(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=' ', font='Times 20 bold', bg='deep sky blue', fg='red', height=4, width=8, command=lambda: bclick(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font='Times 20 bold', bg='deep sky blue', fg='red', height=4, width=8, command=lambda: bclick(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font='Times 20 bold', bg='deep sky blue', fg='red', height=4, width=8, command=lambda: bclick(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=' ', font='Times 20 bold', bg='deep sky blue', fg='red', height=4, width=8, command=lambda: bclick(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font='Times 20 bold', bg='deep sky blue', fg='red', height=4, width=8, command=lambda: bclick(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font='Times 20 bold', bg='deep sky blue', fg='red', height=4, width=8, command=lambda: bclick(button9))
button9.grid(row=5, column=2)

tk.mainloop()
