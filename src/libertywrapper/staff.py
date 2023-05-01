import datetime

from .user import StaffUserAdministrator, StaffUserLeader

class Staff:
    def __init__(self, data):
        self.helpers = [StaffUserAdministrator(**helper) for helper in data.get("helpers")]
        self.administrators = [StaffUserAdministrator(**admin) for admin in data.get("administrators")]
        self.leaders = [StaffUserLeader(**leader) for leader in data.get("leaders")]

    def repr(self):
        return f"Staff(helpers={self.helpers}, administrators={self.administrators}, leaders={self.leaders})"

    def __repr__(self):
        return self.repr()

    def __iter__(self):
        return iter(self.__dict__.items())
