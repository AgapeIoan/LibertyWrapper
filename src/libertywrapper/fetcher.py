import asyncio
import json
import requests

def check_json_status(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        if response.get("status") == "SUCCESS":
            return response
        else:
            raise Exception(f"Error on fetching the data. Status: {response.get('status')} | Message: {response.get('message')}")
    return wrapper

def check_json_status(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        if response.get("status") == "SUCCESS":
            return response
        else:
            raise Exception(f"Error on fetching the data. Status: {response.get('status')} | Message: {response.get('message')}")
    return wrapper

class Fetcher:
    api_url = "https://backend-beta.liberty.mp"
    def __init__(self, api_address=''):
        self.api_address = api_address
        self.url = f'{self.api_url}{self.api_address}'
        self.session = requests.Session()

    def get(self) -> str:
        with self.session as session:
            with session.get(self.url) as response:
                return response.text()

    @check_json_status
    def get_json(self) -> dict:
        with self.session as session:
            with session.get(self.url) as response:
                if response.status_code == 200:
                    return response.json()
                else:
                    raise Exception(f"Error on fetching the data. Status: {response.status}")

class General(Fetcher):
    def get_stats() -> dict:
        return Fetcher("/general/stats").get_json()

    def get_staff() -> dict:
        return Fetcher("/general/staff").get_json()

    def get_map_blips() -> dict:
        return Fetcher("/general/map/blips").get_json()

    def get_online_players() -> dict:
        return Fetcher("/general/online").get_json()


class User(Fetcher):
    def search_user(nickname) -> dict:
        if not nickname:
            raise Exception("Nickname not specified")
        return Fetcher(f"/user/search/{nickname}").get_json()
    
    def get_user(nickname) -> dict:
        # O sa dea eroare ca datele astea se obtin cu user token, nu sunt publice
        # Se rezolva cu login si sesiune salvata in pickle, handling la cookies sa fie reinnoite daca expira and stuff
        if not nickname:
            raise Exception("Nickname not specified")
        return Fetcher(f"/user/profile/{nickname}").get_json()


class Forum(Fetcher):
    def get_forum_categories() -> dict:
        return Fetcher("/forum/categories").get_json()

    def get_chat_messages() -> dict:
        return Fetcher("/chat/messages").get_json()

    def get_chat_latest() -> dict:
        return Fetcher("/chat/latest/1").get_json()


class Faction(Fetcher):
    def get_faction_list() -> dict:
        return Fetcher("/faction/list").get_json()

    def get_faction_history() -> dict:
        return Fetcher("/faction/history").get_json()

    def get_faction_applications() -> dict:
        return Fetcher("/faction/applications/statistics").get_json()
        
if __name__ == "__main__":
    # asyncio.run(UpdateCache.update_map_blips())
    x = asyncio.run(Fetcher.Player().search_player("test"))
    print(x)
    with open("test.json", "w") as f:
        json.dump(x, f, indent=4)