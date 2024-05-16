from fastapi import FastAPI
from routes.entry import entry_route
from routes.smtp import smtp_routes
from routes.auth import auth_route
from routes.email import email_route
from routes.profile import profile_route
from routes.templates import templates_routes
from routes.subscription import subscription_route
from routes.analytics import analytics_route
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(entry_route)
app.include_router(smtp_routes)
app.include_router(auth_route)
app.include_router(email_route)
app.include_router(templates_routes)
app.include_router(profile_route)
app.include_router(subscription_route)
app.include_router(analytics_route)
