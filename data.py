import datetime
    
class OnlinePlayers:
    def __init__(self, data):
        self.data = data
        # TODO Actualizat clasa player dupa ce dau de oameni cu factiune online

class MapBlips:
    def __init__(self, data):
        self.data = data
        self.blips = [Blip(x["id"], x["position"], x["name"], x["scale"]) for x in data["blips"]]

class Blip:
    def __init__(self, id, position, name, scale):
        self.id = id
        self.position = (position["x"], position["y"], position["z"])
        self.name = name
        self.scale = scale

class Staff:
    def __init__(self, data):
        self.data = data
        self.helpers = [StaffMember(x["id"], x["name"], x["UserAvatar"], x["Status"], x["Faction"], x["Level"], x["updatedAt"], perms=x["sPermissions"]) for x in data["staff"]["helpers"]]
        self.administrators = [StaffMember(x["id"], x["name"], x["UserAvatar"], x["Status"], x["Faction"], x["Level"], x["updatedAt"], perms=x["sPermissions"]) for x in data["staff"]["administrators"]]
        self.leaders = [StaffMember(x["id"], x["name"], x["UserAvatar"], x["Status"], x["Faction"], x["Level"], x["updatedAt"], faction=x["faction"]) for x in data["staff"]["leaders"]]
        
class StaffMember:
    def __init__(self, id, name, avatar, status, faction_id, level, updated_at, faction=None, perms=None):
        self.id = id
        self.name = name
        self.avatar = avatar
        self.status = status
        self.faction_id = faction
        self.level = level
        self.updated_at = datetime.datetime.strptime(updated_at, "%Y-%m-%dT%H:%M:%S.%fZ")
        # 2023-01-10T20:55:12.373Z -> 2023-01-10 20:55:12.373000
        
        self.faction = Faction(faction) if faction else None
        self.perms = StaffPerms(perms) if perms else None
        
class General:
    def __init__(self, data):
        self.data = data
        self.total_users = data["total_users"]
        self.total_online = data["total_online"]
        self.total_vehicles = data["total_vehicles"]
        self.total_houses = data["total_houses"]
        self.total_apartments = data["total_apartments"]
        self.total_posts = data["total_posts"]
        self.top_users_activity = [Player(x["UserAvatar"], x["name"], x["Level"], x["Playtime"], faction=x.get("Faction")) for x in data["top_users_activity"]]
        self.top_users_last_week_activity = [Player(x["UserAvatar"], x["name"], x["Level"], x["Playtime"], faction=x.get("Faction"), quests=x["DailyQuestsStats"]) for x in data["top_users_last_week_activity"]]
        self.top_users_quests = [Player(x["UserAvatar"], x["name"], x["Level"], x["Playtime"], quests=x["DailyQuestsStats"]) for x in data["top_users_quests"]]
        self.top_users_jobs = [Player(x["UserAvatar"], x["name"], x["Level"], x["Playtime"], money=x["money"]) for x in data["top_users_jobs"]]


class Player:
    def __init__(self, avatar, name, level, playtime, id=None, faction=None, money=None, quests=None):
        self.avatar = avatar
        self.name = name
        self.level = level
        self.playtime = datetime.timedelta(seconds=playtime)
        
        self.id = id
        self.money = money
        self.faction = Faction(faction) if faction else None
        self.quests = DailyQuests(quests) if quests else None
        # self.faction = faction # data["Faction"] | top_users_last_week_activity, top_users_activity
        # self.quests = quests # data["DailyQuestsStats"] | top_users_quests, top_users_last_week_activity

class DailyQuests:
    def __init__(self, quests):
        self.streak = quests["streak"]
        self.completed = quests["completed"]
        self.longest_streak = quests["longest_streak"]

class Faction:
        def __init__(self, faction):
            self.name = faction["Name"]
            self.type = faction.get("Type")

class StaffPerms:
    def __init__(self, perms):
        self.staff = perms.get("staff")
        self.manager = perms.get("manager")
        self.operator = perms.get("operator")
        self.admin = perms.get("admin")
