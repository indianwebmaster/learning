import MCSV
import VolunteerHour


class VolunteersHours:
    total_items = 0
    volunteer_hour_list = []        # Array of VolunteerHour objects

    def load_csv(self, csv_filename):
        """
        :string csv_filename
        """
        volunteers_hours_csv = MCSV.MCSV()
        content = volunteers_hours_csv.load_file(csv_filename)

        # full_name num_entries start_entry total_hours
        #   entries ==> (@start_entry) activity, activity_date, activity_hours (for num_entries)
        last_full_name = "Nobody"
        line = 0
        idx = 0
        first_entry = True
        for each_line in content:
            # Skip the 1st two lines
            if line > 1:
                # Split the line delimited by '|'
                one_line_array = each_line.split('|')
                new_full_name = one_line_array[1]
                # Check if this a new name
                if new_full_name != last_full_name:
                    # Means, it is a new name
                    if first_entry:
                        # Just use idx == 0 for first entry, don't increment it.
                        first_entry = False
                    else:
                        # Means we have one full name entry at least
                        # Move idx, so we can start the next entry
                        idx += 1

                    self.volunteer_hour_list.append(
                        VolunteerHour.VolunteerHour(new_full_name, one_line_array[2], one_line_array[9]))
                    last_full_name = new_full_name

                self.volunteer_hour_list[idx].add_activity(one_line_array[3], one_line_array[0], one_line_array[8])

            line += 1

        idx += 1
        self.total_items = idx

    def print_data(self):
        for one_volunteer_hour in self.volunteer_hour_list:
            one_volunteer_hour.do_print()

# Test code, exec if run as main
if __name__ == "__main__":
    import Defines

    volunteers_hours = VolunteersHours()
    volunteers_hours.load_csv(Defines.Defines.volunteers_hours_filepath)
    volunteers_hours.print_data()
