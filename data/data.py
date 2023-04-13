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

    def __iter__(self):
        return iter(self.__dict__.items())

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

    def __iter__(self):
        return iter(self.__dict__.items())

class OnlinePlayers:
    def __init__(self):
        data = asyncio.run(Fetcher.General.get_online_players())
        self.players = [BriefUser(**x) for x in data.get("users")]

    def repr(self):
        return f"OnlinePlayers(players={self.players})"

    def __repr__(self):
        return self.repr()

    def __iter__(self):
        return iter(self.players)

class MapBlips:
    def __init__(self):
        data = asyncio.run(Fetcher.General.get_map_blips(cache=False))

        self.blips = [MapBlip(**x) for x in data.get("blips")]

    def repr(self):
        return f"MapBlips(blips={self.blips})"

    def __repr__(self):
        return self.repr()

    def __iter__(self):
        return iter(self.blips)

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

    def __iter__(self):
        return iter(self.position)

class User:
    def __init__(self, **kwargs):
        self.avatar = kwargs.get("UserAvatar")
        self.name = kwargs.get("name")
        self.level = kwargs.get("Level")
        self.playtime = datetime.timedelta(seconds=kwargs.get("Playtime"))
    
    def repr(self):
        return f"User(avatar={self.avatar}, name={self.name}, level={self.level}, playtime={self.playtime})"

    def __repr__(self):
        return self.repr()

    def __iter__(self):
        return iter((self.avatar, self.name, self.level, self.playtime))

        
class StaffUser(User):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = kwargs.get("id")
        self.status = kwargs.get("Status") == "true"
        self.faction_id = kwargs.get("Faction") if isinstance(kwargs.get("Faction"), int) else None
        self.last_seen = datetime.datetime.strptime(kwargs.get("LastSeen"), "%Y-%m-%dT%H:%M:%S.%fZ")

    def repr(self):
        return f"StaffUser(avatar={self.avatar}, name={self.name}, level={self.level}, playtime={self.playtime}, id={self.id}, status={self.status}, faction_id={self.faction_id}, last_seen={self.last_seen})"

    def __iter__(self):
        return super().__iter__() + iter((self.id, self.status, self.faction_id, self.last_seen))

class StaffUserAdministrator(StaffUser):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.perms = StaffPerms(**kwargs.get("sPermissions"))

    def repr(self):
        return f"StaffUserAdministrator(avatar={self.avatar}, name={self.name}, level={self.level}, playtime={self.playtime}, id={self.id}, status={self.status}, faction_id={self.faction_id}, last_seen={self.last_seen}, perms={self.perms})"

    def __iter__(self):
        return super().__iter__() + iter((self.perms,))

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
        
    def repr(self):
        return f"StaffPerms(staff={self.staff}, admin={self.admin}, operator={self.operator}, manager={self.manager})"

    def __repr__(self):
        return self.repr()

    def __iter__(self):
        return iter((self.staff, self.admin, self.operator, self.manager))

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

    def __iter__(self):
        return super().__iter__() + iter((self.id, self.faction))

class UserActivity(User):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.faction = BriefFaction(kwargs.get("Faction").get("name")) if kwargs.get("Faction") else None

    def repr(self):
        return f"UserActivity(avatar={self.avatar}, name={self.name}, level={self.level}, playtime={self.playtime}, faction={self.faction})"

    def __iter__(self):
        return super().__iter__() + iter((self.faction,))

class UserQuestsActivity(User):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = kwargs.get("id")
        self.quests = DailyQuests(kwargs.get("DailyQuestsStats")) if kwargs.get("DailyQuestsStats") else None

    def repr(self):
        return f"UserQuestsActivity(avatar={self.avatar}, name={self.name}, level={self.level}, playtime={self.playtime}, id={self.id}, quests={self.quests})"

    def __iter__(self):
        return super().__iter__()

class UserJobsActivity(User):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = kwargs.get("id")
        self.money = kwargs.get("money")

    def repr(self):
        return f"UserJobsActivity(avatar={self.avatar}, name={self.name}, level={self.level}, playtime={self.playtime}, id={self.id}, money={self.money})"

    def __iter__(self):
        return super().__iter__() + iter((self.id, self.money))

class UserSearchResult(BriefUser):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.perms = StaffPerms(kwargs.get("sPermissions"))

    def repr(self):
        return f"UserSearchResult(avatar={self.avatar}, name={self.name}, level={self.level}, playtime={self.playtime}, id={self.id}, faction={self.faction}, perms={self.perms})"

    def __iter__(self):
        return super().__iter__() + iter((self.perms,))

class DailyQuests:
    def __init__(self, quests):
        self.streak = quests.get("streak")
        self.completed = quests.get("completed")
        self.longest_streak = quests.get("longest_streak")

    def repr(self):
        return f"DailyQuests(streak={self.streak}, completed={self.completed}, longest_streak={self.longest_streak})"
    
    def __repr__(self):
        return self.repr()

    def __iter__(self):
        return iter((self.streak, self.completed, self.longest_streak))

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

    def __iter__(self):
        return iter((self.name, self.type, self.id, self.rank))

