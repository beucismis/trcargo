import requests


def request_page(session: requests.Session, request: requests.Request) -> requests.Response:
    prepped = request.prepare()
    response = session.send(prepped)
    response.raise_for_status()

    return response
