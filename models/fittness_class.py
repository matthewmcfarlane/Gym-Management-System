class FitnessClass:
    def __init__(self, name, capacity, start_time, duration, day, active=False, id=None):
        self.name = name
        self.capacity = capacity
        self.start_time = start_time
        self.duration = duration
        self.day = day
        self.active = active
        self.id = id
