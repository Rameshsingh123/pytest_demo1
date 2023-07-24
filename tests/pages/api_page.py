import requests


class ExampleAPIPage:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_data(self):
        url = f"{self.base_url}/endpoint"
        response = requests.get(url)
        return response

    def post_data(self, data, headers):
        url = f"{self.base_url}/another_endpoint"
        response = requests.post(url, json=data, headers=headers)
        return response
