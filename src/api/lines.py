from fastapi import APIRouter, HTTPException
from enum import Enum
from src import database as db

router = APIRouter()


@router.get("/lines/{id}", tags=["lines"])
def get_line(id: int):
    """
    This endpoint returns a line by its identifier id. For each line:
    * 'line_id:' the internal id of the movie.
    * 'character_name': the character name for the character who spoke the line.
    * 'movie_id': the movie identifier for the movie the line was in
    * 'conversation_id': the conversation that this line was a part of.
    * 'line_text': text of the line spoken
    """
    curr_line = db.lines.get(id)
    if curr_line:
        char = db.characters.get(curr_line.c_id)
        json = {
            "line_id": id,
            "char_id": char.id,
            "character_name": char.name,
        }
        return json
    raise HTTPException(status_code=404, detail="Line not found")

class line_sort_options(str, Enum):
    line_id = "line_id"
    line_length = "line_length"
