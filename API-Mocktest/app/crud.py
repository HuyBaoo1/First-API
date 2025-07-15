from sqlalchemy.orm import Session 
from . import models,schemas 

def get_users(db: Session):
    return db.query(models.User).all()

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user
# ----------------------------------------


def get_movies(db: Session, limit: int = 100):
    return db.query(models.Movie).limit(limit).all()

def create_movie(db: Session, movie: schemas.MovieCreate):
    db_movie = models.Movie(
        title=movie.title,
        year=movie.year,
        author=movie.author
    )
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def get_movie_by_id(db: Session, movie_id: int):
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()

def delete_movie(db: Session, movie_id: int):
    movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if movie:
        db.delete(movie)
        db.commit()
    return movie

# ----------------------------------------


def get_tvshows(db: Session, limit: int = 100):
    return db.query(models.TVShow).limit(limit).all()

def create_tvshow(db: Session, tvshow: schemas.TVShowCreate):
    db_tvshow = models.TVShow(
        title=tvshow.title,
        year=tvshow.year,
        author=tvshow.author
    )
    db.add(db_tvshow)
    db.commit()
    db.refresh(db_tvshow)
    return db_tvshow

def get_tvshow_by_id(db: Session, tvshow_id: int):
    return db.query(models.TvShow).filter(models.TvShow.id == tvshow_id).first()

def delete_tvshow(db: Session, tvshow_id: int):
    tvshow = db.query(models.TvShow).filter(models.TvShow.id == tvshow_id).first()
    if tvshow:
        db.delete(tvshow)
        db.commit()
    return tvshow