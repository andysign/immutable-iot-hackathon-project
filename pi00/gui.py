#!/usr/bin/python
# from tkinter import * 			# imports the Tkinter lib
# root = Tk()				# create the root object
# root.wm_title("Hello World")		# sets title of the window
# root.geometry("480x320")
# root.mainloop()				# starts the GUI loop

import middleware
from web3 import Web3
from tkinter import *
import time

# Web3Stuff
web3 = Web3()
if not web3.isConnected():
	exit("Error, Web3 doesn't work.")

w3 = middleware.W3(web3)
print("version", w3.version())
filter = w3.createBlockFilter()
print("getPiNumber", w3.getPiNumber())
print("getContractVersion", w3.getContractVersion())

# TkinterStuff
wh = "480x320"
w = int(wh.split("x")[0])
h = int(wh.split("x")[1])
if w3.getPiNumber() == 1:
	bg_colors = [ "#eaeaea", "#aeaeae", "#c00000" ]
elif w3.getPiNumber() == 2:
	bg_colors = [ "#c00000", "#aeaeae", "#eaeaea" ]
else:
	bg_colors = [ "#aeaeae", "#eaeaea", "#c00000" ]

class App(Frame):
	def __init__(self,master=None):
		Frame.__init__(self, master)
		self.master = master
		self.state = False
		self.master.attributes('-fullscreen', False)
		self.pack(fill=BOTH, expand=1)
		main_frame =   Frame(
			self, background=bg_colors[0], width=160, height=h
		).grid(row=0, column=0, sticky="nsew")
		middle_frame = Frame(
			self, background=bg_colors[1], width=160, height=h
		).grid(row=0, column=1, sticky="nsew")
		last_frame =   Frame(
			self, background=bg_colors[2], width=160, height=h
		).grid(row=0, column=2, sticky="nsew")
		Button(self,text="FullScr",command=self.fs_toggle).place(x=410, y=0)
		self.master.bind("<Escape>", self.fs_toggle)

		t1 = Text(main_frame, width=17, height=1, font=("Courier",13))
		t1.tag_configure("center", justify='center')
		t1.insert("1.0", "NODE STATS: ")
		t1.tag_add("center", "1.0", "end")
		t1.pack()
		t1.place(x=6, y=16)

		t2 = Text(main_frame, width=13, height=1, font=("Courier",9))
		t2.tag_configure("center", justify='left')
		t2.insert("1.0", "Block Height:")
		t2.tag_add("center", "1.0", "end")
		t2.pack()
		t2.place(x=6, y=48)

		self.blk_height_lbl = Label(bg="#777",fg="#aff",font=("Courier",9))
		self.blk_height_lbl.place(x=92, y=48)

		t3 = Text(main_frame, width=13, height=1, font=("Courier",9))
		t3.tag_configure("center", justify='left')
		t3.insert("1.0", "LastBlkTime:")
		t3.tag_add("center", "1.0", "end")
		t3.pack()
		t3.place(x=6, y=68)

		self.blk_time_lbl = Label(bg="#777",fg="#aff",font=("Courier",9))
		self.blk_time_lbl.place(x=92, y=68)

		t4 = Text(main_frame, width=17, height=1, font=("Courier",13))
		t4.tag_configure("center", justify='center')
		t4.insert("1.0", "SMART CT STATS: ")
		t4.tag_add("center", "1.0", "end")
		t4.pack()
		t4.place(x=6, y=96)

		t3 = Text(main_frame, width=19, height=1, font=("Courier",9))
		t3.tag_configure("center", justify='left')
		t3.insert("1.0", "AverageMeasurement:")
		t3.tag_add("center", "1.0", "end")
		t3.pack()
		t3.place(x=6, y=128)


		# T1.insert("1.0", "text")
		# T1.tag_add("center", "1.0", "end")
		# T1.pack()
		self.update_display()


	def fs_toggle(self, event=None):
		self.state = not self.state  # Just toggling the boolean
		self.master.attributes("-fullscreen", self.state)
		return "break"

	def update_display(self):
		blk_num = w3.getBlockNumber()
		self.blk_height_lbl.configure(text=blk_num)
		blk_timestamp = w3.getLatestBlockTimestamp()
		blk_timestamp = time.ctime(blk_timestamp)
		blk_timestamp = blk_timestamp.split(" ")[3]
		self.blk_time_lbl.configure(text=blk_timestamp)
		self.after(1000, self.update_display)

win = Tk()
# win.update_idletasks()
win.wm_title("GethNodeGUI")
win.geometry(wh)
x = (win.winfo_screenwidth() // 2) - (w // 2)
y = (win.winfo_screenheight()// 2) - (h // 2)
win.geometry('{}x{}+{}+{}'.format(w, h, x, y)) # win.resizable(False, False)
# win.grid_columnconfigure(0, weight=1)
# win.grid_columnconfigure(1, weight=1)
# win.grid_columnconfigure(2, weight=1)
app = App(win)
win.after(1000, app.update_display)
win.mainloop()

# for i in range(30):
# 	time.sleep(1)
# 	new_blocks = filter.get_new_entries()
# 	if len(new_blocks)>0:
# 		print("NewBlock")
# 		print(w3.getBlockNumber())

# window = Tk()
# window.wm_title("GethNodeGUI")
# window.geometry("480x320")

# root.attributes("-fullscreen", True) 	# set to fullscreen

# from tkinter import *
#
# from tkinter import *
#
# class Window(Frame):
#
# 	def __init__(self, master=None):
# 		Frame.__init__(self, master)
# 		self.master = master
#
# 		# widget can take all window
# 		self.pack(fill=BOTH, expand=1)
#
# 		text = Label(self, text="Just do it")
# 		text.place(x=70,y=90)
#
# 		# create button, link it to clickExitButton()
# 		#exitButton = Button(self, text="Exit", command=self.clickExitButton)
#
# 		# place button at (0,0)
# 		#exitButton.place(x=0, y=0)
#
# 	def clickExitButton(self):
# 		exit()
#
# root = Tk()
# app = Window(root)
# root.wm_title("Tkinter button")
# root.geometry("480x320")
# root.mainloop()
