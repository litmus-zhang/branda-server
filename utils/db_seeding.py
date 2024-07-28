from models.models import Brand, User
from config.database import SessionLocal
from mimesis import Person, Generic


def seed_users(db=SessionLocal):
    person = Person("en")

    for _ in range(10):
        user = User(
            firstname=person.first_name(),
            lastname=person.last_name(),
            email=person.email(),
            hashed_password=person.password(),
        )
        db.add(user)
    db.commit()


def seed_brands(db):
    generic = Generic("en")

    for _ in range(10):
        brand = Brand(
            name=generic.business.company(),
            font=generic.text.word(),
            strategy=generic.text.word(),
            color=generic.color.color_name(),
            logo=generic.business.company(),
            messaging=generic.text.word(),
            photography=generic.business.company(),
            illustration=generic.business.company(),
            presentation=generic.business.company(),
            owner_id=1,
        )
        db.add(brand)
    db.commit()


def seed_all():
    db = SessionLocal()
    seed_users(db)
    seed_brands(db)

seed_all()
