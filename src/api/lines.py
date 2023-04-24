from fastapi import APIRouter, HTTPException
from enum import Enum
from src import database as db

router = APIRouter()


@router.get("/lines/{id}", tags=["lines"])
def get_line(line_id: str):
    """
    This endpoint returns a line by it's identifier id. For each line:
    * 'line_id:' the internal id of the movie.
    * 'character_id': the character identifier for the character who spoke the line.
    * 'movie_id': the movie identifier for the movie the line was in
    * 'conversation_id': the conversation that this line was a part of.
    * 'line_text': text of the line spoken
    """
    try:
        curr_line = db.lines.get(line_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="No matching line was found")
    return_line = {
        "line_id": line_id,
        "character_id": curr_line.character_id
    }
    return return_line


class line_sort_options(str, Enum):
    line_id = "line_id"
    line_length = "line_length"
