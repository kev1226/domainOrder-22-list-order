from fastapi import Request
from app.repository.order_repository import find_order_by_id
from app.auth.jwt_utils import decode_token


async def resolve_get_order_by_id(_, info, id):
    request: Request = info.context["request"]
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    user_data = decode_token(token)

    if not user_data:
        raise Exception("Token inválido")

    email = user_data["email"]
    roles = user_data.get("roles", [])

    order = await find_order_by_id(id)

    if not order:
        raise Exception("Orden no encontrada")

    if order["user"]["email"] != email and "admin" not in roles:
        raise Exception("Acceso denegado: orden no pertenece a este usuario")

    order["id"] = str(order["_id"])
    return order
