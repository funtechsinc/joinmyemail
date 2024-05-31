from pydantic import BaseModel


class User(BaseModel):
    username: str = None
    handle: str = None
    company: str = None
    title: str = None
    about: str = None
    sub_title: str = None
    photo_url: str = None
    category: str = None
    youtube: str = None
    instagram: str = None
    x: str = None
    buy_me_a_coffe: str = None
    welcome_message: str = None
    welcome_message_subject: str = None
    call_to_action: str = None
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
    welcome_message_subject: str
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


class Unsubscribe(BaseModel):
    hash_token: str


class EmailTemplate(BaseModel):
    template_name: str = None
    body: str = None


class Campaign(BaseModel):
    subject: str = None
    body: str = None
    template_id: int = None
    smtp_id: int
    deployed: bool = None
