from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    password: str
    company: str


class Login(BaseModel):
    email: str
    password: str


class SmtpConfig(BaseModel):
    uuid: int
    name: str = None
    smtp_email: str = None
    smtp_password: str = None


class UserSubscription(BaseModel):
    uuid: str
    display_name: str
    email: str
    country: str
    subscription_hash: str


class EmailTemplate(BaseModel):
    uuid: str
    template_name: str
    body: str


class EmailSendingResult(BaseModel):
    uuid: str
    subject: str
    body: str
    smtp_id: str
    number_of_subscribers_reach: int
    success: int
    errors: int