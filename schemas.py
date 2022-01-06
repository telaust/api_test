from typing import List, Optional

from pydantic import BaseModel


class User(BaseModel):
    user_id: int
    x_data_type: str
    y_data_type: str
    correlation_value: Optional[float] = None
    correlation_p_value: Optional[float] = None


class UserCreate(User):
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: Optional[int] = None
