import os

from nadeshiko_api_client.client import Client
from nadeshiko_api_client.models import SentenceSearchRequest

client = Client(os.environ["NADESHIKO_API_KEY"])
response = client.search_sentence(SentenceSearchRequest(query="行方不明", limit=50))

if response.sentences:
    for sentence in response.sentences:
        if sentence.segment_info:
            print(sentence.segment_info.content_jp)
