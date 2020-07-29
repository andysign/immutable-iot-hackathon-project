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
print("getCtVersion", w3.getCtVersion())

# TkinterStuff
wh = "480x320"
w = int(wh.split("x")[0])
h = int(wh.split("x")[1])
if w3.getPiNumber() == 1:
	bg_colors = [ "#eaeaea", "#aeaeae", "#c00000" ]
	lbl_names = [ "Self", "B", "C" ]
elif w3.getPiNumber() == 2:
	bg_colors = [ "#c00000", "#aeaeae", "#eaeaea" ]
	lbl_names = [ "Self", "A", "C" ]
else:
	bg_colors = [ "#aeaeae", "#eaeaea", "#c00000" ]
	lbl_names = [ "Self", "A", "B" ]

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

		t1 = Text(main_frame, width=14, height=1, font=("Courier",13))
		t1.tag_configure("center", justify='center')
		t1.insert("1.0", "NODE STATS: ")
		t1.tag_add("center", "1.0", "end")
		t1.config(state=DISABLED)
		t1.pack()
		t1.place(x=6, y=16)

		t2 = Text(main_frame, width=13, height=1, font=("Courier",9))
		t2.tag_configure("center", justify='left')
		t2.insert("1.0", "Block Height:")
		t2.tag_add("center", "1.0", "end")
		t2.config(state=DISABLED)
		t2.pack()
		t2.place(x=6, y=48)

		self.blk_height_lbl = Label(bg="#777",fg="#aff",font=("Courier",9))
		self.blk_height_lbl.place(x=92, y=48)

		t3 = Text(main_frame, width=13, height=1, font=("Courier",9))
		t3.tag_configure("center", justify='left')
		t3.insert("1.0", "LastBlkTime:")
		t3.tag_add("center", "1.0", "end")
		t3.config(state=DISABLED)
		t3.pack()
		t3.place(x=6, y=68)

		self.blk_time_lbl = Label(bg="#777",fg="#aff",font=("Courier",9))
		self.blk_time_lbl.place(x=92, y=68)

		t4 = Text(main_frame, width=14, height=1, font=("Courier",13))
		t4.tag_configure("center", justify='center')
		t4.insert("1.0", "SMART CT STATS: ")
		t4.tag_add("center", "1.0", "end")
		t4.config(state=DISABLED)
		t4.pack()
		t4.place(x=6, y=96)

		t5 = Text(main_frame, width=13, height=1, font=("Courier",9))
		t5.tag_configure("center", justify='left')
		t5.insert("1.0", "AverageMVal:")
		t5.tag_add("center", "1.0", "end")
		t5.config(state=DISABLED)
		t5.pack()
		t5.place(x=6, y=128)

		self.ct_average_lbl = Label(bg="#777",fg="#aff",font=("Courier",9))
		self.ct_average_lbl.place(x=92, y=128)

		t6 = Text(main_frame, width=15, height=1, font=("Courier",13))
		t6.tag_configure("center", justify='center')
		t6.insert("1.0", "FakeValREADING")
		t6.tag_add("center", "1.0", "end")
		t6.config(state=DISABLED)
		t6.pack()
		t6.place(x=6, y=154)

		b1 = Button(main_frame, width=3, text="0 ", fg="black")
		b1.place(x=6, y=178)


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
		ct_average = w3.getMeasureAverage()
		self.ct_average_lbl.configure(text=ct_average)
		self.after(1000, self.update_display)

win = Tk() # win.update_idletasks()
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
