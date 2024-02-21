from pydantic import BaseModel
from typing import List, Optional

class Record(BaseModel):
    # required
    cover: str
    artist: str
    title: str
    year: int
    genre: str
    format: str

    # optional
    country: Optional[str] = 'N/A'

    def __str__(self):
        return f'{self.artist} {self.title} {self.year} {self.format}'