from movie import movie_recommend
import pandas as pd
from tkinter import *


model  = movie_recommend()
movie_name = 'None'

movie_titles = pd.read_csv('./Movie_Id_Titles')
win= Tk()

win.geometry("715x250")
menu= StringVar()
menu.set("Select Any Movie")
cnt = 0
drop= Listbox(win, width=40, height=10, selectmode=MULTIPLE)
for lang in movie_titles['title'].values:
    drop.insert(cnt,lang)
    cnt = cnt+1

def selected_item():
	global movie_name
	movie_name = [drop.get(name) for name in drop.curselection()][0]
        
btn = Button(win, text='select movie', command=selected_item)
btn.pack(side='bottom')
drop.pack()
win.mainloop()

print(model.alike_movie(movie_name))
