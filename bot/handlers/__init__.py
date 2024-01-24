from .admins import admin_start_router
from .users import maintenance_router, user_start_router


routers_list = [
    admin_start_router,
    maintenance_router,
    user_start_router,
]

__all__ = [
    'routers_list',
]
