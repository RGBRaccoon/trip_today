from core.base_service import BaseService


class LocationService(BaseService):
    def __init__(self, session):
        super().__init__(session)
        self.location_repository = LocationRepository(session=self.session)
