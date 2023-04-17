from fastapi import APIRouter, HTTPException
from enum import Enum
from src import database as db

router = APIRouter()


@router.get("/lines/{id}", tags=["lines"])
def get_line(id: str):
    """



    :param id:
    :return:
    """
    try:
        curr_line = db.lines[id]
    except KeyError:
        raise HTTPException(status_code=404, detail="No matching line was found")
    return_line = {
        "line_id": id,
        "character_id": int(curr_line["character_id"]),
        "movie_id": int(curr_line["movie_id"]),
        "conversation_id": int(curr_line["conversation_id"]),
        "line_text": str(curr_line["line_text"] or None)
    }
    return return_line


class line_sort_options(str, Enum):
    line_id = "line_id"
    line_length = "line_length"
