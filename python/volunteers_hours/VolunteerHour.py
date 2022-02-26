class VolunteerHour:
    """
    Class to contain the relationship of one volunteer and the one or many activity hours for them.
    Volunteer Info: full_name email total_hours
        Activity Info: name, date, hours (for num_activities)
    """
    full_name = ""
    email = ""
    total_hours = ""
    num_activities = 0
    activity = []
    activity_date = []
    activity_hours = []

    def __init__(self, full_name="", email="", total_hours="0:00"):
        if full_name != "" and email != "":
            self.add_volunteer(full_name, email, total_hours)

    def add_volunteer(self, full_name, email, total_hours="0:00"):
        self.full_name = full_name
        self.email = email
        self.total_hours = total_hours

    def add_activity(self, name, date, hours):
        self.activity.append(name)
        self.activity_date.append(date)
        self.activity_hours.append(hours)
        self.num_activities += 1

    def do_print(self):
        print(self.full_name, self.email, self.total_hours, self.num_activities)
        for j in range(self.num_activities):
            print("  " + self.activity[j], self.activity_date[j], self.activity_hours[j])


# Test code, exec if run as main
if __name__ == "__main__":
    volunteerHour = VolunteerHour("Manoj Thakur", "mthakur@yahoo.com", "10:00")
    volunteerHour.do_print()

    volunteerHour.add_activity("activity", "1/1/2017", "10:00")
    volunteerHour.do_print()

    volunteerHour.add_activity("activity", "2/1/2017", "10:00")
    volunteerHour.do_print()
