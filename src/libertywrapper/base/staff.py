class StaffPerms:
    def __init__(self, perms):
        self.staff = perms.get("staff")
        self.manager = perms.get("manager")
        self.operator = perms.get("operator")
        self.admin = perms.get("admin")
        self.helper = perms.get("helper")

    def repr(self):
        return f"StaffPerms(staff={self.staff}, manager={self.manager}, operator={self.operator}, admin={self.admin}, helper={self.helper})"
    
    def __repr__(self):
        return self.repr()

    def __iter__(self):
        return iter((self.staff, self.manager, self.operator, self.admin))
