from firebase_admin import db

brands = db.collections("brands")


# create a collection for Brands
# - add name, logo, font and all brand identity