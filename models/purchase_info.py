from pydantic import BaseModel
from typing import Optional

class PurchaseInfo(BaseModel):
    date: Optional[str] = None
    currency: Optional[str] = None
    price: Optional[float] = None
    location: Optional[str] = None

    def __init__(self, **data):
        super().__init__(**data)

        # validate the purchase
        if self.price and not self.currency:
            self.currency = 'USD'

    def __str__(self):
        return f'{self.date} {self.price} {self.currency} {self.location}'
