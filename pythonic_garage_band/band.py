class Musician:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"

    def __repr__(self):
        return f"{type(self).__name__} instance. Name = {self.name}"

    def get_instrument(self):
        return "Instrument"

    def play_solo(self):
        return "Solo"


class Guitarist(Musician):
    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"


class Bassist(Musician):
    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"


class Drummer(Musician):
    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"


class Band:
    instances = []

    def __init__(self, name, members=None):
        self.name = name
        self.members = members if members is not None else []
        Band.instances.append(self)

    def __str__(self):
        return f"Band {self.name} with members: {', '.join(str(member) for member in self.members)}"

    def __repr__(self):
        return f"Band instance. Name = {self.name}"

    @classmethod
    def to_list(cls):
        return cls.instances

    def play_solos(self):
        return [member.play_solo() for member in self.members]
