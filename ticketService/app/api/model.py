
from pydantic import BaseModel
from typing import List, Optional

class TicIn(BaseModel):
    desc: str
    parent_id: Optional[str] = None
    sprint : str = None
    child_id :str = None
    story_points: int = None
    tic_dev : str = None
    tic_pm : str = None
    tic_creator : str = None
    tic_start_date : str = None
    tic_end_date : str = None


class TicOut(TicIn):
    id: int


class TicUpdate(TicIn):
    name: Optional[str] = None