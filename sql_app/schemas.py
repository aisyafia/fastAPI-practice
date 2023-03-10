from typing import Union
from pydantic import BaseModel

# list stuff
class RecipeBase(BaseModel):
    name: str
    category: str
    is_tried: bool
    picture: str

class RecipeCreate(RecipeBase):
    pass

class Recipe(RecipeBase):
    # ingredients: recipe[Ingredient] = []

    class Config:
        orm_mode = True