from database import Base
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, index=True)
    category = Column(String, index=True)
    is_tried = Column(Boolean)
    picture = Column(String)

    # ingredients = relationship("Ingredient", back_populates="recipes")


class Ingredients(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, index=True)
    type = Column(String, unique=True, index=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))

    # recipes = relationship("Recipe", back_populates="ingredients")

