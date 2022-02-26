# This Google Authentication mechanism has been deprecated (Manoj: 05/20/2017)
import re
import urllib
import urllib2

class Spreadsheet(object):
    def __init__(self, key):
        super (Spreadsheet, self).__init__()
        self.key = key


class Client(object):
    def __init__(self, email, password):
        super (Client, self).__init__()
        self.email = email
        self.password = password

    def _get_auth_token(self, email, password, source, service):
        url = "https://www.google.com/accounts/ClientLogin"
        params = {
            "Email": email,
            "Password": password,
            "service": service,
            "accountType": "HOSTED_OR_GOOGLE",
            "source":source
        }
        req = urllib2.Request(url, urllib.urlencode(params))
        return re.findall(r"Auth=(.*)", urllib2.urlopen(req).read())[0]

    def get_auth_token(self):
        source = type(self).__name__
        return self._get_auth_token(self.email, self.password, source, service="wise")

    def download(self,spreadsheet, gid=0, format="csv"):
        url_format = "https://spreadsheets.google.com/feeds/download/spreadsheets/Export?key=%s&exportFormat=%s&gid=%i"
        headers = {
            "Authorization": "GoogleLogin auth=" + self.get_auth_token(),
            "GData-Version": "3.0"
        }
        req = urllib2.Request(url_format % (spreadsheet.key, format, gid), headers=headers)
        return urllib2.urlopen(req)


if __name__ == "__main__":
    import getpass
    import csv

    email="itacolunteer@gmail.com"
    password = getpass.getpass()
    spreadsheet_id = "1X9KszJu6WheUmIcKHAlt8tqAlNtaO4ocD9Mna3xeUDw"

    gs = Client(email, password)
    ss = Spreadsheet(spreadsheet_id)

    csv_file = gs.download(ss)

    for row in csv.reader(csv_file):
        print ", ".join(row)
