class Member:
    def __init__(
        self, first_name, last_name, email =None, dob=None, membership_type="PPV", active=False, id=None
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.dob = dob
        self.membership_type = membership_type
        self.active = active
        self.id = id
        self.memberships = ["Gold", "Silver", "Bronze", "PPV"]

