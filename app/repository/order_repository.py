import motor.motor_asyncio
from bson import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()

client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGODB_URI"))
db = client[os.getenv("DB_NAME")]
collection = db["orders"]


async def find_order_by_id(order_id: str):
    try:
        order = await collection.find_one({"_id": ObjectId(order_id)})
        return order
    except:
        return None
