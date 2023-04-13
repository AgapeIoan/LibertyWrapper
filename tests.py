import asyncio
from src.libertywrapper.data import Faction
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) 
# https://stackoverflow.com/questions/68123296/asyncio-throws-runtime-error-with-exception-ignored

import unittest
from libertywrapper import data


class TestLibertyWrapper(unittest.TestCase):
    def test_import(self):
        import libertywrapper
        self.assertTrue(libertywrapper)

    def test_import_fetcher(self):
        from libertywrapper import fetcher
        self.assertTrue(fetcher)

    def test_import_data(self):
        from libertywrapper import data
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