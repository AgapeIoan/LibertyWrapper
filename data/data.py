import datetime
from fetcher import Fetcher
import asyncio

class General:
    def __init__(self):
        # data = Fetcher.General.get_stats()
        data = asyncio.run(Fetcher.General.get_stats())

        self.total_users = data.get("total_users")
        self.total_online = data.get("total_online")
        self.total_vehicles = data.get("total_vehicles")
        self.total_houses = data.get("total_houses")
        self.total_apartments = data.get("total_apartments")
        self.total_posts = data.get("total_posts")

        self.top_users_activity = [UserActivity(**x) for x in data.get("top_users_activity")]
        self.top_users_last_week_activity = [UserQuestsActivity(**x) for x in data.get("top_users_last_week_activity")]
        self.top_users_quests = [UserQuestsActivity(**x) for x in data.get("top_users_quests")]
        self.top_users_jobs = [UserJobsActivity(**x) for x in data.get("top_users_jobs")]
        
        self.online_history = [ServerOnlineHistory(x) for x in data.get("online_history")]

    def repr(self):
        return f"General(total_users={self.total_users}, total_online={self.total_online}, total_vehicles={self.total_vehicles}, total_houses={self.total_houses}, total_apartments={self.total_apartments}, total_posts={self.total_posts}, top_users_activity={self.top_users_activity}, top_users_last_week_activity={self.top_users_last_week_activity}, top_users_quests={self.top_users_quests}, top_users_jobs={self.top_users_jobs}, online_history={self.online_history})"

    def __repr__(self):
        return self.repr()

class OnlinePlayers:
    def __init__(self):
        data = asyncio.run(Fetcher.General.get_online_players())
        self.players = [BriefUser(**x) for x in data.get("users")]

    def repr(self):
        return f"OnlinePlayers(players={self.players})"

    def __repr__(self):
        return self.repr()

class Staff:
    def __init__(self):
        data = asyncio.run(Fetcher.General.get_staff())
        data = data.get("staff")

        self.helpers = data.get("helpers")
        self.administrators = data.get("administrators")
        self.leaders = data.get("leaders")

    def repr(self):
        return f"Staff(helpers={self.helpers}, administrators={self.administrators}, leaders={self.leaders})"

    def __repr__(self):
        return self.repr()

# TODO MapBlips si e done General fetcher
class MapBlips:
    def __init__(self):
        data = asyncio.run(Fetcher.General.get_map_blips())

        self.blips = [MapBlip(**x) for x in data.get("blips")]

    def repr(self):
        return f"MapBlips(blips={self.blips})"

    def __repr__(self):
        return self.repr()

class MapBlip:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.position = tuple(kwargs.get("position").values()) # (x, y, z)
        self.name = kwargs.get("name")
        self.scale = kwargs.get("scale")

    def repr(self):
        return f"MapBlip(id={self.id}, position={self.position}, name={self.name}, scale={self.scale})"

    def __repr__(self):
        return self.repr()

class User:
    def __init__(self, **kwargs): # Nu pot face lista de params ca nu am garantia ca primesc date ordonate
        self.avatar = kwargs.get("UserAvatar")
        self.name = kwargs.get("name")
        self.level = kwargs.get("Level")
        self.playtime = datetime.timedelta(seconds=kwargs.get("Playtime"))
    
    def repr(self):
        return f"User(avatar={self.avatar}, name={self.name}, level={self.level}, playtime={self.playtime})"

    def __repr__(self):
        return self.repr()

        
class StaffUser(User):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = kwargs.get("id")
        self.status = kwargs.get("Status") == "true"
        self.faction_id = kwargs.get("Faction") if isinstance(kwargs.get("Faction"), int) else None
        self.last_seen = datetime.datetime.strptime(kwargs.get("LastSeen"), "%Y-%m-%dT%H:%M:%S.%fZ")

    def repr(self):
        return f"StaffUser(avatar={self.avatar}, name={self.name}, level={self.level}, playtime={self.playtime}, id={self.id}, status={self.status}, faction_id={self.faction_id}, last_seen={self.last_seen})"

