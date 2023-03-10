from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import database, models, crud, schemas

# from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
  CORSMiddleware, 
  allow_origins=origins, 
  allow_credentials=True, 
  allow_methods=["*"],
  allow_headers=["*"]
)

# Dependency
def get_db():
  db = database.SessionLocal()
  try:
    yield db
  finally:
    db.close()

# # create list
@app.post("/recipes", response_model=schemas.Recipe)
def create_list(recipe: schemas.Recipe, db: Session = Depends(get_db)):
  print("here")
  return crud.create_recipe(db, recipe=recipe)