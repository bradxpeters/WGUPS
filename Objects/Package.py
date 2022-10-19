from datetime import datetime

from Objects.Constants import AT_HUB, EN_ROUTE, DELIVERED


class Package:
    def __init__(self, address, city, deadline, package_id, state, status, weight, zipcode):
        self.address = address
        self.city = city
        self.deadline = deadline
        self.delivery_time: datetime = None
        self.departure_time = None
        self.id = package_id
        self.state = state
        self.status = status
        self.weight = weight
        self.zipcode = zipcode

    def __str__(self):
        return \
            'Package ID: {}\n' \
            'Address: {}\n' \
            'City: {}\n' \
            'Deadline: {}\n' \
            'Delivery Time: {}\n' \
            'State: {}\n' \
            'Status: {}\n' \
            'Weight: {}\n' \
            'Zipcode: {}\n'.format(
                self.id,
                self.address,
                self.city,
                self.deadline,
                self.delivery_time.time(),
                self.state,
                self.status,
                self.weight,
                self.zipcode,
            )

    def get_status(self, time):
        # Convert struct to datetime
        time = datetime(*time[:6])

        if self.delivery_time < time:
            self.status = DELIVERED
        elif self.departure_time > time:
            self.status = EN_ROUTE
        else:
            self.status = AT_HUB
