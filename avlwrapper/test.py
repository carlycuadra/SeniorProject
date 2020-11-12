import Tkinter 
import tkMessageBox
import json
from Tkinter import *
import tkFileDialog as filedialog
import fileinput
import avlwrapper as avl
from math import radians, sqrt, tan
import subprocess
from PIL import ImageTk,Image  
import ttk
import tkMessageBox


root = Tkinter.Tk()
root.title('AVL Test')
root.iconbitmap('airplane.ico')
root.geometry("900x500")
w = Tkinter.Label(root, text=" AVL Editor",compound = Tkinter.CENTER,font = "Helvetica 50 bold italic",bg="#708090")
w.pack()
root.configure(bg='#708090')
canvas = Canvas(root, width = 300, height = 300)      
canvas.place(x=30,y=100)     
img = ImageTk.PhotoImage(file="airplane.png")      
canvas.create_image(0,0, anchor=NW, image=img)
canvas.configure(bg="#708090")
OPTIONS = [
"Jan",
"Feb",
"Mar"
]
print(avl.Point)

# def SelSurf():
# 	a=[]
# 	for line in fileinput.FileInput(avl_file,inplace=1):
# 		if 'SURFACE' in line:
# 			line = line.next()
# 			a.append(line)
# 			print(line)
# 		else:
# 			print (line)

def open_txt():
	avl_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open Text File", filetypes=(("AVL Files", "*.avl"), ))
	name = avl_file
	# name = name.replace("C:/gui/", "")
	# name = name.replace(".avl", "")
	a=[]
	print("opened: "+avl_file)
	with open(avl_file) as f:
		for line in f:
			if 'SURFACE' in line:
				for i in range(2):
						scale=next(f)
						a.append(scale.rstrip('\n'))
						filtered = [x for x in a if x.strip()]
				print(filtered)
		
	variable = StringVar(root)
	variable.set("Select Surface") 
	w = OptionMenu(root, variable, *filtered)
	w.configure(background="#708090")
	w.place(x=560,y=150)	
	# avl_file = open(avl_file, 'r')
	# content = avl_file.read()
	# for line in content:
    #         for part in line.split():
    #          if "#Xref" in part:
    #             print (part+" and "+part+1)
	#tkMessageBox.showinfo("Message", content)   
	# avl_file.close()

	root.title('{name}')

# def get_Surface():
# 	avl_file = avl_file = filedialog.askopenfilename(initialdir="/Users/carlycuadra/Documents/SeniorProject/Avl/runs/avl_file", title="Open AVL File", filetypes=(("AVL Files", "*.avl"), ))

# 	a=[]
# 	with open(avl_file) as f:
# 		for line in f:
# 			if 'SURFACE' in line:
# 				for i in range(2):
# 						scale=next(f)
# 						a.append(scale.rstrip('\n'))
# 						filtered = [x for x in a if x.strip()]
			

#GUI to change X coordinate of an AVL file
def change_X():
	avl_file = avl_file = filedialog.askopenfilename(initialdir="/Users/carlycuadra/Documents/SeniorProject/Avl/runs/avl_file", title="Open AVL File", filetypes=(("AVL Files", "*.avl"), ))
	x = x_coord.get()
	with open(avl_file) as f:
		for line in fileinput.FileInput(avl_file,inplace=1):
			if 'Xref' in line:
				line = line.split()
				line[0] = x
				new_string = ' '.join(line)
				print(new_string)
			else:
				print (line)
				
	
def change_Y():
	avl_file = avl_file = filedialog.askopenfilename(initialdir="/Users/carlycuadra/Documents/SeniorProject/Avl/runs/avl_file", title="Open AVL File", filetypes=(("AVL Files", "*.avl"), ))
	y = y_coord.get()
	for line in fileinput.FileInput(avl_file,inplace=1):
		if 'Xref' in line:
			line = line.split()
			line[1] = y
			new_string = ' '.join(line)
			print(new_string)
		else:
			print (line)

