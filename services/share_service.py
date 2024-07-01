from enum import Enum
import os
from fastapi.responses import JSONResponse


class Scope(str, Enum):
    PUBLIC = "public"
    PRIVATE = "private"


class LinkShareService:
    def __init__(self):
        pass

    def share_link(self, link):
        # get the scope(public, private), mail(list of mails of recipient) and assets() to share,
        # create a link and send it to the recipient
        # return the link
        # link format: /share/{documentId}/{scope}/{asset_id}
        BASE_URL = (
            os.getenv("BASE_URL") if os.getenv("BASE_URL") else "http://localhost:8000"
        )
        return JSONResponse(
            content={
                "message": "Link shared successfully",
                "data": {
                    "link": f"{BASE_URL}/share/{link.asset_id}/{link.scope}/{link.asset_id}"
                },
            }
        )
