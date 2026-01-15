from __future__ import annotations

import dataclasses
import http.client
import json
from http import HTTPStatus
from typing import Any, TypeVar

from dacite import from_dict

from .exceptions import NadeshikoException
from .models import ResponseV1, SentenceSearchRequest

T = TypeVar("T")


class Client:
    def __init__(self, token: str) -> None:
        self.connection = http.client.HTTPSConnection("api.brigadasos.xyz")
        self.token = token

    def _request(self, method: str, path: str, payload: Any, response_type: type[T]) -> T:
        headers = {"Content-Type": "application/json", "X-API-Key": self.token}
        self.connection.request(method, f"/api/v1/{path}", json.dumps(payload), headers)
        res = self.connection.getresponse()
        if res.status != HTTPStatus.OK:
            raise NadeshikoException(res.read().decode())
        data = json.loads(res.read())
        return from_dict(response_type, data)

    def search_sentence(self, request: SentenceSearchRequest) -> ResponseV1:
        response = self._request("POST", "search/media/sentence", dataclasses.asdict(request), ResponseV1)
        return response
