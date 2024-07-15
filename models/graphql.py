import strawberry
import typing


@strawberry.type
class BusinessDetails:
    niche: str
    description: str
    target_audience: str
    country: str

@strawberry.type
class Brand:
    ID: strawberry.ID
    name: str
    logo: str
    color: str
    font: str
    messaging: str
    photography: str
    Illustration: str
    business_details: "BusinessDetails"

@strawberry.type
class User:
    ID: strawberry.ID
    name: str
    email: str
    brands: typing.List["Brand"]

    
@strawberry.type
class Query:
    getBrand: typing.List[Brand]
    getUser:  typing.List[User]

schema = strawberry.Schema(schema_directives=[Brand, BusinessDetails, User], query=Query)