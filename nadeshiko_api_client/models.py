from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SearchQuery:
    search: str
    exact_match: bool = False


@dataclass
class SearchRequest:
    query: SearchQuery
    take: int


@dataclass
class Segment:
    public_id: str
    text: str


@dataclass
class SearchResponse:
    segments: list[Segment]
