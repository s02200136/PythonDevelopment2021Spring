import tkinter as tk


class Application(tk.Frame):
	def __init__(self, master=None, title="<application>", **kwargs):
		super().__init__(master, **kwargs)
		self.master.title(title)
		self.master.columnconfigure(0, weight=1)
		self.master.rowconfigure(0, weight=1)
		self.master.minsize(width=200, height=200)
		self.create_widgets()
		self.grid(sticky=tk.NSEW)

	def _generate_new_task(self):
		pass

	def create_widgets(self):
		self.comands = tk.Frame(self, bg='orange', borderwidth=5, relief="ridge", width=200, height=100)
		self.comands.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW)

		self.numbers = tk.Frame(self, bg='black', borderwidth=5)
		self.numbers.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW)
		self.number_buttons = []

		self.newButton = tk.Button(self.comands, text='New', command=self._generate_new_task)
		self.newButton.grid(row=0, column=0)

		self.quitButton = tk.Button(self.comands, text='Quit', command=self.quit)
		self.quitButton.grid(row=0, column=1)

		self.comands.columnconfigure(0, weight=1)
		self.comands.columnconfigure(1, weight=1)
		self.comands.rowconfigure(0, weight=1)

		self.columnconfigure(1, weight=1)
		self.rowconfigure(1, weight=1)
		for i in range(4):
			self.numbers.columnconfigure(i, weight=1)
			self.numbers.rowconfigure(i, weight=1)

		self.pack(fill=tk.BOTH)


if __name__ == '__main__':
	app = Application(title="15")
	app.mainloop()
