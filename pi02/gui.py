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
	lbl_names = [ "Self", "A", "C" ]
elif w3.getPiNumber() == 2:
	bg_colors = [ "#c00000", "#aeaeae", "#eaeaea" ]
	lbl_names = [ "Self", "A", "B" ]
else:
	bg_colors = [ "#aeaeae", "#eaeaea", "#c00000" ]
	lbl_names = [ "Self", "B", "C" ]

class App(Frame):
	def __init__(self,master=None):
		Frame.__init__(self, master)
		self.master = master
		self.fs_state = False
		self.last_val = 0
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
		Button(
			text="FullScr",command=self.fs_toggle,height=1,font=("Courier",9)
		).place(x=415, y=0)
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

		t6 = Text(main_frame, width=13, height=1, font=("Courier",9))
		t6.tag_configure("center", justify='left')
		t6.insert("1.0", "LastVal:")
		t6.tag_add("center", "1.0", "end")
		t6.config(state=DISABLED)
		t6.pack()
		t6.place(x=6, y=184)

		self.last_val_lbl = Label(bg="#777",fg="#aff",font=("Courier",9))
		self.last_val_lbl.place(x=92, y=184)

		b1 = Button(width=2, text="0 ", command=lambda:self.ct_set(0))
		b1.place(x=6, y=212)
		b2 = Button(width=2, text="5 ", command=lambda:self.ct_set(5))
		b2.place(x=56, y=212)
		b3 = Button(width=2, text="10", command=lambda:self.ct_set(10))
		b3.place(x=106, y=212)
		b4 = Button(width=2, text="15", command=lambda:self.ct_set(15))
		b4.place(x=6, y=244)
		b5 = Button(width=2, text="20", command=lambda:self.ct_set(20))
		b5.place(x=56, y=244)
		b6 = Button(width=2, text="25", command=lambda:self.ct_set(25))
		b6.place(x=106, y=244)
		b7 = Button(width=2, text="30", command=lambda:self.ct_set(30))
		b7.place(x=6, y=276)
		b8 = Button(width=2, text="35", command=lambda:self.ct_set(35))
		b8.place(x=56, y=276)
		b9 = Button(width=2,text="∞",bg='red',command=lambda:self.ct_set(1000))
		b9.place(x=106, y=276)

		t7 = Text(main_frame, width=14, height=1, font=("Courier",13))
		t7.tag_configure("center", justify='center')
		t7.insert("1.0", "NODE "+lbl_names[1]+" STATS:")
		t7.tag_add("center", "1.0", "end")
		t7.config(state=DISABLED)
		t7.pack()
		t7.place(x=166, y=16)

		t8 = Text(main_frame, width=13, height=1, font=("Courier",9))
		t8.tag_configure("center", justify='left')
		t8.insert("1.0", "measurement"+lbl_names[1]+":")
		t8.tag_add("center", "1.0", "end")
		t8.config(state=DISABLED)
		t8.pack()
		t8.place(x=166, y=154)

		self.last_middle_lbl = Label(bg="#777",fg="#aff",font=("Courier",9))
		self.last_middle_lbl.place(x=256, y=154)

		t9 = Text(main_frame, width=14, height=1, font=("Courier",13))
		t9.tag_configure("center", justify='center')
		t9.insert("1.0", ""+lbl_names[2]+" STATS:")
		t9.tag_add("center", "1.0", "end")
		t9.config(state=DISABLED)
		t9.pack()
		t9.place(x=326, y=16)

		t0 = Text(main_frame, width=13, height=1, font=("Courier",9))
		t0.tag_configure("center", justify='left')
		t0.insert("1.0", "measurement"+lbl_names[2]+":")
		t0.tag_add("center", "1.0", "end")
		t0.config(state=DISABLED)
		t0.pack()
		t0.place(x=326, y=154)

		self.last_right_lbl = Label(bg="#777",fg="#aff",font=("Courier",9))
		self.last_right_lbl.place(x=416, y=154)



		self.update_display()


	def fs_toggle(self, event=None):
		self.fs_state = not self.fs_state  # Just toggling the boolean
		self.master.attributes("-fullscreen", self.fs_state)
		return "break"

	def ct_set(self, v):
		self.last_val = v
		w3.setFakeReading(v)
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
		self.last_val_lbl.configure(text=self.last_val)
		last_middle = w3.getOtherMeasurement(lbl_names[1])
		self.last_middle_lbl.configure(text=last_middle)
		last_right = w3.getOtherMeasurement(lbl_names[2])
		self.last_right_lbl.configure(text=last_middle)
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
