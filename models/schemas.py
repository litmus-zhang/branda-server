from pydantic import BaseModel


class Strategy(BaseModel):
    industry: str
    niche: str
    country: str


class Base(BaseModel):
    niche: str
    industry: str


class UserInput(BaseModel):
    email: str
    password: str


class BaseBody(BaseModel):
    name: str | None = None
    font: str | None = None
    strategy: str | None = None
    color: str | None = None
    logo: str | None = None
    messaging: str | None = None
    photography: str | None = None
    illustration: str | None = None
    presentation: str | None = None


class LogoVariant(BaseModel):
    name: str
    url: str

    niche : str
    industry : str


class UserInput(BaseModel):
    email: str
    password: str

class BaseBody(BaseModel):
    name: str | None = None
    font: str | None = None
    strategy: str | None = None
    color: str | None = None
    logo: str | None = None
    messaging: str | None = None
    photography: str | None = None
    illustration: str | None = None
    presentation: str | None = None

class Logo(BaseModel):
    variants: list[LogoVariant]
