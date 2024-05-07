from fastapi import APIRouter

entry_route = APIRouter()


# entry route
@entry_route.get('/')
async def home() -> dict:
    return {
        'status': 'ok',
        'message': '@Subscribe to my email list'
    }
