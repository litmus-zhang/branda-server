from typing import List
from novu.api import EventApi, TopicApi
import os
from pydantic import EmailStr

url, api = "https://api.novu.co", os.getenv("NOVU_API_KEY")


class NotificationService:
    def __init__(self):
        self.event_api = EventApi(url=url, api_key=api)

    def send_onboarding_mail(self, message, user_email):
        # send mail
        pass

    def email_link_to_brand(self, message, emails: List[EmailStr]):
        # send mail
        pass

    def create_topic(
        self,
        topic_key: str,
        topic_name: str,
    ):
        new_topic = TopicApi(url, api).create(key=topic_key, name=topic_name)
        return new_topic
