import operations.smtp_server as smtp_operations
from fastapi import APIRouter
from models.pydantic_model import SmtpConfig
import all_routes

smtp_routes = APIRouter()


# create a server
@smtp_routes.post(all_routes.smtp_create_server)
async def create_smtp(doc: SmtpConfig):
    doc = dict(doc)
    res = smtp_operations.create_smtp_server(doc)
    return res


# update a server
@smtp_routes.patch(all_routes.smtp_update)
async def update_smtp(doc: SmtpConfig, smtp_id: int):
    doc = dict(doc.model_dump(exclude_unset=True))
    res = smtp_operations.update_smtp(doc, smtp_id)
    return res


# get all smtp
@smtp_routes.get(all_routes.smtp_all_servers)
async def all_smtp(uuid: str):
    res = smtp_operations.get_all_smtp(uuid)
    return res


# get a single smtp
@smtp_routes.get(all_routes.smtp_get)
async def get_smtp(server_id: int):
    res = smtp_operations.get_smtp(server_id)
    return res


# delete
@smtp_routes.delete(all_routes.smtp_delete)
async def delete_smtp(server_id: int):
    res = smtp_operations.delete_smtp(server_id)
    return res