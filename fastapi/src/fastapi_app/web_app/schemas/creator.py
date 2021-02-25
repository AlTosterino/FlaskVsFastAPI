from pydantic import BaseModel, Field


class CreatorSchema(BaseModel):
    first_name: str = Field(
        title="First name of the creator",
        min_length=2,
        max_length=60,
        example="John",
    )
    last_name: str = Field(
        title="Last name of the creator",
        min_length=2,
        max_length=100,
        example="Doe",
    )
