from datetime import datetime


class Truck:
    def __init__(self, truck_id, address, capacity, departure_time, load, mileage, packages, speed):
        departure_time = datetime.strptime(departure_time, '%H:%M')
        self.truck_id = truck_id
        self.address = address
        self.capacity: int = capacity
        self.departure_time = departure_time
        self.load = load
        self.mileage = mileage
        self.packages = packages
        self.speed = speed
        self.time = departure_time

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (
            self.truck_id, self.address, self.capacity, self.departure_time, self.load, self.mileage, self.packages,
            self.speed
        )
