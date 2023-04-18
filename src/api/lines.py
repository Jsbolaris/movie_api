from fastapi import APIRouter, HTTPException
from enum import Enum
from src import database as db

router = APIRouter()


@router.get("/lines/{id}", tags=["lines"])
def get_line(id: int):
    """
    This endpoint returns a line by its identifier id. For each line:
    * 'line_id:' the internal id of the movie.
    * 'line_text': text of the line spoken
    * 'char_id': the character id for the character who spoke the line.
    * 'character_name': the character name for the character who spoke the line.
    * 'movie_title': the movie title for the movie the line was in.
    * 'person_1': the first character involved in the conversation.
    * 'person_2': the second character involved in the conversation.

    """
    curr_line = db.lines.get(id)
    if curr_line:
        char = db.characters.get(curr_line.c_id)
        json = {
            "line_id": id,
            "line_text": curr_line.line_text,
            "char_id": char.id,
            "character_name": char.name,
            "movie_title:": db.movies[curr_line.movie_id].title,
            "person_1:": db.conversations[curr_line.conv_id].c1_id,
            "person_2:": db.conversations[curr_line.conv_id].c2_id
        }
        return json

    raise HTTPException(status_code=404, detail="Line not found")


@router.get("/lines/{char_id}", tags=["lines"])
def get_char_lines(char_id: int):
    """
    This endpoint returns a character and all their lines
    * 'character': The name of the character.
    * 'lines': A list of lines spoken by said character
    """

    char = db.characters.get(char_id)
    if char:
        lines = db.characters.get(char_id).lines
        json = {
            "character_name": char.name,
            "lines": lines
        }
        return json

    raise HTTPException(status_code=404, detail="character not found")
