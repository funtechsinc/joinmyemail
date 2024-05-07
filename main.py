from fastapi import FastAPI
from routes.entry import entry_route
from routes.smtp import smtp_routes
from routes.google import google_route
from routes.email import email_route

app = FastAPI()

app.include_router(entry_route)
app.include_router(smtp_routes)
app.include_router(google_route)
app.include_router(email_route)
