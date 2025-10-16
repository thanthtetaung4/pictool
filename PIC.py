class PIC:
	infile: str
	outfile: str
	flag: str
	width: int
	height: int

	def __init__(self, mode, *args):
		data = args[0]
		if (mode == -1):
			raise Exception("Invalid mode")
		self.mode = mode
		self.infile = data[0]
		self.flag = data[1]
		if (self.mode == 1):
			self.width = int(data[2])
			self.height = int(data[3])
			self.outfile = data[4]
		elif (self.mode == 2):
			self.width = 0
			self.height = 0
			self.outfile = data[2]

	def __str__(self):
		return(f"infile : {self.infile}\n\
				outfile : {self.outfile}\n\
				flag : {self.flag}\n\
				width : {self.width}\n\
				height : {self.height}\n")