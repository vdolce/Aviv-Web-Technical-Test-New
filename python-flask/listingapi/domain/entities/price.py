from pydantic import BaseModel


class PriceEntity(BaseModel):
    listing_id: int
    price_eur: float
