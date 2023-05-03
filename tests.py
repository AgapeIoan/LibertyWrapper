import asyncio
import sys

# check if windows
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) 
    # https://stackoverflow.com/questions/68123296/asyncio-throws-runtime-error-with-exception-ignored

import unittest

class TestLibertyWrapper(unittest.TestCase):
    def test_import(self):
        import src.libertywrapper
        self.assertTrue(src.libertywrapper)

    def test_import_bot(self):
        from src.libertywrapper import bot
        self.assertTrue(bot)

class TestData(unittest.TestCase):
    # def __init__(self, methodName: str = "runTest") -> None:
    #     super().__init__(methodName)

    def test_classes(self):
        import src.libertywrapper.bot as bot
        wrapper = bot.Wrapper()

        general = wrapper.fetch_homepage()
        staff = wrapper.fetch_staff()
        onlineplayers = wrapper.fetch_online_players()
        mapblips = wrapper.fetch_mapblips()
        usersearch = wrapper.search_user("Agape")
        factions = wrapper.fetch_factions()
        # player = wrapper.fetch_user("AgapeIoan")

        self.assertTrue(general)
        self.assertTrue(staff)
        self.assertTrue(onlineplayers)
        self.assertTrue(mapblips)
        self.assertTrue(usersearch)
        self.assertTrue(factions)
        # self.assertTrue(player)

    def test_user_search(self):
        import src.libertywrapper.bot as bot
        wrapper = bot.Wrapper()
        users = ["kseny", "a", "libertystats"]
        for user in users:
            result = wrapper.search_user(user)
            print(result)
            self.assertTrue(result)

        users = [" a", ".!,)6", "gdyjgfukk", "xh hc iv"]
        for user in users:
            result = wrapper.search_user(user)
            print(result)
            self.assertFalse(result)

"""
class TestFactionMethods(unittest.TestCase):
    def test_factions_get(self):
        faction_data = data.Factions()
        factions = faction_data.get(id=1)
        self.assertTrue(factions)
        factions = faction_data.get(name="Downtown Taxi Company")
        self.assertTrue(factions)
        factions = faction_data.get(name="Downtown Taxi Company", id=1)
        self.assertTrue(factions)
        factions = faction_data.get(name="asd")
        self.assertFalse(factions)
        factions = faction_data.get(id=99)
        self.assertFalse(factions)
"""
