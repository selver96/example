from typing import Final, Tuple
from fastapi.routing import APIRouter

from . import employee




ROUTERS: Final[Tuple[APIRouter, ...]] = (
    employee.router,
)