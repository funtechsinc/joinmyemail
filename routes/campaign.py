from fastapi import APIRouter
import operations.campaign as db
import all_routes
from models.pydantic_model import Campaign

campaign_routes = APIRouter()


# create campaign
@campaign_routes.post(all_routes.campaign_create)
def create_campaigns(doc: Campaign, uuid: int):
    doc: dict = dict(doc)
    uuid: int = uuid
    res: dict = db.create_campaign(doc, uuid)
    return res


# get user campaigns
@campaign_routes.get(all_routes.campaign_all)
def all_campaigns(uuid: int):
    uuid = uuid
    res: dict = db.user_campaigns(uuid)
    return res


# Delete Campaign
@campaign_routes.delete(all_routes.campaign_delete)
def delete_campaign(campaign_id: int):
    campaign_id = campaign_id
    res: dict = db.delete_campaign(campaign_id)
    return res
