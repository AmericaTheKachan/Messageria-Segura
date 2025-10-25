class Message:
    def __init__(self, from_user, to_user, status, message):
        self.from_user = from_user
        self.to_user = to_user
        self.status = status
        self.message = message

    def toDict(self):
        return {
            "from_user": self.from_user,
            "to_user": self.to_user,
            "status": self.status,
            "message": self.message
        }