def change_Z():
	avl_file = avl_file = filedialog.askopenfilename(initialdir="/Users/carlycuadra/Documents/SeniorProject/Avl/runs/avl_file", title="Open AVL File", filetypes=(("AVL Files", "*.avl"), ))
	z = z_coord.get()
	for line in fileinput.FileInput(avl_file,inplace=1):
		if 'Xref' in line:
			line = line.split()
			line[2] = z
			new_string = ' '.join(line)
			print(new_string)
		else:
			print (line)

def change_scale():

	avl_file = avl_file = filedialog.askopenfilename(initialdir="/Users/carlycuadra/Documents/SeniorProject/Avl/runs/avl_file", title="Open AVL File", filetypes=(("AVL Files", "*.avl"), ))
	new_scale=scale.get()

	with open(avl_file) as f:
		for line in f:
			if 'SCALE' in line:
				for i in range(2):
					scale=next(f)
					#print(next(f).rstrip('\n'))
                	print(scale.rstrip('\n'))
  

def change_translate():
	avl_file = avl_file = filedialog.askopenfilename(initialdir="/Users/carlycuadra/Documents/SeniorProject/Avl/runs/avl_file", title="Open AVL File", filetypes=(("AVL Files", "*.avl"), ))
	trans=translate.get()
	with open(avl_file) as f:
		for line in f:
			if 'TRANSLATE' in line:
				for i in range(2):
						print(next(f).strip())

def save_txt():
	avl_file = filedialog.askopenfilename(initialdir="/Users/carlycuadra/Documents/SeniorProject/Avl/runs/avl_file", title="Open AVL File", filetypes=(("AVL Files", "*.avl"), ))
	avl_file = open(avl_file, 'w')
	avl_file.write(my_text.get(1.0, END))
	

def select():


	selected = my_text.selection_get()

	my_label.config(text=selected)
subprocess.Popen([r"/Users/carlycuadra/Documents/SeniorProject/avlwrapper/avl3.35"])

# my_frame = Frame(root)
# my_frame.pack(pady=10)

# Create scrollbar
# text_scroll = Scrollbar(my_frame)
# text_scroll.pack(side=RIGHT, fill=Y)



# my_text = Text(my_frame, width=15, height=15, font=("Helvetica", 16), yscrollcommand=text_scroll.set, undo=True)
# my_text.place(x=50,y=250)
# my_text.pack()

# Configure our scrollbar
# text_scroll.config(command=my_text.yview)


open_button = Button(root, text="Select AVL File", command=open_txt,highlightbackground="#708090")
open_button.pack()
open_button.place(x=575,y=100)

# default value




save_button = Button(root, text="Save AVL File", command=save_txt,highlightbackground="#708090")
save_button.pack()
save_button.place(x=575,y=400)

x_coord = Entry(root, width=5)
x_coord.place(x=450,y=230)

coordinates_button = Button(root, text="Change X coordinate", command=change_X,highlightbackground="#708090")
coordinates_button.pack()
coordinates_button.place(x=400,y=200)


y_coord = Entry(root, width=5)
y_coord.pack()
y_coord.place(x=600,y=230)
coordinates_button = Button(root, text="Change Y coordinate", command=change_Y,highlightbackground="#708090")
coordinates_button.pack()
coordinates_button.place(x=560,y=200)


z_coord=Entry(root,width=5)
z_coord.place(x=760,y=230)

coordinates_button = Button(root, text="Change Z coordinate", command=change_Z,highlightbackground="#708090")
coordinates_button.pack()
coordinates_button.place(x=720,y=200)

scale = Entry(root, width=5)
scale.place(x=565,y=330)
scale_button = Button(root, text="Scale", command=scale,highlightbackground="#708090")
scale_button.pack()
scale_button.place(x=560,y=300)

translate = Entry(root, width=5)
translate.pack()
translate.place(x=645,y=330)
translate_button = Button(root, text="Translate", command=translate,highlightbackground="#708090")
translate_button.pack()
translate_button.place(x=630,y=300)


# select_button = Button(root, text="Select Text", command=select)
# select_button.pack(pady=10)


# my_label = Label(root, text="")
# my_label.pack()


root.mainloop()
