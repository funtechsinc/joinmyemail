from fastapi import APIRouter, Request
from fastapi.responses import Response
import logging
import base64
from operations.open_email import email_open, get_campaign_opens
import all_routes


tracking_route = APIRouter()

# Configure logging
logging.basicConfig(level=logging.INFO)


@tracking_route.get("/tracking-pixel")
async def tracking_pixel(request: Request):
    email = request.query_params.get("email")
    campaign = int(request.query_params.get("campaign"))
    email_open(email, campaign)
    # Log the email open event
    logging.info(f"Email opened by: {email}")
    print(email)
    # 1x1 pixel image data (transparent PNG)
    pixel_data = base64.b64decode(
        'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/wcAAgIBAUmmSeAAAAAASUVORK5CYII='
    )

    return Response(content=pixel_data, media_type="image/png")


@tracking_route.get(all_routes.campaign_opens)
def get_campaign_open(campaign_id: int):
    res = get_campaign_opens(campaign_id)
    return res
