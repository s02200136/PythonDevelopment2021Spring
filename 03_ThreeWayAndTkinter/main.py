import tkinter as tk
from random import shuffle
from tkinter import messagebox


class Application(tk.Frame):
	def __init__(self, master=None, title="<application>", **kwargs):
		super().__init__(master, **kwargs)
		self.master.title(title)
		self.master.columnconfigure(0, weight=1)
		self.master.rowconfigure(0, weight=1)
		self.master.minsize(width=200, height=200)
		self.create_widgets()
		self.grid(sticky=tk.NSEW)

	@staticmethod
	def is_solvable(nums):
		wrong_sum = 0
		for i in range(16):
			for j in range(i + 1, 16):
				if nums[i] == 0:
					wrong_sum += i // 4 + 1
				if nums[j] != 0 and nums[i] > nums[j]:
					wrong_sum += 1
		return wrong_sum % 2 == 0

	def _create_buttons(self):
		for i in range(4):
			for j in range(4):
				if self.play_grid[i][j] != 0:
					button = tk.Button(self.numbers, bg='green yellow', text=str(self.play_grid[i][j]), relief="ridge",
									   width=2, height=1)
					button.configure(command=lambda obj=button: self._move(obj))
					button.grid(row=i, column=j, sticky=tk.NSEW)
					self.number_buttons.append(button)

	def _generate_new_task(self):
		if not len(self.number_buttons) == 0:
			for button in self.number_buttons:
				button.destroy()
		nums = list(range(16))
		shuffle(nums)

		while not self.is_solvable(nums):
			shuffle(nums)
		self.play_grid = [[nums[x * 4 + y] for y in range(4)] for x in range(4)]
		self._create_buttons()

	def _check(self):
		for i in range(1, 16):
			if not self.play_grid[(i - 1) // 4][(i - 1) % 4] == i:
				return False
		return True

	def _move(self, button):
		y = button.grid_info()['column']
		x = button.grid_info()['row']
		if y > 0:
			if self.play_grid[x][y - 1] == 0:
				self.play_grid[x][y - 1] = self.play_grid[x][y]
				self.play_grid[x][y] = 0
				button.grid(column=y - 1, row=x)
		if y < 3:
			if self.play_grid[x][y + 1] == 0:
				self.play_grid[x][y + 1] = self.play_grid[x][y]
				self.play_grid[x][y] = 0
				button.grid(column=y + 1, row=x)
		if x > 0:
			if self.play_grid[x - 1][y] == 0:
				self.play_grid[x - 1][y] = self.play_grid[x][y]
				self.play_grid[x][y] = 0
				button.grid(column=y, row=x - 1)
		if x < 3:
			if self.play_grid[x + 1][y] == 0:
				self.play_grid[x + 1][y] = self.play_grid[x][y]
				self.play_grid[x][y] = 0
				button.grid(column=y, row=x + 1)

		if self._check():
			messagebox.showinfo('You Won!', message='Congratulations!')
			self._generate_new_task()

	def create_widgets(self):
		self.comands = tk.Frame(self, bg='orange', borderwidth=5, relief="ridge", width=200, height=100)
		self.comands.grid(row=0, column=0, sticky=tk.NSEW)

		self.numbers = tk.Frame(self, bg='black', borderwidth=5)
		self.numbers.grid(row=1, column=0, sticky=tk.NSEW)
		self.number_buttons = []

		self.newButton = tk.Button(self.comands, text='New', command=self._generate_new_task)
		self.newButton.grid(row=0, column=0)

		self.quitButton = tk.Button(self.comands, text='Quit', command=self.quit)
		self.quitButton.grid(row=0, column=1)

		self._generate_new_task()

		self.comands.columnconfigure(0, weight=1)
		self.comands.columnconfigure(1, weight=1)
		self.comands.rowconfigure(0, weight=1)

		self.rowconfigure(1, weight=1)
		self.columnconfigure(0, weight=1)

		for i in range(4):
			self.numbers.columnconfigure(i, weight=1)
			self.numbers.rowconfigure(i, weight=1)


if __name__ == '__main__':
	app = Application(title="15")
	app.mainloop()
