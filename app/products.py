from fastapi import APIRouter, Query
from app.database import products_collection
from app.models import ProductModel
from typing import Optional, List
import re

router = APIRouter()

@router.post("/products", status_code=201)
def create_product(product: ProductModel):
    result = products_collection.insert_one(product.dict())
    return {"message": "Product created", "id": str(result.inserted_id)}

@router.get("/products", status_code=200)
def list_products(name: Optional[str] = None, size: Optional[str] = None,
                  limit: int = 10, offset: int = 0):
    query = {}
    if name:
        query["name"] = {"$regex": re.escape(name), "$options": "i"}
    if size:
        query["size"] = size

    products = products_collection.find(query).skip(offset).limit(limit)
    return [{"_id": str(p["_id"]), **{k: v for k, v in p.items() if k != "_id"}} for p in products]
