import tkinter as gui

N = 12

jalur = [	[0,1,1,1,0,1,0,1,1,1,1,1],
			[0,1,0,0,0,1,0,1,0,0,1,0],
			[0,1,0,1,1,1,0,1,1,0,1,1],
			[0,1,1,1,0,1,0,0,0,0,1,0],
			[0,1,0,0,0,1,0,1,1,1,1,1],
			[0,2,1,1,1,1,0,0,0,1,1,0],
			[0,1,0,0,1,1,1,1,1,1,1,1],
			[0,1,0,1,1,1,0,1,1,1,1,0],
			[0,1,0,1,0,1,0,0,1,0,0,0],
			[0,1,0,1,0,1,1,0,1,1,1,1],
			[0,0,0,1,0,1,1,0,1,0,1,1],
			[1,1,1,1,0,1,1,0,1,0,1,3]	]

solusi = [	[0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0]	]

def tampilKOTAK(a, b, c, d):
	wadah = gui.Tk()
	wadah.geometry("575x610")
	
	kotak = [[],[],[],[],[],[],[],[],[],[],[],[]]
	label = [[],[],[],[],[],[],[],[],[],[],[],[]]

	jalan = "LimeGreen"
	tembok = "ForestGreen"
	arah = "SpringGreen"
	tulisan = "DarkGreen"
	panjang = 6
	lebar = 3
	mulai = "START"
	selesai = "FINISH"

	for i in range(N):
		for j in range(N):
			kotak[i].append(gui.Frame(wadah, relief=gui.RAISED, borderwidth=0))
			kotak[i][j].grid(row=i, column=j, padx=0, pady=0)
			if jalur[i][j] == 1:
				if i == a and j == b:
					if solusi[i][j] == 1:
						label[i].append(gui.Label(kotak[i][j], text=mulai, fg=tulisan, bg=arah, width=panjang, height=lebar))
					if solusi[i][j] == 0:
						label[i].append(gui.Label(kotak[i][j], text=mulai, fg=tulisan, bg=jalan, width=panjang, height=lebar))
				elif i == c and j == d:
					if solusi[i][j] == 1:
						label[i].append(gui.Label(kotak[i][j], text=selesai, fg=tulisan, bg=arah, width=panjang, height=lebar))
					if solusi[i][j] == 0:
						label[i].append(gui.Label(kotak[i][j], text=selesai, fg=tulisan, bg=jalan, width=panjang, height=lebar))
				else :
					if solusi[i][j] == 1:
						label[i].append(gui.Label(kotak[i][j], text="", fg=tulisan, bg=arah, width=panjang, height=lebar))
					if solusi[i][j] == 0:
						label[i].append(gui.Label(kotak[i][j], text="", fg=tulisan, bg=jalan, width=panjang, height=lebar))
			if jalur[i][j] == 0:
				label[i].append(gui.Label(kotak[i][j], text="", fg=tulisan, bg=tembok, width=panjang, height=lebar))

	for i in range(N):
		for j in range(N):
			label[i][j].pack()

	wadah.mainloop()

if __name__ == '__main__':
	a = 0
	b = 0
	c = 0
	d = 0

	for i in range(N):
		for j in range(N):
			if jalur[i][j] == 2:
				jalur[i][j] = 1
				a = i
				b = j
			if jalur[i][j] == 3:
				jalur[i][j] = 1
				c = i
				d = j

	tampilKOTAK(a, b, c, d)