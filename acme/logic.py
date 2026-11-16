import re
from datetime import datetime
from typing import List

import model
import db


TITLE_LIMIT = 30
TEXT_LIMIT = 200
_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


class LogicException(Exception):
    pass


class EventLogic:
    def __init__(self):
        self._event_db = db.EventDB()

    @staticmethod
    def _validate_event(event: model.Event):
        if event is None:
            raise LogicException("event is None")
        if event.date is None or not _DATE_RE.match(event.date):
            raise LogicException(f"invalid date: {event.date}")
        try:
            datetime.strptime(event.date, "%Y-%m-%d")
        except ValueError:
            raise LogicException(f"invalid date: {event.date}")
        if event.title is None or len(event.title) > TITLE_LIMIT:
            raise LogicException(f"title lenght > MAX: {TITLE_LIMIT}")
        if event.text is None or len(event.text) > TEXT_LIMIT:
            raise LogicException(f"text lenght > MAX: {TEXT_LIMIT}")

    def _ensure_unique_date(self, event: model.Event, exclude_id: str = None):
        for existing in self._event_db.list():
            if existing.date == event.date and existing.id != exclude_id:
                raise LogicException(f"event already exists for date: {event.date}")

    def create(self, event: model.Event) -> str:
        self._validate_event(event)
        self._ensure_unique_date(event)
        try:
            return self._event_db.create(event)
        except Exception as ex:
            raise LogicException(f"failed CREATE operation with: {ex}")

    def list(self) -> List[model.Event]:
        try:
            return self._event_db.list()
        except Exception as ex:
            raise LogicException(f"failed LIST operation with: {ex}")

    def read(self, _id: str) -> model.Event:
        try:
            return self._event_db.read(_id)
        except Exception as ex:
            raise LogicException(f"failed READ operation with: {ex}")

    def update(self, _id: str, event: model.Event):
        self._validate_event(event)
        self._ensure_unique_date(event, exclude_id=_id)
        try:
            return self._event_db.update(_id, event)
        except Exception as ex:
            raise LogicException(f"failed UPDATE operation with: {ex}")

    def delete(self, _id: str):
        try:
            return self._event_db.delete(_id)
        except Exception as ex:
            raise LogicException(f"failed DELETE operation with: {ex}")
