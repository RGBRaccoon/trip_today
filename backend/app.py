from fastapi import FastAPI

from api.router.router import router
from core.gunicorn import CustomGunicornApp

app = FastAPI()
# app.include_router(router=total_test_router)
app.include_router(router=router)
if __name__ == "__main__":
    # Gunicorn 서버를 Python 코드 내에서 실행
    CustomGunicornApp(app=app).run()
