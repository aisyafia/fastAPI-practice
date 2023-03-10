from sqlalchemy.orm import Session
import models, schemas

def create_recipe(db: Session, recipe: schemas.Recipe):
    print("here")
    print("recipe", list)
    db_recipe = models.Recipe(**recipe.dict())
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe