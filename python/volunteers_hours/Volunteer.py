class Volunteer:
    """
    Class defining the details of one volunteer.
    contains the volunteer details and the parent details
    """
    full_name = ""
    email_address = ""
    parent_full_name = ""
    parent_email_address = ""

    def __init__(self, full_name, email_address):
        self.full_name = full_name
        self.email_address = email_address

    def add_parent(self, parents_full_name, parents_email_address):
        self.parent_full_name = parents_full_name
        self.parent_email_address = parents_email_address
