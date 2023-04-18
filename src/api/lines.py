from fastapi import APIRouter, HTTPException
from enum import Enum
from src import database as db

router = APIRouter()


@router.get("/lines/{id}", tags=["lines"])
def get_line(temp_id: int):
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
    curr_line = db.lines.get(temp_id)
    if curr_line:
        char = db.characters.get(curr_line.c_id)
        json = {
            "line_id": temp_id,
            "line_text": curr_line.line_text or None,
            "char_id": char.id,
            "character_name": char.name,
            "movie_title:": db.movies[curr_line.movie_id].title,
            "person_1:": db.conversations[curr_line.conv_id].c1_id,
            "person_2:": db.conversations[curr_line.conv_id].c2_id
        }
        return json

    raise HTTPException(status_code=404, detail="Line not found")


@router.get("/lines/{id}/character", tags=["lines"])
def get_char_lines(id: int):
    """
    This endpoint returns a character and all their lines
    * 'character': The name of the character.
    * 'lines': A list of lines spoken by said character
    """
    character = db.characters.get(id)
    if character:
        json = {
            "character": character.name
        }
        return json
    raise HTTPException(status_code=404, detail="Character not found")


@router.get("/lines/{id}", tags=["lines"])
def get_conversations(char_id: int):
    character = db.characters.get(char_id)
