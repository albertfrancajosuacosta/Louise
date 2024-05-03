# Python program to illustrate the usage of 
# treeview scrollbars using tkinter


# Python program to illustrate the usage of 
# treeview scrollbars using tkinter





'''
from tkinter import ttk
import tkinter as tk

# Creating tkinter window
window = tk.Tk()
window.resizable(width = 1, height = 1)

# Using treeview widget
treev = ttk.Treeview(window, selectmode ='browse')

# Calling pack method w.r.to treeview
treev.pack(side ='right')

# Constructing vertical scrollbar
# with treeview
verscrlbar = ttk.Scrollbar(window, 
						orient ="vertical", 
						command = treev.yview)

# Calling pack method w.r.to vertical 
# scrollbar
verscrlbar.pack(side ='right', fill ='x')

# Configuring treeview
treev.configure(xscrollcommand = verscrlbar.set)

# Defining number of columns
treev["columns"] = ("1", "2", "3")

# Defining heading
treev['show'] = 'headings'

# Assigning the width and anchor to the
# respective columns
treev.column("1", width = 90, anchor ='c')
treev.column("2", width = 90, anchor ='se')
treev.column("3", width = 90, anchor ='se')

# Assigning the heading names to the 
# respective columns
treev.heading("1", text ="Name")
treev.heading("2", text ="Sex")
treev.heading("3", text ="Age")

# Inserting the items and their features to the 
# columns built
treev.insert("", 'end', text ="L1", 
			values =("Nidhi", "F", "25"))
treev.insert("", 'end', text ="L2",
			values =("Nisha", "F", "23"))
treev.insert("", 'end', text ="L3",
			values =("Preeti", "F", "27"))
treev.insert("", 'end', text ="L4",
			values =("Rahul", "M", "20"))
treev.insert("", 'end', text ="L5", 
			values =("Sonu", "F", "18"))
treev.insert("", 'end', text ="L6",
			values =("Rohit", "M", "19"))
treev.insert("", 'end', text ="L7", 
			values =("Geeta", "F", "25"))
treev.insert("", 'end', text ="L8", 
			values =("Ankit", "M", "22"))
treev.insert("", 'end', text ="L10", 
			values =("Mukul", "F", "25"))
treev.insert("", 'end', text ="L11",
			values =("Mohit", "M", "16"))
treev.insert("", 'end', text ="L12",
			values =("Vivek", "M", "22"))
treev.insert("", 'end', text ="L13",
			values =("Suman", "F", "30"))

# Calling mainloop
window.mainloop()
'''




import numpy as np

from scipy.stats import anderson
import pandas as pd

data = pd.read_excel("C:\\Users\\alber\\Documents\\LabMax\\teste.xlsx",index_col=None)

print(data.columns[0])

res = anderson(data[data.columns[0]], dist='norm')

print(res)

#print('Estatística')
#print(res[0])

#print('critical_values')
#print(res[1][2])

#print('significance_level')
#print(res[2][2])


'''
root = Tk()
root.title('Model Definition')
root.geometry('{}x{}'.format(460, 350))

# create all of the main containers
top_frame = Frame(root, bg='cyan', width=450, height=50, pady=3)
center = Frame(root, bg='gray2', width=50, height=40, padx=3, pady=3)
btm_frame = Frame(root, bg='white', width=450, height=45, pady=3)
btm_frame2 = Frame(root, bg='red', width=450, height=60, pady=3)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ew")
center.grid(row=1, sticky="nsew")
btm_frame.grid(row=3, sticky="ew")
btm_frame2.grid(row=4, sticky="ew")

# create the widgets for the top frame
model_label = Label(top_frame, text='Model Dimensions')
width_label = Label(top_frame, text='Width:')
length_label = Label(top_frame, text='Length:')
entry_W = Entry(top_frame, background="pink")
entry_L = Entry(top_frame, background="orange")

# layout the widgets in the top frame
model_label.grid(row=0, columnspan=3)
width_label.grid(row=1, column=0)
length_label.grid(row=1, column=2)
entry_W.grid(row=1, column=1)
entry_L.grid(row=1, column=3)

# create the center widgets
center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)

ctr_left = Frame(center, bg='blue', width=100, height=190)
ctr_mid = Frame(center, bg='yellow', width=100, height=190, padx=3, pady=3)
ctr_right = Frame(center, bg='green', width=100, height=190, padx=3, pady=3)


ctr_left.grid(row=0, column=0, sticky="ns")
ctr_mid.grid(row=0, column=1, sticky="nsew")
ctr_right.grid(row=0, column=2, sticky="ns")

root.mainloop()

import tkinter 
from tkinter import *


root = Tk() 

L1 = Label(root, text="User Name") 
L1.grid(row=0,column=0) 
L2 = Label(root, text="Password") 
L2.grid(row=1,column=0) 

mystr = StringVar() 
mystr.set('username@xyz.com') 

entry = Entry(textvariable=mystr, 
			state=DISABLED).grid(row=0, 
								column=1, 
								padx=10, 
								pady=10) 

passwd = Entry().grid(row=1,column=1, 
					padx=10,pady=10) 
mainloop() 


mu, sigma = 0, 0.1 # mean and standard deviation

s = np.random.normal(mu, sigma, 1000)

df = pd.DataFrame(s)

df.to_excel("teste.xlsx")



p = pd.read_excel('C:\\Users\\alber\\Documents\LabMax\\teste - Copia.xlsx', index_col=None, header=None)  

for linha in range(6):
            for coluna in range(1):
                print(p.iat[linha, coluna])
                
               

root = tk.Tk()

frame = BarraRolagem(root)

for i in range(50):
    ttk.Label(frame.scrollable_frame, text="Sample scrolling label").pack()

frame.pack()
root.mainloop()

'''