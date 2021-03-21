import tkinter as tk
from tkinter import font


class InputLabel(tk.Label):
	def __init__(self, master=None, title="Application"):
		super().__init__(master=master, relief='ridge', takefocus=1, anchor=tk.W)
		self.master.title(title)
		self.master.minsize(width=200, height=50)

		self.text = tk.StringVar()
		self.font = font.Font(font='Terminus', size=10, weight='normal')
		self.font_size = self.font.measure('a')
		self.config(font=self.font, textvariable=self.text)
		self.grid(sticky=tk.EW)

		self.create_widgets()

		self.master.columnconfigure(0, weight=1)
		self.master.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)
		self.rowconfigure(0, weight=1)

	def create_widgets(self):
		self.quit_button = tk.Button(self.master, text='Exit', command=self.quit)
		self.quit_button.grid(row=1, column=0, sticky=tk.SE)

		self.bind('<Any-KeyPress>', self._process_key)
		self.bind('<Button-1>', self._process_mouse_click)

		self.cursor = tk.Frame(self, height=18, width=1, bg='black')
		self.cursor.place(x=0)
		self.pos = 0
		self.focus()

	def _process_key(self, event):
		if event.keysym == 'Home':
			self.pos = 0
		elif event.keysym == 'End':
			self.pos = len(self.text.get())
		elif event.keysym == 'Left':
			self.pos = max(0, self.pos - 1)
		elif event.keysym == 'Right':
			self.pos = min(len(self.text.get()), self.pos + 1)
		elif event.keysym == 'BackSpace':
			string = self.text.get()
			new_pos = max(0, self.pos - 1)
			self.text.set(string[:new_pos] + string[self.pos:])
			self.pos = new_pos
		elif event.char.isprintable() and len(event.char) > 0:
			string = self.text.get()
			self.text.set(string[:self.pos] + event.char + string[self.pos:])
			self.pos += 1
		self._update_cursor()

	def _update_cursor(self):
		x = self.font.measure(self.text.get()[:self.pos])
		self.cursor.place(x=x)

	def _process_mouse_click(self, event):
		self.focus()
		self.pos = min(len(self.text.get()), max(0, event.x // self.font_size))
		self._update_cursor()


if __name__ == '__main__':
	app = InputLabel(title="Label Editor")
	app.mainloop()