class ServerOnlineHistory:
    def __init__(self, data):
        self.date = datetime.datetime.strptime(data["date"], "%Y-%m-%d")
        self.players = data["maxOnline"]

    def repr(self):
        return f"ServerOnlineHistory(date={self.date}, players={self.players})"

    def __repr__(self):
        return self.repr()

    def __iter__(self):
        return iter((self.date, self.players))

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

    def __iter__(self):
        return iter((self.staff, self.manager, self.operator, self.admin))

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
    
    def __iter__(self):
        return iter((self.results,))

class Factions:
    def __init__(self):
        data = asyncio.run(Fetcher.Faction.get_faction_list())
        factions = data.get("factions")
        if factions:
            self.factions = [Faction(faction) for faction in factions]

    def repr(self):
        return f"Factions(factions={self.factions})"

    def __repr__(self):
        return self.repr()
    
    def __iter__(self):
        return iter((self.factions,))

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
        return iter((self.id, self.name, self.type, self.chat_status, self.hq_status, self.location, self.blip_model, self.blip_color, self.has_interior, self.interior, self.has_garage, self.garage, self.ranks, self.max_members, self.min_level, self.applications, self.applications_questions, self.penalty_reasons, self.users))
class FactionInteriorGeneral:
    def __init__(self, data):
        self.heading = data.get("heading")
        self.position = tuple(data.get("position").values())

    def repr(self):
        return f"FactionInteriorGeneral(heading={self.heading}, position={self.position})"

    def __repr__(self):
        return self.repr()

    def __iter__(self):
        return iter((self.heading, self.position))

class FactionInteriorHQ(FactionInteriorGeneral):
    def __init__(self, data):
        super().__init__(data)
        self.duty_pos = tuple(data.get("dutyPos").values())
        self.ipl_list = data.get("IPLList")

    def repr(self):
        return f"FactionInterior(ipl_list={self.ipl_list}, duty_pos={self.duty_pos}, heading={self.heading}, position={self.position})"

    def __iter__(self):
        return iter((self.ipl_list, self.duty_pos, self.heading, self.position))

class FactionInteriorGarage(FactionInteriorGeneral):
    def __init__(self, data):
        super().__init__(data)
        self.ipl_list = data.get("IPLList")

    def repr(self):
        return f"FactionInterior(ipl_list={self.ipl_list}, heading={self.heading}, position={self.position})"

    def __iter__(self):
        return iter((self.ipl_list, self.heading, self.position))

class FactionGarage:
    def __init__(self, data):
        self.hq = tuple(data.get("HQ").values())
        self.exit = FactionInteriorGeneral(data.get("Exit"))
        self.enter = FactionInteriorGeneral(data.get("Enter"))
        self.interior = FactionInteriorGarage(data.get("Interior"))

    def repr(self):
        return f"FactionGarage(hq={self.hq}, exit={self.exit}, enter={self.enter}, interior={self.interior})"

    def __repr__(self):
        return self.repr()

    def __iter__(self):
        return iter((self.hq, self.exit, self.enter, self.interior))

class FactionPenalty:
    def __init__(self, data):
        self.points = data.get("points")
        self.reason = data.get("reason")
        self.duration = data.get("duration")

    def repr(self):
        return f"FactionPenalty(points={self.points}, reason={self.reason}, duration={self.duration})"

    def __repr__(self):
        return self.repr()

    def __iter__(self):
        return iter((self.points, self.reason, self.duration))

class FactionUser:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.name = kwargs.get("name")
        self.level = kwargs.get("Level")
        self.faction_rank = kwargs.get("FactionRank")
        self.user_avatar = kwargs.get("UserAvatar")

    def repr(self):
        return f"FactionUser(id={self.id}, name={self.name}, level={self.level}, faction_rank={self.faction_rank}, user_avatar={self.user_avatar})"

    def __repr__(self):
        return self.repr()

    def __iter__(self):
        return iter((self.id, self.name, self.level, self.faction_rank, self.user_avatar))

class FactionHistory:
    def __init__(self):
        data = asyncio.run(Fetcher.Faction.get_faction_history())
        data = data.get("history")
        self.logs = [FactionHistoryLog(log) for log in data]

    def repr(self):
        return f"FactionHistory(logs={self.logs})"
    
    def __repr__(self):
        return self.repr()

    def __iter__(self):
        return iter(self.logs)

class FactionHistoryLog:
    def __init__(self, data):
        # 2023-04-11T05:35:01.098Z
        self.time = datetime.datetime.strptime(data.get("time"), "%Y-%m-%dT%H:%M:%S.%fZ")
        self.text = data.get("text")

    def repr(self):
        return f"FactionHistoryLog(time={self.time}, text={self.text})"

    def __repr__(self):
        return self.repr()

    def __iter__(self):
        return iter((self.time, self.text))
