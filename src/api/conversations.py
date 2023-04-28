from fastapi import APIRouter, HTTPException
from src import database as db
from pydantic import BaseModel
from typing import List
from datetime import datetime


# FastAPI is inferring what the request body should look like
# based on the following two classes.
class LinesJson(BaseModel):
    character_id: int
    line_text: str


class ConversationJson(BaseModel):
    character_1_id: int
    character_2_id: int
    lines: List[LinesJson]


router = APIRouter()


@router.post("/movies/{movie_id}/conversations/", tags=["movies"])
def add_conversation(movie_id: int, conversation: ConversationJson):
    """
    This endpoint adds a conversation to a movie. The conversation is represented
    by the two characters involved in the conversation and a series of lines between
    those characters in the movie.

    The endpoint ensures that all characters are part of the referenced movie,
    that the characters are not the same, and that the lines of a conversation
    match the characters involved in the conversation.

    Line sort is set based on the order in which the lines are provided in the
    request body.

    The endpoint returns the id of the resulting conversation that was created.
    """
    person1 = db.characters[conversation.character_1_id]
    person2 = db.characters[conversation.character_2_id]
    linesort = 1

    curr_cov = int(db.convos[len(db.convos) - 1]["conversation_id"])
    curr_cov += 1
    # hazard/duplication checks for adding
    if conversation.character_1_id == conversation.character_2_id:
        raise HTTPException(status_code=404, detail="these two characters are the same!")
    if movie_id != person1.movie_id or movie_id != person2.movie_id:
        raise HTTPException(status_code=404, detail="Characters not found in film")
    if movie_id not in db.movies:
        raise HTTPException(status_code=404, detail="movie not found")
    if conversation.character_1_id not in db.characters or conversation.character_2_id not in db.characters:
        raise HTTPException(status_code=404, detail="character(s) not found")
    db.convos.append({"conversation_id": 1 + int(db.convos[len(db.convos) - 1]["conversation_id"]),
                      "character1_id": conversation.character_1_id,
                      "character2_id": conversation.character_2_id,
                      "movie_id": movie_id
                      })
    db.upload_convo()
    # add lines
    for row in conversation.lines:
        char_id = row.character_id
        line_text = row.line_text
        db.all_lines.append({"line_id": 1 + int(db.all_lines[len(db.all_lines) - 1]["line_id"]),
                             "character_id": char_id,
                             "movie_id": movie_id,
                             "conversation_id": curr_cov,
                             "line_sort": linesort,
                             "line_text": line_text
                             })
        line_sort = linesort + 1
    db.upload_lines()

    return curr_cov
    # print("Endpoint has been called!")
    # check characters are different
