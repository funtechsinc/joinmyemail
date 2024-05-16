import operations.templates as templates_operation
from fastapi import APIRouter
from models.pydantic_model import EmailTemplate
import all_routes

templates_routes = APIRouter()


# create a template
@templates_routes.post(all_routes.template_create)
async def create_template(doc: EmailTemplate, uuid: str):
    doc = dict(doc)
    res = templates_operation.create_template(doc, uuid)
    return res


# update a template
@templates_routes.patch(all_routes.template_edit)
async def update_template(doc: EmailTemplate, template_id: int):
    doc = dict(doc.model_dump(exclude_unset=True))
    res = templates_operation.edit_template(doc, template_id)
    return res


# get all templates
@templates_routes.get(all_routes.template_all)
async def all_templates(uuid: int):
    res = templates_operation.all_templates(uuid)
    return res


# get a single smtp
@templates_routes.get(all_routes.template_get)
async def get_template(template_id: int):
    res = templates_operation.one_template(template_id)
    return res


# delete
@templates_routes.delete(all_routes.template_delete)
async def delete_template(_id: int):
    res = templates_operation.delete_template(_id)
    return res
