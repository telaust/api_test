from datetime import datetime, timedelta
from typing import Optional

from sqlalchemy.orm import Session

import db_models as models
import schemas
from auth_utils import *


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_full(db: Session, user_id: int, x_data_type: str, y_data_type: str):
    return db.query(models.User).filter(models.User.user_id == user_id and
                                        models.User.x_data_type == x_data_type and
                                        models.User.y_data_type == y_data_type
                                        ).first()


def get_users(db: Session, skip: int = 0, limit: int = 20):
    return db.query(models.User).offset(skip).limit(limit).all()


def authenticate_user(db, user_id: int, password: str):
    user = get_user(db, user_id)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_user(db: Session, user: schemas.UserCreate):
    """
    Add user to database
    :param db:
    :param user:
    :return:
    """
    jwt_token = get_password_hash(user.password)
    db_user = models.User(hashed_password=jwt_token)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
