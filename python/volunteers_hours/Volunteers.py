import MCSV
import Volunteer


class Volunteers:
    total_items = 0
    volunteer_list = []  # List of Volunteer objects

    """
    :string csv_filename
    """

    def load_csv(self, csv_filename):
        volunteers_csv = MCSV.MCSV()
        content = volunteers_csv.load_file(csv_filename)

        line = 0
        for each_line in content:
            # Skip the 1st two lines
            if line > 1:
                # Split the line delimited by '|'
                one_line_array = each_line.split('|')

                one_volunteer = Volunteer.Volunteer(one_line_array[1], one_line_array[2])
                one_volunteer.add_parent(one_line_array[9], one_line_array[10])
                self.volunteer_list.append(one_volunteer)

            line += 1

    def find(self, full_name):
        for one_volunteer in self.volunteer_list:
            # Use 1st word as "first name" and last word as "last name", thus ignoring middle initial variance
            input_name_list = full_name.lower().strip().split(
                ' ')  # Convert to lowercase & Break full name into multiple entries separated by spaces
            input_name_list = [x.strip() for x in input_name_list]  # Eliminate any leading/trailing spaces
            len_input_name_list = len(input_name_list)  # Save num words in the full name

            volunteer_name_list = one_volunteer.full_name.lower().strip().split(
                ' ')  # Convert to lowercase & Break full name into multiple entries separated by spaces
            volunteer_name_list = [x.strip() for x in volunteer_name_list]  # Eliminate any leading/trailing spaces
            len_volunteer_name_list = len(volunteer_name_list)  # Save num words in the full name

            if input_name_list[0] == volunteer_name_list[0] and input_name_list[len_input_name_list - 1] == \
                    volunteer_name_list[len_volunteer_name_list - 1]:
                return True
        # If we come here, means we did not find any match and thus did not return True above
        return False

    def print_data(self):
        for one_volunteer in self.volunteer_list:
            print(">>" + one_volunteer.full_name, one_volunteer.email_address, one_volunteer.parent_full_name,
                  one_volunteer.parent_email_address)


# Test code, exec if run as main
if __name__ == "__main__":
    import Defines

    volunteer_list = Volunteers()
    volunteer_list.load_csv(Defines.Defines.volunteers_filepath)
    volunteer_list.print_data()

    # Test find()
    find_name = "Sahil Tilak"
    print("Find |" + find_name + "| - " + str(volunteer_list.find(find_name)))
    find_name = "Sahil J. Tilak"
    print("Find |" + find_name + "| - " + str(volunteer_list.find(find_name)))
    find_name = "SAHIL TILAK"
    print("Find |" + find_name + "| - " + str(volunteer_list.find(find_name)))
    find_name = "sAhIl TiLaK"
    print("Find |" + find_name + "| - " + str(volunteer_list.find(find_name)))
    find_name = "  SAHIL   TILAK   "
    print("Find |" + find_name + "| - " + str(volunteer_list.find(find_name)))
    find_name = "Joe Missing"
    print("Find |" + find_name + "| - " + str(volunteer_list.find(find_name)))
