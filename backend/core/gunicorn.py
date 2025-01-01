from gunicorn.app.base import BaseApplication

from core.config import WORKER
from core.db_config import create_db


class CustomGunicornApp(BaseApplication):
    def __init__(self, app):
        self.app = app
        self.options = {
            "bind": "0.0.0.0:8080",  # 서버 바인딩 주소 및 포트
            "workers": WORKER,  # 워커 수
            "worker_class": "uvicorn.workers.UvicornWorker",  # Uvicorn ASGI 워커
            "loglevel": "info",  # 로그 레벨 설정
        }
        create_db()
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items() if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.app
