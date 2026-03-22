from __future__ import annotations

import dataclasses
from http import HTTPStatus
from typing import Any

import requests

from .exceptions import NadeshikoException
from .models import SearchRequest, SearchResponse, Segment


class Client:
    def __init__(self, token: str) -> None:
        self.session = requests.Session()
        self.token = token

    def _request(self, method: str, path: str, payload: Any) -> Any:
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.token}"}
        response = self.session.request(
            method=method, url=f"https://api.nadeshiko.co/v1/{path}", json=payload, headers=headers
        )
        if response.status_code != HTTPStatus.OK:
            raise NadeshikoException(response.text)
        return response.json()

    def search(self, request: SearchRequest) -> SearchResponse:
        payload = dataclasses.asdict(request)
        payload["query"]["exactMatch"] = payload["query"].pop("exact_match")
        response_dict = self._request("POST", "search", payload)
        segments: list[Segment] = []
        for segment in response_dict.get("segments", []):
            segments.append(Segment(public_id=segment["publicId"], text=segment["textJa"]["content"]))
        response = SearchResponse(segments)
        return response
