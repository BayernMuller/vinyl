from pydantic import BaseModel
from typing import List, Tuple, Optional
from models.purchase_info import PurchaseInfo

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
    purchase: Optional[PurchaseInfo] = None

    @property
    def purchase_date(self) -> Optional[str]:
        if self.purchase:
            return self.purchase.date
        return None
    
    @property
    def purchase_price(self) -> Optional[Tuple[str, float]]:
        if self.purchase is None or self.purchase.price is None:
            return None

        currency = self.purchase.currency
        price = self.purchase.price
        if price == 0:
            return None

        return (currency, price) if price and currency else None
    
    @property
    def purchase_location(self) -> Optional[str]:
        if self.purchase:
            return self.purchase.location
        return None

    def __str__(self):
        return f'{self.artist} {self.title} {self.year} {self.format}'
