import math
from pygeodesy.ellipsoidalVincenty import LatLon

class FPyGeod():
    def __init__(self):
        self.__meters_in_nmi = 1852.0

    def __validate_lat_lon(self, lat, lon):
        err = None
        if err is None and (lat > 90.0 or lat < -90.0):
            err = "Invalid latitude specified (%f)" % (lat)
        if err is None and (lon > 180.0 or lon < -180.0):
            err = "Invalid longitude specified (%f)" % (lon)
        assert (err is None), err  # Assert if err is not none, means we found an error

    def __validate_az_degrees(self, az_degrees):
        err = None
        if az_degrees < 0 or az_degrees > 360:
            err = "Invalid azimuth degrees specified (%f)" % (az_degrees)
        assert (err is None), err  # Assert if err is not none, means we found an error

    def __validate_az_acps(self, az_acps):
        err = None
        if az_acps < 0 or az_acps > 4096:
            err = "Invalid azimuth ACPs specified (%f)" % (az_acps)
        assert (err is None), err  # Assert if err is not none, means we found an error

    def __decimal_to_hhmmss(self, dec):
        hh = int(dec)
        x1_dec = dec - hh
        mm = int (x1_dec * 60)
        x2_dec = x1_dec - (float(mm)/60.0)
        ss = (x2_dec * 3600.0)
        if (ss > 59.99999):
            mm = mm + 1
            ss = ss - 59.99999

        hhmmss = "%02d:%02d:%05.3f" % (hh,mm,ss)
        return hhmmss

    @staticmethod
    def parse_latlon(coordinate):
        if isinstance(coordinate, (float, int)):
            if coordinate >= -180 and coordinate <= 180:
                return coordinate
            else:
                raise ValueError(f"{coordinate} is outside the bounds allowable for a geodesic coordinate.")
        elif isinstance(coordinate, str):
            sign_chars = {"N": 1, "S": -1, "E": 1, "W": -1}
            sign = None
            if len(coordinate) == 0:
                return None

            try:
                decimal = float(coordinate)
            except ValueError:
                # Format the string consistently
                coordinate = coordinate.strip().upper()
                translater = str.maketrans({
                        '"': " ",
                        "'": " ",
                        "°": " ",
                        ":": " "
                })
                coordinate = coordinate.translate(translater)

                lastchar = coordinate[-1]
                firstchar = coordinate[0]
                if firstchar in ["-", "+"] and lastchar in sign_chars:
                    raise ValueError()
                elif lastchar in sign_chars:
                    sign = sign_chars[lastchar]
                    coordinate = coordinate[0:-1].strip()
                elif firstchar == "-":
                    sign = -1
                    coordinate = coordinate[1:].strip()
                elif firstchar == "+":
                    sign = 1
                    coordinate = coordinate[1:].strip()
                else:
                    sign = 1

                components = coordinate.split()
                if len(components) == 3:
                    degrees = int(components[0])
                    minutes = int(components[1])
                    seconds = float(components[2])
                    decimal = (degrees + minutes / 60 + seconds / 3600) * sign
                elif len(components) == 1:
                    decimal = float(components[0]) * sign
                else:
                    raise ValueError()

            return FPyGeod.parse_latlon(decimal)

        else:
            raise TypeError(f"{type(coordinate)} is not a supported type for specifying a latitude or longitude value.")

    def latlon_dec_to_hhmmss(self,lat,lon):
        """
        :param lat: in format +/- hh.nnnnnn
        :param lon: in format +/- hh.nnnnnn
        :return: in format (hh:mm:ss.nnn N/S,hh:mm:ss.nnn E/W)
        """
        lat_ns = "N"
        if lat < 0:
            lat = -(lat)
            lat_ns = "S"

        lon_ew = "E"
        if lon < 0:
            lon = -(lon)
            lon_ew = "W"

        hhmmss_lat = self.__decimal_to_hhmmss(lat) + " " + lat_ns
        hhmmss_lon = self.__decimal_to_hhmmss(lon) + " " + lon_ew
        return (hhmmss_lat,hhmmss_lon)

    def hhmmss_to_decimal(self,hhmmss):
        """
        :param hhmmss: in format hh:mm:ss.nnn N/S/E/W
        :return: +/-hh.nnnn
        """
        hhmmss_list = hhmmss.split(":")
        hh = hhmmss_list[0]; mm = hhmmss_list[1]; ss_decimal_dir = hhmmss_list[2]
        ss_list = ss_decimal_dir.split(".")
        if len(ss_list) > 1:
            ss = ss_list[0]
            dec_list = ss_list[1].split(" ")
            dec = dec_list[0]
            nsew = dec_list[1]
        else:
            dec = 0
            ss_list_2 = ss_list[0].split(" ")
            ss = ss_list_2[0]
            nsew = ss_list_2[1]

        decimal_val = float(hh) + (float(mm)/60.0) + (float(ss)/3600.0)
        if nsew == "S" or nsew == "W":
            decimal_val = (-1.0) * decimal_val

        return decimal_val

    def lat_lon_from_reference_given_range_az_degrees(self, ref_lat, ref_lon, range_nmi, az_degrees):
        """
        :param ref_lat: in format +/- hh.nnnnnn
        :param ref_lon: in format +/- hh.nnnnnn
        :param range_nmi:
        :param az_degrees:
        :return: (+/- hh.nnnn, +/- hh.nnnn)
        """
        p = LatLon(ref_lat, ref_lon)
        range_meters = range_nmi * self.__meters_in_nmi
        d = p.destination(range_meters, az_degrees)
        return (d.lat, d.lon)

    def lat_lon_from_reference_multiple_range_az_degrees(self, ref_lat, ref_lon, range_az_list):
        """
        :param ref_lat: in format +/- hh.nnnnnn
        :param ref_lon: in format +/- hh.nnnnnn
        :param range_az_list: [ [range1,azDeg1], [range2,azDeg2] ... ]
        :return: [ (lat1,lon1), (lat2, lon2) ... ]
        """
        lat_lon_list = []
        for range_az in range_az_list:
            lat_lon = self.lat_lon_from_reference_given_range_az_degrees(ref_lat, ref_lon, range_az[0],range_az[1])
            lat_lon_list.append(lat_lon)
        return lat_lon_list

    def lat_lon_from_reference_given_range_az_acps(self, ref_lat, ref_lon, range_nmi, az_acps):
        """
        :param ref_lat: in format +/- hh.nnnnnn
        :param ref_lon: in format +/- hh.nnnnnn
        :param range_nmi:
        :param az_acps:
        :return: (+/- hh.nnnn, +/- hh.nnnn)
        """
        az_degrees = (az_acps * 360.0) / 4096.0
        return self.lat_lon_from_reference_given_range_az_degrees(ref_lat, ref_lon, range_nmi, az_degrees)

    def lat_lon_from_reference_multiple_range_az_acps(self, ref_lat, ref_lon, range_az_list):
        """
        :param ref_lat: in format +/- hh.nnnnnn
        :param ref_lon: in format +/- hh.nnnnnn
        :param range_az_list: [ [range1,azAcp1], [range2,azAcp2] ... ]
        :return: [ (lat1,lon1), (lat2, lon2) ... ]
        """
        lat_lon_list = []
        for range_az in range_az_list:
            lat_lon = self.lat_lon_from_reference_given_range_az_acps(ref_lat, ref_lon, range_az[0],range_az[1])
            lat_lon_list.append(lat_lon)
        return lat_lon_list

    def lat_lon_from_reference_given_xy_nmi(self, ref_lat, ref_lon, x_nmi, y_nmi):
        """
        :param ref_lat: in format +/- hh.nnnn
        :param ref_lon: in format +/- hh.nnnn
        :param x_nmi:
        :param y_nmi:
        :return: (+/- hh.nnnn, +/- hh.nnnn)
        """
        # first transformation along X axis (90 or 270 degrees), get lat,lon
        if x_nmi > 0:
            (lat_1, lon_1) = self.lat_lon_from_reference_given_range_az_degrees(ref_lat,ref_lon,x_nmi, 90.0)
        else:
            (lat_1, lon_1) = self.lat_lon_from_reference_given_range_az_degrees(ref_lat, ref_lon, x_nmi, 270.0)
        # Next, from that point, transform along Y axis (0 or 180 degrees)
        if y_nmi > 0:
            (lat, lon) = self.lat_lon_from_reference_given_range_az_degrees(lat_1,lon_1,y_nmi, 0.0)
        else:
            (lat, lon) = self.lat_lon_from_reference_given_range_az_degrees(lat_1,lon_1,y_nmi, 180.0)
        return (lat,lon)

    def lat_lon_from_reference_multiple_xy_nmi(self, ref_lat, ref_lon, xy_nmi_list):
        """
        :param ref_lat: in format +/- hh.nnnn
        :param ref_lon: in format +/- hh.nnnn
        :param xy_nmi_list: [ [x1,y1], [x2,y2], [x3,y3] ..... ]
        :return: [ (lat1,lon1), (lat2,lon2), (lat3,lon3) ..... ]
        """
        lat_lon_list = []
        for xy_nmi in xy_nmi_list:
            lat_lon = self.lat_lon_from_reference_given_xy_nmi(ref_lat, ref_lon, xy_nmi[0],xy_nmi[1])
            lat_lon_list.append(lat_lon)
        return lat_lon_list

    def distance_rangeAzDeg_between_two_lat_lon(self, lat1, lon1, lat2, lon2):
        """
        :param lat1: in format +/- hh.nnnn
        :param lon1: in format +/- hh.nnnn
        :param lat2: in format +/- hh.nnnn
        :param lon2: in format +/- hh.nnnn
        :return: (range_nmi, azDegrees)
        """
        p = LatLon(lat1, lon1)
        q = LatLon(lat2, lon2)
        range_meters = p.distanceTo(q)
        range_nmi = range_meters / self.__meters_in_nmi
        azDegrees = p.initialBearingTo(q)

        return (range_nmi, azDegrees)

    @DeprecationWarning
    def rangeNmi_azDegrees_from_reference_given_lat_lon(self, ref_lat, ref_lon, lat, lon):
        return self.distance_rangeAzDeg_between_two_lat_lon(ref_lat,ref_lon,lat, lon)

    def distance_rangeAzAcp_between_two_lat_lon(self, lat1, lon1, lat2, lon2):
        """
        :param lat1: in format +/- hh.nnnn
        :param lon1: in format +/- hh.nnnn
        :param lat2: in format +/- hh.nnnn
        :param lon2: in format +/- hh.nnnn
        :return: (range_nmi, azACPs)
        """
        (range_nmi, azDegrees) = self.distance_rangeAzDeg_between_two_lat_lon(lat1,lon1,lat2,lon2)
        azAcp = (int) ((azDegrees * 4096.0) / 360.0)
        return (range,azAcp)

    @DeprecationWarning
    def rangeNmi_azAcps_from_reference_given_lat_lon(self, ref_lat, ref_lon, lat, lon):
        return self.distance_rangeAzAcp_between_two_lat_lon(ref_lat, ref_lon, lat, lon)

    def distance_between_two_lat_lon(self, lat1, lon1, lat2, lon2):
        """
        :param lat1: in format +/- hh.nnnn
        :param lon1: in format +/- hh.nnnn
        :param lat2: in format +/- hh.nnnn
        :param lon2: in format +/- hh.nnnn
        :return: range_nmi
        """
        (range_nmi, azDegrees) = self.distance_rangeAzDeg_between_two_lat_lon(lat1,lon1,lat2,lon2)
        return range_nmi

    def distance_xy_between_two_lat_lon(self, lat1, lon1, lat2, lon2):
        """
        :param lat1: in format +/- hh.nnnn
        :param lon1: in format +/- hh.nnnn
        :param lat2: in format +/- hh.nnnn
        :param lon2: in format +/- hh.nnnn
        :return: (x_nmi, y_nmi)
        """
        (range_nmi, azDegrees) = self.distance_rangeAzDeg_between_two_lat_lon(lat1,lon1,lat2,lon2)
        azRadians = math.radians(azDegrees)

        y_nmi = range_nmi * math.cos(azRadians)
        x_nmi = range_nmi * math.sin(azRadians)
        return (x_nmi, y_nmi)

    def lat_lon_circle (self, ref_lat, ref_lon, radius_nmi, num_entries = 180):
        """
        :param ref_lat: in format +/- hh.nnnn
        :param ref_lon: in format +/- hh.nnnn
        :param radius_nmi:
        :param num_entries:
        :return: [ (lat1,lon1), (lat2,lon2), ... ] ----- num_entries+1
        """
        lat_lon_list = []
        azDegrees = 0.0
        delta_azDegrees = 360.0 / num_entries
        while azDegrees < 360.0:
            (lat,lon) = self.lat_lon_from_reference_given_range_az_degrees(ref_lat,ref_lon,radius_nmi,azDegrees)
            lat_lon_list.append((lat,lon))
            azDegrees += delta_azDegrees
        # Final point will be added as == first, if it is not already
        numItems = len(lat_lon_list)
        if numItems > 0 and (lat_lon_list[0] != lat_lon_list[numItems - 1]): lat_lon_list.append(lat_lon_list[0])
        return lat_lon_list

if __name__ == "__main__":
    geod = FPyGeod()

    for lat,lon in geod.lat_lon_circle(30.5,-120.5,40.0,50):
        print (F"{lat},{lon}")

    print(geod.lat_lon_from_reference_given_range_az_degrees(30.5,-120.5,40,180))   # Center to bottom cicle point
    print(geod.lat_lon_from_reference_given_range_az_acps(30.5,-120.5,40,2048))   # Center to bottom cicle point

    print(geod.distance_rangeAzDeg_between_two_lat_lon(30.5,-120.5,29.831741160929926,-120.5))  # Center to bottom circle point
    print(geod.distance_rangeAzAcp_between_two_lat_lon(30.5,-120.5,29.831741160929926,-120.5))  # Center to bottom circle point

    print(geod.distance_xy_between_two_lat_lon(30.5, -120.5, 29.831741160929926, -120.5))   # Center to bottom circle point
