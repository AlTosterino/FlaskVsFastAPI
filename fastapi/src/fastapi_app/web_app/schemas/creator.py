from pydantic import BaseModel, Field

FIRST_NAME_MIN_LEN = 2
FIRST_NAME_MAX_LEN = 60
LAST_NAME_MIN_LEN = 2
LAST_NAME_MAX_LEN = 100

class CreatorSchema(BaseModel):
    first_name: str = ""
    last_name: str = ""


class CreatorSchemaInput(CreatorSchema):
    first_name: str = Field(
        title="First name of the creator",
        min_length=FIRST_NAME_MIN_LEN,
        max_length=FIRST_NAME_MAX_LEN,
        example="John",
    )
    last_name: str = Field(
        title="Last name of the creator",
        min_length=LAST_NAME_MIN_LEN,
        max_length=LAST_NAME_MAX_LEN,
        example="Doe",
    )


class CreatorSchemaUpdate(CreatorSchema):
    first_name: str = ""
    last_name: str = ""
