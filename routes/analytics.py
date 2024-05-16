from fastapi import APIRouter
import all_routes
import operations.analytics as anly


analytics_route = APIRouter()


# yearly subs
@analytics_route.get(all_routes.analytics_yearly_subscriptions)
def yearly_subs(year: int, uuid: str):
    res = anly.get_yearly_subs(year, uuid)
    return res


# yearly campaigns
@analytics_route.get(all_routes.analytics_yearly_campaigns)
def yearly_campaign(year: int, uuid: str):
    res = anly.get_yearly_campaigns(year, uuid)
    return res

