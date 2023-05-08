import asyncio
import sys
from src.libertywrapper.base.config import USERNAME, PASSWORD

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
    def test_user_get(self):
        import src.libertywrapper.bot as bot
        wrapper = bot.Wrapper(username=USERNAME, password=PASSWORD)

        player = wrapper.fetch_user("agapeioan")
        self.assertTrue(wrapper.fetcher.token)
        self.assertTrue(player)

        original_token = wrapper.fetcher.token

        users = [" a", ".!,)6", "gdyjgfukk", "xh hc iv"]
        for user in users:
            player = wrapper.fetch_user(user)
            self.assertEqual(wrapper.fetcher.token, original_token)
            self.assertFalse(player)
    """