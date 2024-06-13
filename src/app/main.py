from fastapi import FastAPI, Depends

from fastapi_users import FastAPIUsers

from src.app.auth.base_config import auth_backend
from src.app.auth.manager import get_user_manager
from src.app.auth.models import User
from src.app.auth.schema import UserRead, UserCreate
from src.app.operations.router import router as router_operations

app = FastAPI(
    title="Trading App"
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
     router_operations

)
current_user = fastapi_users.current_user()


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonymous"
