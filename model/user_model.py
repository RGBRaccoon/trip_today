from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from core.db_config import Base


class UserModel(SQLAlchemyBaseUserTableUUID, Base):
    pass
