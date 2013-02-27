class BowlingGame(object):
	"""docstring for BowlingGame"""
	def __init__(self, arg):
		super(BowlingGame, self).__init__()
		self.arg = arg

	def Roll(score):
		pass

	def Score():
		return 0

	def AllRollScore(self,rolls):
		sum = 0
		for x in rolls:
			sum += x
		i = 0
		frame = -1
		print "len %d" % len(rolls)
		while (i<len(rolls)) :
			frame += 1
			print "frame %d, score %d" %(frame, sum)
			if (rolls[i] == 10) : # STRIKE
				print "STRIKE at frame %d" % frame
				if (frame < 9) :
					sum += rolls[i+1] + rolls[i+2]
				##elif (frame == 10) :
				##	print "frame====>"
				##	sum += rolls[i+1]
				i += 1
				continue
			print "roll %d" % i
			# SPARE
			if (frame < 10) :
				framescore = rolls[i] + rolls[i+1]
				if (framescore > 10) : # invalid score
					return -1
				if (framescore == 10) :
						sum += rolls[i+3]
			i += 2
		return sum

def main():
	b = BowlingGame(None)
	print "hello world"
	score = b.AllRollScore((1,1,
					1,1,
					1,1,
					1,1,
					1,1,
					1,1,
					1,1,
					1,1,
					1,1,
					1,1,
					))
	print "expected %d, actual %d" % (20, score)
	print "================================="
	score = b.AllRollScore((10,
					10,
					10,
					10,
					10,
					10,
					10,
					10,
					10,
					10,
					10,
					10,
					))
	print "expected %d, actual %d" % (300, score)

if __name__ == '__main__':
	main()