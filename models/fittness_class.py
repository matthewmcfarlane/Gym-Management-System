class FitnessClass:
    def __init__(self, name, capacity, active = False, start_time, duration, day, id=None):
        self.name = name
        self.capacity = capacity
        self.active = active
        self.start_time = start_time
        self.duration = duration
        self.day = day
        self.id = id
