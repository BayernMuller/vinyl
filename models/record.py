from pydantic import BaseModel
from typing import List, Tuple, Optional

DEFAULT_CURRENCY = 'USD'

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
    purchase: Optional[dict] = {}

    # constructor
    def __init__(self, **data):
        super().__init__(**data)

        # validate the purchase
        if self.purchase:
            if 'price' in self.purchase and 'currency' not in self.purchase:
                self.purchase['currency'] = DEFAULT_CURRENCY

    @property
    def purchase_date(self) -> Optional[str]:
        if self.purchase:
            return self.purchase.get('date')
        return None
    
    @property
    def purchase_price(self) -> Optional[Tuple[str, float]]:
        if self.purchase is None or 'price' not in self.purchase:
            return None

        currency = self.purchase.get('currency')
        price = self.purchase.get('price')
        if price == 0:
            return None

        return (currency, price) if price and currency else None

    def __str__(self):
        return f'{self.artist} {self.title} {self.year} {self.format}'