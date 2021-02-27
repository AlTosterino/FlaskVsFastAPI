from typing import Any, Dict, Optional, Union

Response_Type = Optional[Dict[Union[int, str], Dict[str, Any]]]


NOT_FOUND_FOR_ID: Response_Type = {
    404: {
        "description": "News with given ID wasn't found",
        "content": {
            "application/json": {"example": {"detail": "News with id {id} don't exist"}}
        },
    }
}
