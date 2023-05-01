from .base.interiors import FactionInteriorHQ, FactionGarage
from .base.user import FactionUser

class Faction:
    def __init__(self, data):
        self.id = data.get("id")
        self.name = data.get("Name")
        self.type = data.get("Type")
        self.chat_status = data.get("ChatStatus")
        self.hq_status = data.get("HQStatus")
        self.location = tuple(data.get("Location").values()) # (x, y, z)
        self.blip_model = data.get("BlipModel")
        self.blip_color = data.get("BlipColor")
        
        self.has_interior = data.get("HasInterior")
        self.interior = FactionInteriorHQ(data.get("Interior")) # if self.has_interior == "true" else None
        
        self.has_garage = data.get("HasGarage")
        self.garage = FactionGarage(data.get("Garage")) # if self.has_garage == "true" else None

        self.ranks = data.get("Ranks")
        self.max_members = data.get("MaxMembers")
        self.min_level = data.get("MinLevel")
        self.applications = data.get("Applications")
        self.applications_questions = data.get("ApplicationsQuestions")
        self.penalty_reasons = data.get("PenaltyReasons")
        self.users = [FactionUser(**user) for user in data.get("users")]

    def repr(self):
        return f"Faction(id={self.id}, name={self.name}, type={self.type}, chat_status={self.chat_status}, hq_status={self.hq_status}, location={self.location}, blip_model={self.blip_model}, blip_color={self.blip_color}, has_interior={self.has_interior}, interior={self.interior}, has_garage={self.has_garage}, garage={self.garage}, ranks={self.ranks}, max_members={self.max_members}, min_level={self.min_level}, applications={self.applications}, applications_questions={self.applications_questions}, penalty_reasons={self.penalty_reasons}, users={self.users})"

    def __repr__(self):
        return self.repr()

    def __iter__(self):
        return iter(self.__dict__.items())
