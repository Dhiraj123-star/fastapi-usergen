from faker import Faker
from .models import User
from sqlalchemy.orm import Session

fake = Faker()

def create_fake_user(db: Session):
    user = User(
        name=fake.name(),
        email=fake.unique.email(),
        address=fake.address(),
        phone=fake.phone_number()
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
