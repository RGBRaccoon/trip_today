from dotenv import dotenv_values

env_vars = dotenv_values(".env")

# PostgreSQL 연결 URL 설정
# DATABASE_URL = "postgresql+asyncpg://username:password@localhost:5432/dbname"
DATABASE_URL = env_vars["DATABASE_URL"]
SYNC_DATABASE_URL = env_vars["SYNC_DATABASE_URL"]
WORKER = env_vars["WORKER"]
PORT = env_vars["PORT"]
IP = env_vars["IP"]
