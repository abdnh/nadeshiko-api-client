from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal


@dataclass
class SentenceSearchRequest:
    # Text or sentence to search
    query: str
    # Max amount of entries by response
    limit: int | None = None
    # Unique ID from sentence (Useful to get a specific sentence)
    uuid: str | None = None
    # Anime, Liveaction
    category: int | None = None
    # Unique ID from media
    anime_id: int | None = None
    # Array of seasons to get
    season: int | None = None
    # Array of episodes to get
    episode: list[int] | None = None
    # A value from 0 to 1
    random_seed: float | None = None
    # Order by amount of characters
    content_sort: Literal["ASC", "DESC"] = "ASC"
    # Current page of search
    cursor: list[int] = field(default_factory=lambda: [0])


@dataclass
class Statistic:
    anime_id: int | None = None
    category: int | None = None
    name_anime_romaji: str | None = None
    name_anime_en: str | None = None
    name_anime_jp: str | None = None
    amount_sentences_found: int | None = None
    season_with_episode_hits: dict[str, dict[str, int]] | None = None


@dataclass
class CategoryStatistic:
    category: int | None = None
    count: int | None = None


@dataclass
class BasicInfo:
    id_anime: int | None = None
    name_anime_romaji: str | None = None
    name_anime_en: str | None = None
    name_anime_jp: str | None = None
    cover: str | None = None
    banner: str | None = None
    episode: int | None = None
    season: int | None = None
    category: int | None = None


@dataclass
class SegmentInfo:
    status: int | None = None
    uuid: str | None = None
    position: int | None = None
    start_time: str | None = None
    end_time: str | None = None
    content_jp: str | None = None
    content_jp_highlight: str | None = None
    content_en: str | None = None
    content_en_highlight: str | None = None
    content_en_mt: bool | None = None
    content_es: str | None = None


@dataclass
class MediaInfo:
    path_image: str | None = None
    path_audio: str | None = None
    path_video: str | None = None


@dataclass
class Sentence:
    basic_info: BasicInfo | None = None
    segment_info: SegmentInfo | None = None
    media_info: MediaInfo | None = None


@dataclass
class ResponseV1:
    statistics: list[Statistic] | None = None
    categoryStatistics: list[CategoryStatistic] | None = None
    sentences: list[Sentence] | None = None
    cursor: list[int | float] | None = None
