import uuid
from datetime import datetime

from sqlalchemy import ARRAY, JSON, TIMESTAMP, UUID, Boolean, Column, String, Text

from utils import get_instance

_, db = get_instance()


class Users(db.Model):
    __tablename__ = "users"

    account_id = Column(UUID, nullable=False, primary_key=True)
    date_of_birth = Column(TIMESTAMP, nullable=False)
    first_name = Column(String(1000), nullable=False)
    gender = Column(Boolean, nullable=False)
    last_name = Column(String(1000), nullable=False)
    others = Column(JSON, nullable=True)
    social_media_link = Column(ARRAY(String(1000)), nullable=True)
    summary_introduction = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=True)

    def __repr__(self) -> str:
        return f"<User {self.account_id}>"

    def __init__(
        self,
        account_id: uuid.UUID,
        date_of_birth: datetime,
        first_name: str,
        gender: bool,
        last_name: str,
        social_media_link: list = [],
        summary_introduction: str = "",
    ):
        self.account_id = account_id
        self.date_of_birth = date_of_birth
        self.first_name = first_name
        self.gender = gender
        self.last_name = last_name
        self.social_media_link = social_media_link
        self.summary_introduction = summary_introduction
        self.created_at = datetime.now()