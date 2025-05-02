from pydantic import BaseModel

class SlideModel(BaseModel):
    title: str
    content: str