class Member:
    def __init__(
        self, first_name, last_name, dob=None, membership_type="PPV", active=False
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.membership_type = membership_type
        self.active = active
        self.memberships = ["Gold", "Silver", "Bronze", "PPV"]
