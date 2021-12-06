class Member:
    def __init__(
        self, first_name, last_name, dob='', email ='', membership_type="Standard", active=False, id=None
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.membership_type = membership_type
        self.active = active
        self.id = id
        self.memberships = ["Premium", "Standard"]

        

