import datetime

class Log:
    def __init__(self, data):
        # 2023-04-11T05:35:01.098Z
        self.time = datetime.datetime.strptime(data.get("time"), "%Y-%m-%dT%H:%M:%S.%fZ")
        self.text = data.get("text")

    def repr(self):
        return f"Log(time={self.time}, text={self.text})"

    def __repr__(self):
        return self.repr()

    def __iter__(self):
        return iter((self.time, self.text))
