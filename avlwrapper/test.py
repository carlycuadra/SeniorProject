import Tkinter 
import tkMessageBox
import json
from Tkinter import *
import tkFileDialog as filedialog
import fileinput
# import avlwrapper as avl
from math import radians, sqrt, tan
import subprocess
from PIL import ImageTk,Image  
import ttk
import os
from subprocess import Popen, PIPE


root = Tkinter.Tk()
root.title('AVL Test')
root.iconbitmap('airplane.ico')
root.geometry("900x500")
w = Tkinter.Label(root, text=" AVL Editor",compound = Tkinter.CENTER,font = "Helvetica 50 bold italic",bg="#303030",fg="#FFFFFF")
x = Tkinter.Label(root, text=" Update existing AVL files to alter the geometry of an aircraft ",compound = Tkinter.CENTER,font = "Helvetica 20 italic",bg="#303030",fg="#FFFFFF")
w.pack()
x.pack()
 
root.configure(bg='#303030')

pwd = os.getcwd()


def open_txt():
	avl_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open Text File", filetypes=(("AVL Files", "*.avl"), ))
	f = open(avl_file, 'r')
	path=os.path.abspath(avl_file)
	print("path is ",path)
	a=[]
	l=f.readlines()
	for ind in range(len(l)):
		if 'SURFACE' in l[ind]:
			print(l[ind+1])
			a.append(l[ind+1].rstrip('\n'))
			filtered = [x for x in a if x.strip()]
	print(a)
		
	variable = StringVar(root)
	variable.set("Select Surface") 
	w = OptionMenu(root, variable, *filtered)
	w.configure(background="#303030")
	w.place(x=560,y=150)
	# print(variable.get())
	avl_path=avl_file
	print(avl_path)
	avl_file = open(avl_file, 'r')
	content = avl_file.read()
	myPath=os.path.basename(avl_path)
	title = Tkinter.Label(root, text=myPath.title(),font = "Helvetica 23 bold italic",bg="#303030",fg="#FFFFFF")
	title.place(x=120,y=105)
	my_frame = Frame(root,width=40,height=15)
	my_frame.place(x=20,y=165)
	# my_frame.pack(pady=10)

	# Create scrollbar
	text_scroll = Scrollbar(my_frame)
	text_scroll.pack(side=RIGHT, fill=Y)



	my_text = Text(my_frame, width=40, height=15, font=("Helvetica", 16), yscrollcommand=text_scroll.set, undo=True)
	my_text.insert(END, content)
	my_text.place(x=20,y=250)
	my_text.pack()

	# Configure our scrollbar
	text_scroll.config(command=my_text.yview)
	avl_file.close()
	root.title('AVL Editor')

def change_X():
	avl_file = avl_file = filedialog.askopenfilename(initialdir="/Users/carlycuadra/Documents/SeniorProject/Avl/runs/avl_file", title="Open AVL File", filetypes=(("AVL Files", "*.avl"), ))
	x = x_coord.get()
	b = "test"
	for line in fileinput.FileInput(avl_file,inplace=1):
		line=line.rstrip()
		if 'Xref' in b:
			temp = line.split()
			rep = temp[0] + " "
			new_x = x + " "
			line = line.replace(rep, new_x, 1)
		b = line
		print(line)
				
def change_Y():
	avl_file = avl_file = filedialog.askopenfilename(initialdir="/Users/carlycuadra/Documents/SeniorProject/Avl/runs/avl_file", title="Open AVL File", filetypes=(("AVL Files", "*.avl"), ))
	y = y_coord.get()
	b = "test"
	for line in fileinput.FileInput(avl_file,inplace=1):
		line=line.rstrip()
		if 'Yref' in b:
			temp = line.split()
			rep = " " + temp[1] + " "
			new_y = " " + y + " "
			line = line.replace(rep, new_y, 1)
		b = line
		print (line)

def change_Z():
	avl_file = avl_file = filedialog.askopenfilename(initialdir="/Users/carlycuadra/Documents/SeniorProject/Avl/runs/avl_file", title="Open AVL File", filetypes=(("AVL Files", "*.avl"), ))
	z = z_coord.get()
	b = "test"
	for line in fileinput.FileInput(avl_file,inplace=1):
		line=line.rstrip()
		if 'Zref' in b:
			temp = line.split()
			y_val = temp[1]
			z_val = temp[2]
			y_string = " " + temp[1] + " "
			rep = " " + temp[2]
			new_z = " " + z
			if y_val == z_val:
				line = line.replace(rep, new_z, 2)
				line = line.replace(new_z, y_string, 1)
			else:
				line = line.replace(rep, new_z, 1)
		b = line
		print (line)

