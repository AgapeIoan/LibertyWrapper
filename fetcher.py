import asyncio
import json
import aiohttp
import datetime

CACHE = {}
with open("storage/map_blips.json", "r") as f:
    CACHE["map_blips"] = json.load(f)

class UpdateCache:
    async def update_map_blips():
        CACHE["map_blips"] = await Fetcher.General.get_map_blips(cache=False)
        with open("storage/map_blips.json", "w") as f:
            json.dump(CACHE["map_blips"], f, indent=4)

class Fetcher:
    def __init__(self, api_address=''):
        self.api_address = api_address
        self.api_url = "https://backend.liberty.mp"
        self.url = self.api_url + self.api_address

    async def get(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                return await response.text()

    async def get_json(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                return await response.json()

    class General:
        async def get_stats():
            return await Fetcher("/general/stats").get_json()

        async def get_staff():
            return await Fetcher("/general/staff").get_json()

        async def get_map_blips(cache=True):
            if cache:
                # Recomand cache=True si UpdateCache from time to time
                return CACHE["map_blips"]
            else:
                return await Fetcher("/general/map/blips").get_json()

        async def get_online_players(self):
            return await Fetcher("/general/online").get_json()


    class Player:
        async def search_player(self, nickname):
            if not nickname:
                raise Exception("Nickname not specified")
            return await Fetcher(f"/user/search/{nickname}").get_json()
        
        async def get_player(self, nickname):
            # O sa dea eroare ca datele astea se obtin cu user token, nu sunt publice
            # Se rezolva cu login si sesiune salvata in pickle, handling la cookies sa fie reinnoite daca expira and stuff
            if not nickname:
                raise Exception("Nickname not specified")
            return await Fetcher(f"/user/profile/{nickname}").get_json()


    class Forum:
        async def get_forum_categories():
            return await Fetcher("/forum/categories").get_json()

        async def get_chat_messages():
            return await Fetcher("/chat/messages").get_json()

        async def get_chat_latest():
            return await Fetcher("/chat/latest/1").get_json()


    class Faction:
        async def get_faction_list():
            return await Fetcher("/faction/list").get_json()

        async def get_faction_history():
            return await Fetcher("/faction/history").get_json()

        async def get_faction_applications():
            return await Fetcher("/faction/applications/statistics").get_json()
            
if __name__ == "__main__":
    # asyncio.run(UpdateCache.update_map_blips())
    x = asyncio.run(Fetcher.Player().search_player("test"))
    print(x)
    with open("test.json", "w") as f:
        json.dump(x, f, indent=4)