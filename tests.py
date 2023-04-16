import asyncio
from src.libertywrapper.data import Faction
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) 
# https://stackoverflow.com/questions/68123296/asyncio-throws-runtime-error-with-exception-ignored

import unittest
from src.libertywrapper import data, fetcher

class TestLibertyWrapper(unittest.TestCase):
    def test_import(self):
        import src.libertywrapper
        self.assertTrue(src.libertywrapper)

    def test_import_fetcher(self):
        from src.libertywrapper import fetcher
        self.assertTrue(fetcher)

    def test_import_data(self):
        from src.libertywrapper import data
        self.assertTrue(data)

class TestFaction(unittest.TestCase):
    def test_factions_get(self):
        faction_data = data.Factions()
        factions = faction_data.get(1)
        self.assertTrue(factions)
        factions = faction_data.get(name="Downtown Taxi Company")
        self.assertTrue(factions)
        factions = faction_data.get(name="Downtown Taxi Company", id=1)
        self.assertTrue(factions)
        factions = faction_data.get(name="asd")
        self.assertFalse(factions)
        factions = faction_data.get(id=99)
        self.assertFalse(factions)

class TestFetcher(unittest.TestCase):
    fetcher = fetcher.Fetcher
    
    general = fetcher.General
    user = fetcher.User
    forum = fetcher.Forum
    faction = fetcher.Faction

    def test_general_stats(self):
        stats = self.general.get_stats()
        self.assertTrue(stats)

    def test_general_staff(self):
        staff = self.general.get_staff()
        self.assertTrue(staff)

    def test_general_map_blips(self):
        map_blips = self.general.get_map_blips()
        self.assertTrue(map_blips)

    def test_general_online_players(self):
        online_players = self.general.get_online_players()
        self.assertTrue(online_players)

    def test_user_search(self):
        user = self.user.search_user('agape')
        print(user)
        self.assertTrue(user)
    
    # def test_user_get(self):
    #     user = self.user.get_user("Agape")
    #     self.assertTrue(user)
    # nu avem token yet

    def test_forum_categories(self):
        categories = self.forum.get_forum_categories()
        self.assertTrue(categories)

    def test_forum_chat_messages(self):
        chat_messages = self.forum.get_chat_messages()
        self.assertTrue(chat_messages)

    def test_forum_chat_latest(self):
        chat_latest = self.forum.get_chat_latest()
        self.assertTrue(chat_latest)

    def test_faction_list(self):
        faction_list = self.faction.get_faction_list()
        self.assertTrue(faction_list)

    def test_faction_get(self):
        faction = self.faction.get_faction_history()
        self.assertTrue(faction)

    def test_faction_applications(self):
        faction_applications = self.faction.get_faction_applications()
        self.assertTrue(faction_applications)
