import tkinter
N = 4

maze = [ 	[2, 0, 1, 1],
			[1, 0, 1, 3],
			[1, 1, 1, 0],
			[1, 0, 1, 0] ]

sol = [ 	[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0] ]

def showOff(a, b, c, d):
	top = tkinter.Tk()
	top.geometry("580x500")


	rect = [[], [], [], []]
	label = [[], [], [], []]

	solColor = "lightblue"
	routeColor = "white"
	wallColor = "blue"

	for i in range(N):
		for j in range(N):
			rect[i].append(tkinter.Frame(top, relief=tkinter.RAISED, borderwidth=0))
			rect[i][j].grid(row=i, column=j, padx=0, pady=0)
			if maze[i][j] == 0:
				label[i].append(tkinter.Label(rect[i][j], text="" , bg=wallColor, width=20, height=8))
			if maze[i][j] == 1:
				if sol[i][j] == 1:
					if i == a and j == b:
						label[i].append(tkinter.Label(rect[i][j], text="START" , bg=solColor, width=20, height=8))
					elif i == c and j == d:
						label[i].append(tkinter.Label(rect[i][j], text="FINISH" , bg=solColor, width=20, height=8))
					else:
						label[i].append(tkinter.Label(rect[i][j], text="" , bg=solColor, width=20, height=8))
				else :
					if i == a and j == b:
						label[i].append(tkinter.Label(rect[i][j], text="START" , bg=routeColor, width=20, height=8))
					elif i == c and j == d:
						label[i].append(tkinter.Label(rect[i][j], text="FINISH" , bg=routeColor, width=20, height=8))
					else:
						label[i].append(tkinter.Label(rect[i][j], text="" , bg=routeColor, width=20, height=8))
	for i in range(N):
		for j in range(N):
			label[i][j].pack()

	top.mainloop()

def printMaze( maze ):
	
	for i in maze:
		for j in i:
			print(str(j) + " ", end ="")
		print("")

def printSolution( sol ):
	
	for i in sol:
		for j in i:
			print(str(j) + " ", end ="")
		print("")

def isSafe( maze, x, y ):
	
	if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
		return True
	
	return False


def solveMaze( maze, a, b, c, d ):
	
	if solveMazeUtil(maze, a, b, c, d, sol) == False:
		print("Solution doesn't exist");
		return False

	return True
	
def solveMazeUtil(maze, x, y, m, n, sol):
	
	if x == m and y == n and maze[x][y] == 1:
		sol[x][y] = 1
		return True
	
	if isSafe(maze, x, y) == True:
		if sol[x][y] == 1:
			return False
		
		sol[x][y] = 1
		
		if solveMazeUtil(maze, x + 1, y, m, n, sol) == True:
			return True

		if solveMazeUtil(maze, x, y + 1, m, n, sol) == True:
			return True
		
		if solveMazeUtil(maze, x - 1, y, m, n, sol) == True:
			return True
			
		if solveMazeUtil(maze, x, y - 1, m, n, sol) == True:
			return True
		
		sol[x][y] = 0
		return False

if __name__ == "__main__":
	a = 0
	b = 0
	c = 0
	d = 0

	for i in range(N):
		for j in range(N):
			if maze[i][j] == 2:
				maze[i][j] = 1
				a = i
				b = j

			if maze[i][j] == 3:
				maze[i][j] = 1
				c = i
				d = j
			
	solveMaze(maze, a, b, c, d)
	printMaze(maze)
	print()
	printSolution(sol)
	showOff(a, b, c, d)