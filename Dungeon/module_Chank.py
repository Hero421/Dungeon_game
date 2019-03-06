from Blocks.module_GameNone import GameNone

class Chank(object):

	def __init__(self, row, elm, num=10):   # number of rows and elms

		self.row = row
		self.elm = elm
		self.num = num

		self.strt_row = row*num
		self.strt_elm = elm*num

		self.fin_row = self.strt_row + num
		self.fin_elm = self.strt_elm + num

		from module_links import ses_area

		for row in range(-1, self.fin_row - self.strt_row - 1):
			for elm in range(-1, self.fin_elm - self.strt_elm - 1):
				ses_area.map[self.strt_row + row][self.strt_elm + elm] = GameNone()

	def generator(self, map_):

		for row in range(self.strt_row, self.fin_row):
			for elm in range(self.strt_elm, self.fin_elm):
				if type(map_[row][elm]) is GameNone:
					map_[row][elm].act(row, elm)

	def msg(self, avatar):
		
		try:
			avatar.area.chank_map[self.row - 1][self.elm].generator(avatar.map)
		except IndexError:
			pass
		
		try:
			avatar.area.chank_map[self.row - 1][self.elm + 1].generator(avatar.map)
		except IndexError:
			pass
			
		try:
			avatar.area.chank_map[self.row][self.elm + 1].generator(avatar.map)
		except IndexError:
			pass
		
		try:
			avatar.area.chank_map[self.row + 1][self.elm + 1].generator(avatar.map)
		except IndexError:
			pass
			
		try:
			avatar.area.chank_map[self.row + 1][self.elm].generator(avatar.map)
		except IndexError:
			pass
		
		try:
			avatar.area.chank_map[self.row + 1][self.elm - 1].generator(avatar.map)
		except IndexError:
			pass
			
		try:
			avatar.area.chank_map[self.row][self.elm - 1].generator(avatar.map)
		except IndexError:
			pass
			
		try:
			avatar.area.chank_map[self.row - 1][self.elm - 1].generator(avatar.map)
		except IndexError:
			pass