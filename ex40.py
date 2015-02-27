# Modules, Classes, and Objects, 

# __init__ is instantiation, Python builds an empty object
# and imports the functions specified in the class

class Song(object):
	def __init__(self, lyrics, tune):
		self.lyrics = lyrics
		self.tune = tune

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

	def play_the_tune(self):
		print self.tune

happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"],"tune")

bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"],"tune")

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

my_lyrics = ["Oh, oh, oh, ohuhoh"]

my_song = Song(my_lyrics, "tune")

my_song.sing_me_a_song()
my_song.play_the_tune()

q


