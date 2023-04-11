import csv


# TODO: You will want to replace all of the code below. It is just to show you
# an example of reading the CSV files where you will get the data to complete
# the assignment.

# print("reading movies")


# define all objects

# character object
# name and gender can be null
class character:
    def __init__(self, character_id: int, name: str, movie_id: int, gender: str, age: int):
        self.character_id = character_id
        self.name = (name or None)
        self.movie_id = movie_id
        self.gender = (gender or None)
        self.age = age
        self.lineCount = 0


# define movie object
class movie:
    def __init__(self, movie_id: int, title: str, year: str, imdb_rating: float, imdb_votes: int, raw_script_url: str):
        self.movie_id = movie_id
        self.title = title
        self.year = year
        self.imdb_rating = imdb_rating
        self.imdb_votes = imdb_votes
        self.raw_script_url = raw_script_url


# define line object
class line:
    def __init__(self, line_id: int, character_id: int, movie_id: int, conversation_id: int,
                 line_sort: int, line_text: str):
        self.line_id = line_id
        self.character_id = character_id
        self.movie_id = movie_id
        self.conversation_id = conversation_id
        self.line_sort = line_sort
        self.line_text = line_text


# define conversation object
class conversation:
    def __init__(self, conversation_id: int, character1_id: int, character2_id: int, movie_id: int):
        self.numOfLines = 0
        self.conversation_id = conversation_id
        self.character1_id = character1_id
        self.character2_id = character2_id
        self.movie_id = movie_id


# define database with all the information
# fill a dictionary with the information for each relation
class database:
    conversations = {}
    with open("conversation.csv", mode="r", encoding="utf8") as csv_file:
        for row in csv.DictReader(csv_file, skipinitialspace=True):
            curr_conversation = conversation(int(row['conversation_id']), int(row['character1_id']),
                                             int(row['character2_id']), int(row['movie_id']))
        conversations[curr_conversation.conversation_id] = curr_conversation

    characters = {}  # empty character list
    with open("characters.csv", mode="r", encoding="utf8") as csv_file:
        for row in csv.DictReader(csv_file, skipinitialspace=True):
            curr_char = character(int(row['character_id']), str(row['name']), int(row['movie_id']), str(row['gender']),
                                  int(row['age']))
            characters[curr_char.character_id] = curr_char

    movies = {}  # empty movie list
    with open("movie.csv", mode="r", encoding="utf8") as csv_file:
        for row in csv.DictReader(csv_file, skipinitialspace=True):
            curr_movie = movie(int(row['movie_id']), str(row['title']), int(row['year']), float(row['imdb_rating']),
                               int(row['imdb_votes']), str(row['raw_script_url']))
            movies[curr_movie.movie_id] = curr_movie

    lines = {}
    with open("lines.csv", mode="r", encoding="utf8") as csv_file:
        for row in csv.DictReader(csv_file, skipinitialspace=True):
            curr_line = line(int(row['line_id']), int(row['character_id']), int(row['movie_id']),
                             int(row['conversation_id']), int(row['line_sort']), str(row['line_text']))
            lines[curr_line.line_id] = curr_line

    for line in lines.values():
        conversations[line.conversation_id].numOfLines += 1
        characters[line.character_id].lines += 1
