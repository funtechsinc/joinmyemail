from pydantic import BaseModel


class User(BaseModel):
    username: str = None
    handle: str = None
    company: str = None
    title: str = None
    sub_title: str = None
    photo_url: str = None
    category: str = None
    youtube: str = None
    instagram: str = None
    x: str = None
    welcome_message: str = None
    smtp_for_welcome_message: str = None


class UserHandle(BaseModel):
    handle: str


class AuthRegister(BaseModel):
    username: str
    email: str
    password: str


class AuthLogin(BaseModel):
    email: str
    password: str


class WelcomeMessage(BaseModel):
    message: str
    server_id: int


class SmtpConfig(BaseModel):
    name: str = None
    server: str = None
    smtp_email: str = None
    smtp_password: str = None


class UserSubscription(BaseModel):
    display_name: str
    email: str
    country: str


class EmailTemplate(BaseModel):
    template_name: str = None
    body: str = None


class EmailSendingResult(BaseModel):
    uuid: str
    subject: str
    body: str
    smtp_id: str
    number_of_subscribers_reach: int
    success: int
    errors: int