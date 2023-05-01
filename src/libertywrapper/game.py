import datetime

class MapBlip:
    def __init__(self, data):
        self.id = data.get("id")
        self.position = tuple(data.get("position").values()) # (x, y, z)
        self.name = data.get("name")
        self.scale = data.get("scale")

    def repr(self):
        return f"MapBlip(id={self.id}, position={self.position}, name={self.name}, scale={self.scale})"

    def __repr__(self):
        return self.repr()

    def __iter__(self):
        return iter(self.position)
