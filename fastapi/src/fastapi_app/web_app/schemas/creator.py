from pydantic import BaseModel


class CreatorSchema(BaseModel):
    first_name: str
    last_name: str
