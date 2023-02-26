import asyncio
import json
import aiohttp

class Fetcher:
    def __init__(self, api_address):
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

        async def get_map_blips():
            return await Fetcher("/general/map/blips").get_json()


    class Player:
        def __init__(self, nickname):
            self.nickname = nickname

        async def get_online_players(self):
            return await Fetcher("/general/online").get_json()

        async def search_player(self):
            return await Fetcher(f"/user/search/{self.nickname}").get_json()


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
            

class GeneralUser:
    def __init__(self, avatar, name, level, playtime, faction=None, money=None, quests=None):
        self.avatar = avatar # data["UserAvatar"]
        self.name = name # data["name"]
        self.level = level # data["Level"]
        self.playtime = playtime # data["Playtime"]
        self.faction = faction # data["Faction"] | top_users_last_week_activity, top_users_activity
        self.money = money # data["money"] | top_users_jobs
        self.quests = quests # data["DailyQuestsStats"] | top_users_quests, top_users_last_week_activity

    class Faction:
        def __init__(self, faction):
            self.name = faction["Name"]

    class DailyQuests:
        def __init__(self, quests):
            self.streak = quests["streak"]
            self.completed = quests["completed"]
            self.longest_streak = quests["longest_streak"]

if __name__ == "__main__":
    x = asyncio.run(Fetcher.General.get_stats())
    print(x)
    with open("test.json", "w") as f:
        json.dump(x, f, indent=4)