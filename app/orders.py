from fastapi import APIRouter
from app.database import orders_collection
from app.models import OrderModel
from bson.objectid import ObjectId

router = APIRouter()

@router.post("/orders", status_code=201)
def create_order(order: OrderModel):
    result = orders_collection.insert_one(order.dict())
    return {"message": "Order created", "id": str(result.inserted_id)}

@router.get("/orders/{user_id}", status_code=200)
def get_orders(user_id: str, limit: int = 10, offset: int = 0):
    orders = orders_collection.find({"user_id": user_id}).skip(offset).limit(limit)
    return [{"_id": str(o["_id"]), **{k: v for k, v in o.items() if k != "_id"}} for o in orders]
