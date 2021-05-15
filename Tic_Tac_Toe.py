import tkinter as tk 
from tkinter import messagebox
root = tk.Tk()
root.title('Tic Tac Toe Game')

def checkwinner():
	winner = False
	if b1["text"] == 'X' and b2['text'] == 'X' and b3["text"] == 'X':
		b1.config(bg='yellow')
		b2.config(bg='yellow')
		b3.config(bg='yellow')
		winner=True
		messagebox.showinfo('Tic Tac Toe','Congrats! X Wins')
		window()
	elif b4["text"] == 'X' and b5['text'] == 'X' and b6["text"] == 'X':
		b4.config(bg='yellow')
		b5.config(bg='yellow')
		b6.config(bg='yellow')
		winner=True
		messagebox.showinfo('Tic Tac Toe','Congrats! X Wins')
		window()
	elif b7["text"] == 'X' and b8['text'] == 'X' and b9["text"] == 'X':
		b7.config(bg='yellow')
		b8.config(bg='yellow')
		b9.config(bg='yellow')
		winner=True
		messagebox.showinfo('Tic Tac Toe','Congrats! X Wins')
		window()
	elif b1["text"] == 'X' and b4['text'] == 'X' and b7["text"] == 'X':
		b1.config(bg='yellow')
		b4.config(bg='yellow')
		b7.config(bg='yellow')
		winner=True
		messagebox.showinfo('Tic Tac Toe','Congrats! X Wins')
		window()
	elif b2["text"] == 'X' and b5['text'] == 'X' and b8["text"] == 'X':
		b2.config(bg='yellow')
		b5.config(bg='yellow')
		b8.config(bg='yellow')
		winner=True
		messagebox.showinfo('Tic Tac Toe','Congrats! X Wins')
	elif b3["text"] == 'X' and b6['text'] == 'X' and b9["text"] == 'X':
		b3.config(bg='yellow')
		b6.config(bg='yellow')
		b9.config(bg='yellow')
		winner=True
		messagebox.showinfo('Tic Tac Toe','Congrats! X Wins')
		window()
	elif b1["text"] == 'X' and b5['text'] == 'X' and b9["text"] == 'X':
		b1.config(bg='yellow')
		b5.config(bg='yellow')
		b9.config(bg='yellow')
		winner=True
		messagebox.showinfo('Tic Tac Toe','Congrats! X Wins')
		window()
	elif b3["text"] == 'X' and b5['text'] == 'X' and b7["text"] == 'X':
		b3.config(bg='yellow')
		b5.config(bg='yellow')
		b7.config(bg='yellow')
		winner=True
		messagebox.showinfo('Tic Tac Toe','Congrats! X Wins')
		window()
	elif b1["text"] == 'O' and b2['text'] == 'O' and b3["text"] == 'O':
		b1.config(bg='yellow')
		b2.config(bg='yellow')
		b3.config(bg='yellow')
		winner=True
		messagebox.showinfo('Tic Tac Toe','Congrats! O Wins')
		window()
	elif b4["text"] == 'O' and b5['text'] == 'O' and b6["text"] == 'O':
		b4.config(bg='yellow')
		b5.config(bg='yellow')
		b6.config(bg='yellow')
		winner=True
		messagebox.showinfo('Tic Tac Toe','Congrats! O Wins')
		window()
	elif b7["text"] == 'O' and b8['text'] == 'O' and b9["text"] == 'O':
		b7.config(bg='yellow')
		b8.config(bg='yellow')
		b9.config(bg='yellow')
		winner=True
		messagebox.showinfo('Tic Tac Toe','Congrats! O Wins')
		window()
	elif b1["text"] == 'O' and b4['text'] == 'O' and b7["text"] == 'O':
		b1.config(bg='yellow')
		b4.config(bg='yellow')
		b7.config(bg='yellow')
		winner=True
		messagebox.showinfo('Tic Tac Toe','Congrats! O Wins')
		window()
	elif b2["text"] == 'O' and b5['text'] == 'O' and b8["text"] == 'O':
		b2.config(bg='yellow')
		b5.config(bg='yellow')
		b8.config(bg='yellow')
		winner=True
		messagebox.showinfo('Tic Tac Toe','Congrats! O Wins')
		window()
	elif b3["text"] == 'O' and b6['text'] == 'O' and b9["text"] == 'O':
		b3.config(bg='yellow')
		b6.config(bg='yellow')
		b9.config(bg='yellow')
		winner=True
		messagebox.showinfo('Tic Tac Toe','Congrats! O Wins')
		window()
	elif b1["text"] == 'O' and b5['text'] == 'O' and b9["text"] == 'O':
		b1.config(bg='yellow')
		b5.config(bg='yellow')
		b9.config(bg='yellow')
		winner=True
		messagebox.showinfo('Tic Tac Toe','Congrats! O Wins')
		window()
	elif b3["text"] == 'O' and b5['text'] == 'O' and b7["text"] == 'O':
		b3.config(bg='yellow')
		b5.config(bg='yellow')
		b7.config(bg='yellow')
		winner=True
		messagebox.showinfo('Tic Tac Toe','Congrats! O Wins')
		window()
	if winner == False and count == 9:
		messagebox.showinfo('Tic Tac Toe','Oops! Match Draw')
		window()
def btn_click(btn):
	global click,count

	if btn["text"] == '' and click== True:
		btn.config(text='X')
		click=False
		count+=1
		print(count)
		checkwinner()
	elif btn["text"] == '' and click == False:
		btn.config(text='O')
		click=True
		count+=1
		print(count)
		checkwinner()
	else:
		messagebox.showerror('Tic Tac Toe','Button Already Clicked!')

def window():

	global click,count
	click = True
	count = 0 
	global b1,b2,b3,b4,b5,b6,b7,b8,b9
	b1 = tk.Button(root,text='',height=3,width=6,font=("Arial",20),command=lambda:btn_click(b1))
	b2 = tk.Button(root,text='',height=3,width=6,font=("Arial",20),command=lambda:btn_click(b2))
	b3 = tk.Button(root,text='',height=3,width=6,font=("Arial",20),command=lambda:btn_click(b3))
	b4 = tk.Button(root,text='',height=3,width=6,font=("Arial",20),command=lambda:btn_click(b4))
	b5 = tk.Button(root,text='',height=3,width=6,font=("Arial",20),command=lambda:btn_click(b5))
	b6 = tk.Button(root,text='',height=3,width=6,font=("Arial",20),command=lambda:btn_click(b6))
	b7 = tk.Button(root,text='',height=3,width=6,font=("Arial",20),command=lambda:btn_click(b7))
	b8 = tk.Button(root,text='',height=3,width=6,font=("Arial",20),command=lambda:btn_click(b8))
	b9 = tk.Button(root,text='',height=3,width=6,font=("Arial",20),command=lambda:btn_click(b9))

	b1.grid(row=0,column=0)
	b2.grid(row=0,column=1)
	b3.grid(row=0,column=2)
	b4.grid(row=1,column=0)
	b5.grid(row=1,column=1)
	b6.grid(row=1,column=2)
	b7.grid(row=2,column=0)
	b8.grid(row=2,column=1)
	b9.grid(row=2,column=2)

	root.mainloop()

window()