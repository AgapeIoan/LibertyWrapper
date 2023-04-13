import asyncio
import json
import aiohttp
import datetime

CACHE = {}
with open("storage/map_blips.json", "r") as f:
    CACHE["map_blips"] = json.load(f)

def check_json_status(func):
    async def wrapper(*args, **kwargs):
        response = await func(*args, **kwargs)
        if response.get("status") == "SUCCESS":
            return response
        else:
            raise Exception(f"Error on fetching the data. Status: {response.get('status')} | Message: {response.get('message')}")
    return wrapper

def check_json_status(func):
    async def wrapper(*args, **kwargs):
        response = await func(*args, **kwargs)
        if response.get("status") == "SUCCESS":
            return response
        else:
            raise Exception(f"Error on fetching the data. Status: {response.get('status')} | Message: {response.get('message')}")
    return wrapper

class UpdateCache:
    async def update_map_blips():
        CACHE["map_blips"] = await Fetcher.General.get_map_blips(cache=False)
        with open("storage/map_blips.json", "w") as f:
            json.dump(CACHE["map_blips"], f, indent=4)

class Fetcher:
    api_url = "https://backend-beta.liberty.mp"
    def __init__(self, api_address=''):
        self.api_address = api_address
        self.url = f'{self.api_url}{self.api_address}'
        self.session = aiohttp.ClientSession()

    async def get(self) -> str:
        async with self.session as session:
            async with session.get(self.url) as response:
                return await response.text()

    @check_json_status
    async def get_json(self) -> dict:
        async with self.session as session:
            async with session.get(self.url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    raise Exception(f"Error on fetching the data. Status: {response.status}")

    class General:
        async def get_stats() -> dict:
            return await Fetcher("/general/stats").get_json()

        async def get_staff() -> dict:
            return await Fetcher("/general/staff").get_json()

        async def get_map_blips(cache=True) -> dict:
            if cache:
                # Recomand cache=True si UpdateCache from time to time
                return CACHE["map_blips"]
            else:
                return await Fetcher("/general/map/blips").get_json()

        async def get_online_players() -> dict:
            return await Fetcher("/general/online").get_json()


    class User:
        async def search_user(self, nickname) -> dict:
            if not nickname:
                raise Exception("Nickname not specified")
            return await Fetcher(f"/user/search/{nickname}").get_json()
        
        async def get_user(self, nickname) -> dict:
            # O sa dea eroare ca datele astea se obtin cu user token, nu sunt publice
            # Se rezolva cu login si sesiune salvata in pickle, handling la cookies sa fie reinnoite daca expira and stuff
            if not nickname:
                raise Exception("Nickname not specified")
            return await Fetcher(f"/user/profile/{nickname}").get_json()


    class Forum:
        async def get_forum_categories() -> dict:
            return await Fetcher("/forum/categories").get_json()

        async def get_chat_messages() -> dict:
            return await Fetcher("/chat/messages").get_json()

        async def get_chat_latest() -> dict:
            return await Fetcher("/chat/latest/1").get_json()


    class Faction:
        async def get_faction_list() -> dict:
            return await Fetcher("/faction/list").get_json()

        async def get_faction_history() -> dict:
            return await Fetcher("/faction/history").get_json()

        async def get_faction_applications() -> dict:
            return await Fetcher("/faction/applications/statistics").get_json()
            
if __name__ == "__main__":
    # asyncio.run(UpdateCache.update_map_blips())
    x = asyncio.run(Fetcher.Player().search_player("test"))
    print(x)
    with open("test.json", "w") as f:
        json.dump(x, f, indent=4)