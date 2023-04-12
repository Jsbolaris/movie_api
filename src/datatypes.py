from dataclasses import dataclass
# TODO: Remove lists!
@dataclass
class Character:
	id:       int
	name:     str
	movie_id: int
	gender:   str
	age:      int
	#conversations: list
	#lines: list
	num_lines: int

@dataclass
class Movie:
	id: int
	title: str
	year: int
	imdb_rating: float
	imdb_votes: int
	raw_script_url: str
	#characters: list
	#conversations: list
	#lines: list

@dataclass
class Conversation:
	id: int
	c1_id: int
	c2_id: int
	movie_id: int
	num_lines: int
	#lines: list

@dataclass
class Line:
	id: int
	c_id: int
	movie_id: int
	conv_id: int
	line_sort: int
	line_text: str