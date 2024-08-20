from pydantic import BaseModel

class StockSerializer(BaseModel):
    operation: str
    unit_cost: float
    quantity: int


class TaxStockSerializer(BaseModel):
    tax: float
