class TestRegionEndpoint:
    endpoint = "http://127.0.0.1:7000/graphql/"

    def test_get_all_regions(self, api_client):
        query = """
            query {
                regions {
                    id
                    name
                    slug
                    postCode
                    numberOfDistricts
                }
            }
            """
        executed = api_client(query=query)
        assert executed == {"data": {"hey": "hello Peter!"}}

    def test_get_all_regions(self, api_client):
        query = """
            query{
                region(slug:"kilimanjaro"){
                    id
                }
            }
            """
        executed = api_client(query=query)
        assert executed == {"data": {"region": {"id": "11"}}}