class StaffUserAdministrator(StaffUser):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.perms = StaffPerms(**kwargs.get("sPermissions"))

    def repr(self):
        return f"StaffUserAdministrator(avatar={self.avatar}, name={self.name}, level={self.level}, playtime={self.playtime}, id={self.id}, status={self.status}, faction_id={self.faction_id}, last_seen={self.last_seen}, perms={self.perms})"

class StaffUserLeader(StaffUser):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.faction = BriefFaction(name=kwargs.get("Name"), type=kwargs.get("Type"))

    def repr(self):
        return f"StaffUserLeader(avatar={self.avatar}, name={self.name}, level={self.level}, playtime={self.playtime}, id={self.id}, status={self.status}, faction_id={self.faction_id}, last_seen={self.last_seen}, faction={self.faction})"

class StaffPerms:
    def __init__(self, **kwargs):
        self.staff = kwargs.get("staff") == "true"
        self.admin = kwargs.get("admin") == "true"
        self.operator = kwargs.get("operator") == "true"
        self.manager = kwargs.get("manager") == "true"
        
class BriefUser(User):
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

class UserActivity(User):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.faction = BriefFaction(kwargs.get("Faction").get("name")) if kwargs.get("Faction") else None

    def repr(self):
        return f"UserActivity(avatar={self.avatar}, name={self.name}, level={self.level}, playtime={self.playtime}, faction={self.faction})"

class UserQuestsActivity(User):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = kwargs.get("id")
        self.quests = DailyQuests(kwargs.get("DailyQuestsStats")) if kwargs.get("DailyQuestsStats") else None

    def repr(self):
        return f"UserQuestsActivity(avatar={self.avatar}, name={self.name}, level={self.level}, playtime={self.playtime}, id={self.id}, quests={self.quests})"

class UserJobsActivity(User):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = kwargs.get("id")
        self.money = kwargs.get("money")

    def repr(self):
        return f"UserJobsActivity(avatar={self.avatar}, name={self.name}, level={self.level}, playtime={self.playtime}, id={self.id}, money={self.money})"

class UserSearchResult(BriefUser):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.perms = StaffPerms(kwargs.get("sPermissions"))
        
class DailyQuests:
    def __init__(self, quests):
        self.streak = quests.get("streak")
        self.completed = quests.get("completed")
        self.longest_streak = quests.get("longest_streak")

    def repr(self):
        return f"DailyQuests(streak={self.streak}, completed={self.completed}, longest_streak={self.longest_streak})"
    
    def __repr__(self):
        return self.repr()
class BriefFaction:
    def __init__(self, name, type=None, id=None, rank=None, **kwargs):
        self.name = name
        self.type = type
        self.id = id
        self.rank = rank

    def repr(self):
        return f"Faction(name={self.name}, type={self.type}, id={self.id}, rank={self.rank})"
    
    def __repr__(self):
        return self.repr()

class ServerOnlineHistory:
    def __init__(self, data):
        self.date = datetime.datetime.strptime(data["date"], "%Y-%m-%d")
        self.players = data["maxOnline"]

    def repr(self):
        return f"ServerOnlineHistory(date={self.date}, players={self.players})"

    def __repr__(self):
        return self.repr()

class StaffPerms:
    def __init__(self, perms):
        self.staff = perms.get("staff")
        self.manager = perms.get("manager")
        self.operator = perms.get("operator")
        self.admin = perms.get("admin")

    def repr(self):
        return f"StaffPerms(staff={self.staff}, manager={self.manager}, operator={self.operator}, admin={self.admin})"
    
    def __repr__(self):
        return self.repr()

class UserSearch:
    def __init__(self, nickname):
        data = asyncio.run(Fetcher.User.search_user(self, nickname))
        results = data.get("users")
        if results:
            self.results = [UserSearchResult(**result) for result in results]

    def repr(self):
        return f"UserSearch(results={self.results})"

    def __repr__(self):
        return self.repr()