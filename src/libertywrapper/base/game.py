import datetime

class RandomData:
    """
    Stores miscelaneous data with uncommon usages.
    """
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def repr(self):
        return f"RandomData({self.__dict__})"
    
    def __repr__(self):
        return self.repr()

    def __iter__(self):
        return iter(self.__dict__.items())

class Character(RandomData):
    def repr(self):
        return f"Character({self.__dict__})"
    
class ItemLoadout(RandomData):
    def repr(self):
        return f"ItemLoadout({self.__dict__})"

class PanelSettings:
    def __init__(self, data):
            self.can_follow = data.get("canFollow")
            self.can_comment = data.get("canComment")
            self.notifications = data.get("notifications")
            self.private_profile = data.get("privateProfile")

    def repr(self):
        return f"PanelSettings({self.__dict__})"

    def __repr__(self):
        return self.repr()

    def __iter__(self):
        return iter(self.__dict__.items())
    
class Item:
    def __init__(self, data):
        self.quantity = data.get("qt")
        self.used = data.get("used")
        self.key = data.get("key")
        self.uuid = data.get("uuid")
        self.custom_data = data.get("custom_data")

class Inventory:
    def __init__(self, data):
        self.items = [Item(item) for item in data.get("Items")]
        self.slots = data.get("Slots")
        self.equipped_items = ItemLoadout(**data.get("EquippedItems"))

class Color:
    def __init__(self, data):
        if isinstance(data, dict):
            self.type = data.get("type")
            self.value = data.get("value")
        else:
            self.type = None
            self.value = None

class VehicleState:
    def __init__(self, data):
        self.position = tuple(data.get("Position").values()) # (x, y, z)
        self.heading = data.get("Heading")
        self.dimension = data.get("Dimension")

class Vehicle:
    def __init__(self, data):
        self.id = data.get("id")
        self.owner = data.get("Owner")
        self.modelhash = data.get("ModelHash")
        self.position = tuple(data.get("Position").values()) # (x, y, z)
        self.heading = data.get("Heading")
        self.dimension = data.get("Dimension")
        self.lastlocation = VehicleState(data.get("LastLocation"))
        self.locked = data.get("Locked")
        self.engine_health = data.get("EngineHealth")
        self.body_health = data.get("BodyHealth")
        self.destroyed = data.get("Destroyed")
        self.dirt_level = data.get("DirtLevel")
        self.plate = data.get("Plate")
        self.fuel_type = data.get("Fuel").get("type")
        self.fuel_value = data.get("Fuel").get("value")
        self.traveled_distance = data.get("TraveledDistance")
        self.expire_time = data.get("ExpireTime")
        self.upgrades_cost = data.get("UpgradesCost")
        self.is_dead = data.get("IsDead")
        self.listed_on_market = data.get("listedOnMarket")
        self.expire_hours = data.get("ExpireHours")
        self.created_at = datetime.datetime.fromisoformat(data.get("createdAt").replace("Z", "+00:00"))
        self.updated_at = datetime.datetime.fromisoformat(data.get("updatedAt").replace("Z", "+00:00"))
        self.upgrades = data.get("Upgrades")
        self.colors = [Color(color) for color in data.get("colors")]
        # 2 culori sunt cum trebuie, celelalte 2 au valoare -1 si probabil au alt rol
        # self.plate_smth = data.get("plate")

class Comment:
    def __init__(self, data):
        self.id = data.get("id")
        self.text = data.get("text")
        self.profile_id = data.get("profileId")
        self.creator_id = data.get("creatorId")
        self.creator_name = data.get("creator").get("name")
        self.creator_avatar = data.get("creator").get("UserAvatar")

class AchievementProgress:
    def __init__(self, data):
        self.uuid = data.get("id") # uuid
        self.progress = data.get("progress")
        self.user_id = data.get("userId")
        self.achievement = Achievement(data.get("achievement"))
        # self.max_progress = data.get("maxProgress")
        # self.achievement_id = data.get("achievementId")

class Achievement:
    def __init__(self, data):
        self.id = data.get("id")
        self.name = data.get("name")
        self.description = data.get("description")
        self.max_progress = data.get("maxProgress")
        self.progress_name = data.get("progressName")
        self.icon = data.get("icon")
        self.category = data.get("category")
        self.reward = data.get("reward")

class Business:
    def __init__(self, data):
        self.icon = data.get("Icon")
        self.name = data.get("Name")
        self.type = data.get("Type")
        self.shares_count = data.get("SharesCount")
        self.market_stock_price = data.get("MarketStockPrice")

class BusinessShare:
    def __init__(self, data):
        self.id = data.get("ID")
        self.shares = data.get("Shares")
        self.biz_id = data.get("bizId")
        self.user_id = data.get("userId")
        self.business = Business(data.get("Business"))