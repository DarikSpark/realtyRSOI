
class Flat(object):

    def __init__(self, id, name, rooms, cost, latitude, longitude):
        self.id = id
        self.name = name
        self.rooms = rooms
        self.cost = cost
        self.latitude = latitude
        self.longitude = longitude


class Shedule(object):

    def __init__(self, flat_id, date, date_to, busy_from, busy_to):
        self.flat_id = flat_id
        self.date = date
        self.date_to = date_to
        self.busy_from = busy_from
        self.busy_to = busy_to
