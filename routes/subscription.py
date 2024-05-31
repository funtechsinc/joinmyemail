from fastapi import APIRouter
import all_routes
import operations.subscriptions as subs
from models.pydantic_model import UserSubscription

subscription_route = APIRouter()


# new subscriber
@subscription_route.post(all_routes.subscriptions_create)
def create_subscription(doc: UserSubscription, handle: str) -> dict:
    doc = dict(doc)
    res = subs.new_subscription(doc, handle)
    return res


# unsubscribe
@subscription_route.get(all_routes.subscription_unsubscribe)
def unsubscribe(hash_token: str) -> dict:
    res = subs.unsubscribe(hash_token)
    return res


# all subscriptions
@subscription_route.get(all_routes.subscription_all)
def all_subscribers(uuid: int):
    res = subs.all_subscribers(uuid)
    return res