def change_scale():

	avl_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open Text File", filetypes=(("AVL Files", "*.avl"), ))

	new_scale=scale.get()
	print("opened: "+avl_file)
	f = open(avl_file, 'r')
	g = open('avl_file', 'w')
	l=f.readlines()

	for ind in range(len(l)):
		if 'SCALE' in l[ind]:
			print(l[ind+1])
			l[ind+1]=new_scale+'\n'
			
			g.write(l[ind])
		else:
			g.write(l[ind])

	os.remove(avl_file)
	os.rename('avl_file', avl_file)
	g.close()
	f.close()
  

def change_translate():
	avl_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open Text File", filetypes=(("AVL Files", "*.avl"), ))
	trans=translate_But.get()
	print("opened: "+avl_file)
	f = open(avl_file, 'r')
	g = open('avl_file', 'w')
	l=f.readlines()

	for ind in range(len(l)):
		if 'TRANSLATE' in l[ind]:
			print(trans)
			l[ind+1]=trans+'\n'
			print(l[ind+1])
			g.write(l[ind])
		else:
			g.write(l[ind])

	os.remove(avl_file)
	os.rename('avl_file', avl_file)
	g.close()
	f.close()

def save_txt():
	avl_file = filedialog.askopenfilename(initialdir="/Users/carlycuadra/Documents/SeniorProject/Avl/runs/avl_file", title="Open AVL File", filetypes=(("AVL Files", "*.avl"), ))
	avl_file = open(avl_file, 'w')
	avl_file.write(my_text.get(1.0, END))


def loadImg():
	avl_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open Text File", filetypes=(("AVL Files", "*.avl"), ))
	path=os.path.abspath(avl_file)
	avl335 = pwd + "/avl3.35"

	p=subprocess.Popen(avl335, shell=True, stdin=subprocess.PIPE)
	p.stdin.write("LOAD "+path+os.linesep)
	p.stdin.write('OPER' + os.linesep)
	p.stdin.write('G' + os.linesep)

open_button = Button(root, text="Select AVL File", command=open_txt,highlightbackground="#303030")
open_button.pack()
open_button.place(x=575,y=180)


x_coord = Entry(root, width=5)
x_coord.place(x=450,y=280)

coordinates_button = Button(root, text="Change X coordinate", command=change_X,highlightbackground="#303030")
coordinates_button.pack()
coordinates_button.place(x=400,y=250)


y_coord = Entry(root, width=5)
y_coord.pack()
y_coord.place(x=600,y=280)
coordinates_button = Button(root, text="Change Y coordinate", command=change_Y,highlightbackground="#303030")
coordinates_button.pack()
coordinates_button.place(x=560,y=250)

z_coord=Entry(root,width=5)
z_coord.pack()
z_coord.place(x=760,y=280)
coordinates_button = Button(root, text="Change Z coordinate", command=change_Z,highlightbackground="#303030")
coordinates_button.pack()
coordinates_button.place(x=720,y=250)

preview = Tkinter.Label(root, text=" Select an AVL file to see a preview of the content ",font = "Helvetica 13 italic",bg="#303030",fg="#FFFFFF")
preview.place(x=20,y=140)

u = Tkinter.Label(root, text=" Separate each value with a space (Eg: 1.0 1.0 1.0) ",font = "Helvetica 13 italic",bg="#303030",fg="#FFFFFF")
u.place(x=485,y=330)
scale = Entry(root, width=5)
scale.place(x=565,y=380)
scale_button = Button(root, text="Scale", command=change_scale,highlightbackground="#303030")
scale_button.pack()
scale_button.place(x=560,y=350)

translate_But = Entry(root, width=5)
translate_But.pack()
translate_But.place(x=645,y=380)
translate_button = Button(root, text="Translate", command=change_translate,highlightbackground="#303030")
translate_button.pack()
translate_button.place(x=630,y=350)

img_but = Button(root, text="Load geometry", command=loadImg,highlightbackground="#303030")
img_but.pack()
img_but.place(x=575,y=450)


root.mainloop()
