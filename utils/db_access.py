from typing import Tuple


async def pagination(skip: int = 0, limit: int = 10) -> Tuple[int, int]:
    return (skip, limit)
