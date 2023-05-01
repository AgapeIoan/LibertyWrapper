import datetime

from .base.user import GenericUser
from .base.faction import BriefFaction
from .base.staff import StaffPerms

class BriefUser(GenericUser):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = kwargs.get("id")
        
        if kwargs.get("FactionRank"):
            faction = kwargs.get("faction")
            self.faction = BriefFaction(faction.get("name"), faction.get("type"), kwargs.get("Faction"), kwargs.get("FactionRank"))
        else:
            self.faction = None

    def repr(self):
        return f"BriefUser(avatar={self.avatar}, name={self.name}, level={self.level}, playtime={self.playtime}, id={self.id}, faction={self.faction})"

    def __iter__(self):
        pass

class UserSearchResult(BriefUser):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.perms = StaffPerms(kwargs.get("sPermissions"))

    def repr(self):
        return f"UserSearchResult(avatar={self.avatar}, name={self.name}, level={self.level}, playtime={self.playtime}, id={self.id}, faction={self.faction}, perms={self.perms})"

    def __iter__(self):
        pass

class GenericStaffUser(GenericUser):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = kwargs.get("id")
        self.status = kwargs.get("Status") == "true"
        self.faction_id = kwargs.get("Faction") if isinstance(kwargs.get("Faction"), int) else None
        # 2023-05-01T05:21:33.091Z
        self.last_seen = datetime.datetime.strptime(kwargs.get("updatedAt"), "%Y-%m-%dT%H:%M:%S.%fZ") if kwargs.get("LastSeen") else None
        # playtime o sa fie 0

    def repr(self):
        return f"GenericStaffUser(avatar={self.avatar}, name={self.name}, level={self.level}, playtime={self.playtime}, id={self.id}, status={self.status}, faction_id={self.faction_id}, last_seen={self.last_seen})"

    def __iter__(self):
        pass

class StaffUserAdministrator(GenericStaffUser):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.perms = StaffPerms(kwargs.get("sPermissions"))
        #self.admin_label = **kwargs.get("AdminLabel")

    def repr(self):
        return f"StaffUserAdministrator(avatar={self.avatar}, name={self.name}, level={self.level}, playtime={self.playtime}, id={self.id}, status={self.status}, faction_id={self.faction_id}, last_seen={self.last_seen}, perms={self.perms})"

    def __iter__(self):
        pass

class StaffUserLeader(GenericStaffUser):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.faction = BriefFaction(name=kwargs.get("Name"), type=kwargs.get("Type"))

    def repr(self):
        return f"StaffUserLeader(avatar={self.avatar}, name={self.name}, level={self.level}, playtime={self.playtime}, id={self.id}, status={self.status}, faction_id={self.faction_id}, last_seen={self.last_seen}, faction={self.faction})"
