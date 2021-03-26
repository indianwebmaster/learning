from pygeodesy.ellipsoidalVincenty import LatLon


def test1():
    p = LatLon(-37.95103, 144.42487)
    d = p.destination(54972.271, 306.86816)
    print (d.lon, d.lat)

test1()