import pytest
from graphene.test import Client
from graphene_django.utils.testing import graphql_query

from geodata.schema import schema


@pytest.fixture
def api_client():
    client = Client(schema)

    def do_create_query(query):
        client.execute(query)

    return do_create_query
