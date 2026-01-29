from __future__ import annotations

import dataclasses
from http import HTTPStatus
from typing import Any, TypeVar

import requests
from dacite import from_dict

from .exceptions import NadeshikoException
from .models import ResponseV1, SentenceSearchRequest

T = TypeVar("T")


class Client:
    def __init__(self, token: str) -> None:
        self.session = requests.Session()
        self.token = token

    def _request(self, method: str, path: str, payload: Any, response_type: type[T]) -> T:
        headers = {"Content-Type": "application/json", "X-API-Key": self.token}
        response = self.session.request(
            method=method, url=f"https://api.brigadasos.xyz/api/v1/{path}", json=payload, headers=headers
        )
        if response.status_code != HTTPStatus.OK:
            raise NadeshikoException(response.text)
        return from_dict(response_type, response.json())

    def search_sentence(self, request: SentenceSearchRequest) -> ResponseV1:
        response = self._request("POST", "search/media/sentence", dataclasses.asdict(request), ResponseV1)
        return response
