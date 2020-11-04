import Tkinter 
import tkMessageBox
import json
from Tkinter import *
import fileinput
import avlwrapper as avl
from math import radians, sqrt, tan
import subprocess
subprocess.Popen([r"/Users/carlycuadra/Documents/SeniorProject/avlwrapper/avl3.35"])


root = Tkinter.Tk()
root.title('AVL Test')
root.iconbitmap('airplane.ico')
root.geometry("500x650")





def open_txt():
	avl_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open Text File", filetypes=(("AVL Files", "*.avl"), ))
	name = avl_file
	# name = name.replace("C:/gui/", "")
	# name = name.replace(".avl", "")
	
	avl_file = open(avl_file, 'r')
	content = avl_file.read()
    # for line in content:
    #         for part in line.split():
    #          if "#Xref" in part:
    #             print part
    #             print part+1

	my_text.insert(END, content)
	avl_file.close()

	root.title('{name}')

#GUI to change X coordinate of an AVL file
def change_X():
	avl_file = avl_file = filedialog.askopenfilename(initialdir="/Users/carlycuadra/Documents/SeniorProject/Avl/runs/avl_file", title="Open AVL File", filetypes=(("AVL Files", "*.avl"), ))
	x = x_coord.get()
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


def save_txt():
	avl_file = filedialog.askopenfilename(initialdir="/Users/carlycuadra/Documents/SeniorProject/Avl/runs/avl_file", title="Open AVL File", filetypes=(("AVL Files", "*.avl"), ))
	avl_file = open(avl_file, 'w')
	avl_file.write(my_text.get(1.0, END))

def select():
   
	selected = my_text.selection_get()

	my_label.config(text=selected)


my_frame = Frame(root)
my_frame.pack(pady=10)

# Create scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

my_text = Text(my_frame, width=46, height=15, font=("Helvetica", 16), yscrollcommand=text_scroll.set, undo=True)
my_text.pack()

# Configure our scrollbar
text_scroll.config(command=my_text.yview)


open_button = Button(root, text="Open AVL File", command=open_txt)
open_button.pack(pady=10)

save_button = Button(root, text="Save File Changes", command=save_txt)
save_button.pack(pady=10)

x_coord = Entry(root, width=5)
x_coord.pack()
coordinates_button = Button(root, text="Change X coordinate", command=change_X)
coordinates_button.pack(pady=5)

y_coord = Entry(root, width=5)
y_coord.pack()
coordinates_button = Button(root, text="Change Y coordinate", command=change_Y)
coordinates_button.pack(pady=5)

z_coord = Entry(root, width=5)
z_coord.pack()
coordinates_button = Button(root, text="Change Z coordinate", command=change_Z)
coordinates_button.pack(pady=5)

select_button = Button(root, text="Select Text", command=select)
select_button.pack(pady=10)


my_label = Label(root, text="")
my_label.pack()

root.mainloop()
