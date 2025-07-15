from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session  
from . import models, database, crud, schemas
from pydantic import BaseModel



models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.post("/users/", response_model= schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    existing_users = crud.get_users(db)
    if any(u.email == user.email for u in existing_users):
        raise HTTPException(status_code=400, detail="Email already registered")

    return crud.create_user(db, user)

@app.get("/users/", response_model=list[schemas.UserOut])
def get_users(db: Session = Depends(database.get_db)):
    return crud.get_users(db=db)

@app.get("/users/{user_id}", response_model=schemas.UserOut)
def get_user(user_id: int, db: Session = Depends(database.get_db)):
    user = crud.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.delete("/users/{user_id}", response_model=schemas.UserOut)
def delete_user(user_id: int, db: Session = Depends(database.get_db)):
    user = crud.delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

#-------------------------------------------

@app.post("/movies/", response_model=schemas.MovieOut)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(database.get_db)):
    return crud.create_movie(db, movie)

@app.get("/movies/", response_model=list[schemas.MovieOut])
def list_movies(limit: int = 100, db: Session = Depends(database.get_db)):
    return crud.get_movies(db, limit)

@app.get("/movies/{movie_id}", response_model=schemas.MovieOut)
def get_movie(movie_id: int, db: Session = Depends(database.get_db)):
    movie = crud.get_movie_by_id(db, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@app.delete("/movies/{movie_id}", response_model=schemas.MovieOut)
def delete_movie(movie_id: int, db: Session = Depends(database.get_db)):
    movie = crud.delete_movie(db, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie    

#---------------------------------------------

@app.post("/tvshows/", response_model=schemas.TVShowOut)
def create_tvshow(tvshow: schemas.TVShowCreate, db: Session = Depends(database.get_db)):
    return crud.create_tvshow(db, tvshow)

@app.get("/tvshows/", response_model=list[schemas.TVShowOut])
def list_tvshows(limit: int = 100, db: Session = Depends(database.get_db)):
    return crud.get_tvshows(db, limit)

@app.get("/tvshows/{tvshow_id}", response_model=schemas.TVShowOut)
def get_tvshow(tvshow_id: int, db: Session = Depends(database.get_db)):
    tvshow = crud.get_tvshow_by_id(db, tvshow_id)
    if not tvshow:
        raise HTTPException(status_code=404, detail="TV Show not found")
    return tvshow

@app.delete("/tvshows/{tvshow_id}", response_model=schemas.TVShowOut)
def delete_tvshow(tvshow_id: int, db: Session = Depends(database.get_db)):
    tvshow = crud.delete_tvshow(db, tvshow_id)
    if not tvshow:
        raise HTTPException(status_code=404, detail="TVShow not found")
    return tvshow
