from typing import List

from fastapi import FastAPI, HTTPException
import uvicorn

from pearson_correlation import calculate_correlation
from db_cru import *
from database import SessionLocal

welltory_app = FastAPI()
db = SessionLocal()


def list_intersect(list1: List, list2: List):
    """
    Intersection of two lists
    :param list1: the first list
    :param list2: the second list
    :return: intersection of lists
    """
    assert len(list1) == len(list2)

    try:
        return list(set(list1) & set(list2))
    except (ValueError, TypeError):
        return None


@welltory_app.post("/calculate", response_model=schemas.User)
async def calculate(user: schemas.UserCreate):

    # add user to database
    create_user(db, user)

    # calculate correlations
    user_data = user["data"]

    user_data_x = user_data["x"]
    user_data_y = user_data["y"]

    x_values_dates = sorted([val['date'] for val in user_data_x], key=lambda val: val['date'])
    y_values_dates = sorted([val['date'] for val in user_data_y], key=lambda val: val['date'])
    similar_dates = []
    try:
        similar_dates = sorted(list_intersect(x_values_dates, y_values_dates))
    except TypeError as e:
        print(e)

    x_values = [i["value"] for i in user_data_x if i['date'] in similar_dates]
    y_values = [i["value"] for i in user_data_y if i['date'] in similar_dates]

    user.correlation_value = calculate_correlation(x_values, y_values)[0]
    user.correlation_p_value = calculate_correlation(x_values, y_values)[1]


@welltory_app.get("/correlation")
async def get_correlation(x_data_type: str, y_data_type: str, user_id: int):

    user = get_user_full(db=db, user_id=user_id, x_data_type=x_data_type, y_data_type=y_data_type)

    if user.correlation_value is None or user.correlation_p_value is None:
        raise HTTPException(status_code=404, detail="Metrics was not calculated")

    return_json = {
        "user_id": user.user_id,
        "x_data_type": user.x_data_type,
        "y_data_type": user.y_data_type,
        "correlation": {
            "value": user.correlation_value,
            "p_value": user.correlation_p_value,
        }
    }

    return return_json

if __name__ == "__main__":
    uvicorn.run(welltory_app, host="127.0.0.1", port=5000)