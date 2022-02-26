"""
The purpose is to find the volunteers with defined VolunteerHour but no entry in Volunteers
"""
import Defines
import Volunteers
import VolunteersHours


def find_missing_volunteers():
    """
    Check the list of volunteer_list in volunteer hours, and find the ones not in the volunteer db
    Do the match by full name
    :return: list of VolunteerHour objects not matching
    """
    volunteers = Volunteers.Volunteers()
    volunteers_hours = VolunteersHours.VolunteersHours()

    volunteers.load_csv(Defines.Defines.volunteers_filepath)
    volunteers_hours.load_csv(Defines.Defines.volunteers_hours_filepath)

    missing_volunteer_hour = []
    for one_volunteerHour in volunteers_hours.volunteer_hour_list:
        if not volunteers.find(one_volunteerHour.full_name):
            missing_volunteer_hour.append(one_volunteerHour)

    return missing_volunteer_hour


# Test code, exec if run as main
if __name__ == "__main__":
    missing_volunteers = find_missing_volunteers()
    i = 1
    # volunteers_hours.print_data()
    for one_missing_volunteer in missing_volunteers:
        print(str(i) + "|" + one_missing_volunteer.full_name + "|" + one_missing_volunteer.email + "|" +
              one_missing_volunteer.activity[0] + "|" + one_missing_volunteer.activity_date[0])
        i += 1
    print("total missing volunteer_list = " + str(len(missing_volunteers)))
    # print("total volunteer_list with hours = " + str(len(volunteers_hours.volunteer_hour_list)))
    # print("total registered volunteer_list = " + str(len(volunteers_hours.volunteers.volunteers)))
