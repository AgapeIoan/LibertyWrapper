import requests
import os
import json

from .user import BriefUser, UserSearchResult
from .game import MapBlip
from .player import Player
from .general import General
from .faction import Faction
from .staff import Staff
from .base.data import Log

from .base.config import USERNAME, PASSWORD


def check_json_status(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        if response.get("status") == "SUCCESS":
            return response
        else:
            raise Exception(f"Error on fetching the data. Status: {response.get('status')} | Message: {response.get('message')}")
    return wrapper

class Fetcher:
    api_url = "https://backend.liberty.mp"
    def __init__(self, api_address='', username='', password=''):
        self.api_address = api_address
        self.url = f'{self.api_url}{self.api_address}'
        self.session = requests.Session()
        
        self.token = ""
        self.username = username
        self.password = password

        self.latest_result = None

    def get(self) -> str:
        with self.session as session:
            with session.get(self.url) as response:
                return response.text

    @check_json_status
    def get_json(self, auth=None, headers=None, offline=False) -> dict:
        if offline:
            with open(f"storage/offline{self.api_address}/data.json", "r") as f:
                return json.load(f)
        if auth:
            headers = {"authorization": f"Bearer {auth}"}
        with self.session as session:
            with session.get(self.url, headers=headers) as response:
                if response.status_code == 200:
                    return response.json()
                elif response.status_code == 503:
                    print(response.text)
                    raise Exception(f"Response code: {response.status_code} | Service Unavailable")
                else:
                    print(response.text)
                    raise Exception(f"Error on fetching the data. Response: {response.text}")

    def login(self, username, password) -> dict:
        if not username or not password:
            raise Exception("Username or password not provided!")
        return self.session.post(
            f"{self.api_url}/user/login",
            data={"name": username, "password": password},
        ).json()

    def init_token(self, username, password): # TODO Return type -> str or None
        if not username or not password:
            raise Exception("Username or password not provided!")
        print("Debug: token")
        self.token = self.login(username, password).get("token")
        return self.token

    def search_user(self, nickname) -> dict:
        if not nickname:
            raise Exception("Nickname not specified")
        self.latest_result = Fetcher(f"/user/search/{nickname}").get_json()
        return self.latest_result
    
    def get_user(self, nickname, auth=None) -> dict:
        if not nickname:
            raise Exception("Nickname not specified")
        if not auth:
            auth = self.token
        self.latest_result = Fetcher(f"/user/profile/{nickname}").get_json(auth=auth)
        return self.latest_result

    def get_stats(self) -> dict:
        self.latest_result = Fetcher("/general/stats").get_json()
        return self.latest_result

    def get_staff(self) -> dict:
        self.latest_result = Fetcher("/general/staff").get_json()
        return self.latest_result

    def get_map_blips(self) -> dict:
        self.latest_result = Fetcher("/general/map/blips").get_json()
        return self.latest_result

    def get_online_players(self) -> dict:
        self.latest_result = Fetcher("/general/online").get_json()
        return self.latest_result

    def get_forum_categories(self) -> dict:
        self.latest_result = Fetcher("/forum/categories").get_json()
        return self.latest_result

    def get_chat_messages(self) -> dict:
        self.latest_result = Fetcher("/chat/messages").get_json()
        return self.latest_result

    def get_chat_latest(self) -> dict:
        self.latest_result = Fetcher("/chat/latest/1").get_json()
        return self.latest_result

    def get_faction_list(self) -> dict:
        self.latest_result = Fetcher("/faction/list").get_json()
        return self.latest_result

    def get_faction_history(self) -> dict:
        self.latest_result = Fetcher("/faction/history").get_json()
        return self.latest_result

    def get_faction_applications(self) -> dict:
        self.latest_result = Fetcher("/faction/applications/statistics").get_json()
        return self.latest_result

    def save_offline_data(self):
        # TODO Delete on stable release
        dir = "storage/offline"
        if not os.path.exists(dir):
            os.makedirs(dir)

        os.makedirs(dir + "/user/profile", exist_ok=True)
        os.makedirs(dir + "/user/search/Agape", exist_ok=True)
        os.makedirs(dir + "/general/stats", exist_ok=True)
        os.makedirs(dir + "/general/staff", exist_ok=True)
        os.makedirs(dir + "/general/map/blips", exist_ok=True)
        os.makedirs(dir + "/general/online", exist_ok=True)
        os.makedirs(dir + "/forum/categories", exist_ok=True)
        os.makedirs(dir + "/chat/messages", exist_ok=True)
        os.makedirs(dir + "/chat/latest/1", exist_ok=True)
        os.makedirs(dir + "/faction/list", exist_ok=True)
        os.makedirs(dir + "/faction/history", exist_ok=True)
        os.makedirs(dir + "/faction/applications/statistics", exist_ok=True)

        with open(dir + "/general/stats/data.json", "w+", encoding='utf-8') as f:
            f.write(json.dumps(self.get_stats(), indent=4))
        
        with open(dir + "/general/staff/data.json", "w+", encoding='utf-8') as f:
            f.write(json.dumps(self.get_staff(), indent=4))

        with open(dir + "/general/map/blips/data.json", "w+", encoding='utf-8') as f:
            f.write(json.dumps(self.get_map_blips(), indent=4))

        with open(dir + "/general/online/data.json", "w+", encoding='utf-8') as f:
            f.write(json.dumps(self.get_online_players(), indent=4))

        with open(dir + "/forum/categories/data.json", "w+", encoding='utf-8') as f:
            f.write(json.dumps(self.get_forum_categories(), indent=4))

        with open(dir + "/chat/messages/data.json", "w+", encoding='utf-8') as f:
            f.write(json.dumps(self.get_chat_messages(), indent=4))

        with open(dir + "/chat/latest/data.json", "w+", encoding='utf-8') as f:
            f.write(json.dumps(self.get_chat_latest(), indent=4))

        with open(dir + "/faction/list/data.json", "w+", encoding='utf-8') as f:
            f.write(json.dumps(self.get_faction_list(), indent=4))

        with open(dir + "/faction/history/data.json", "w+", encoding='utf-8') as f:
            f.write(json.dumps(self.get_faction_history(), indent=4))

        with open(dir + "/faction/applications/statistics/data.json", "w+", encoding='utf-8') as f:
            f.write(json.dumps(self.get_faction_applications(), indent=4))
        
        with open(dir + "/user/search/Agape/data.json", "w+", encoding='utf-8') as f:
            f.write(json.dumps(self.search_user("Agape"), indent=4))

        print("Data saved successfully!")

class Wrapper:
    def __init__(self, username=USERNAME, password=PASSWORD):
        self.bot = None
        self.fetcher = Fetcher(username=username, password=password)
        self.username = username
        self.password = password

    def fetch_online_players(self):
        data = self.fetcher.get_online_players().get("users")
        if data:
            return [BriefUser(**x) for x in data]
        return None

    def fetch_homepage(self):
        data = self.fetcher.get_stats()
        return General(data)

    def fetch_mapblips(self):
        data = self.fetcher.get_map_blips().get("blips")
        if data:
            return [MapBlip(x) for x in data]
        return None

    def fetch_factions(self):
        data = self.fetcher.get_faction_list()
        factions = data.get("factions")
        if factions:
            return [Faction(faction) for faction in factions]
        return None

    def fetch_faction_history(self):
        data = self.fetcher.get_faction_history()
        logs = data.get("history")
        if logs:
            return [Log(log) for log in data]
        return None

    def fetch_staff(self):
        data = self.fetcher.get_staff()
        return Staff(data.get("staff"))

    def search_user(self, nickname):
        data = self.fetcher.search_user(nickname)
        results = data.get("users")
        if results:
            return [UserSearchResult(**result) for result in results]
        return None

    def fetch_user(self, nickname):
        if not self.fetcher.token:
            self.fetcher.init_token(self.username, self.password)
        try:
            data = self.fetcher.get_user(nickname)
        except Exception as e:
            # Status: ERROR | Message: User not found.
            return None
        if data:
            player = Player(data.get("user"))
            return player
        return None
