import os

from nadeshiko_api_client.client import Client
from nadeshiko_api_client.models import SearchRequest, SearchQuery

client = Client(os.environ["NADESHIKO_API_KEY"])
response = client.search(SearchRequest(query=SearchQuery(search="行方不明"), take=50))
for segment in response.segments:
    print(segment.text)
