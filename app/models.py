from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId

class ProductModel(BaseModel):
    name: str
    price: float
    description: str
    size: str

class OrderModel(BaseModel):
    user_id: str
    product_ids: List[str]
