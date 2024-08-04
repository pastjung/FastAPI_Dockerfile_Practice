from pydantic import BaseModel
import datetime

class User(BaseModel):
    id : int | None = None
    name : str
    description : str | None = None
    create_date : datetime.date | None = None