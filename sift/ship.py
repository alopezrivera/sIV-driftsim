# SPDX-FileCopyrightText: © 2021 Antonio López Rivera <antonlopezr99@gmail.com>
# SPDX-License-Identifier: GPL-3.0-only

from numpy import sin, cos, arctan2, sqrt

from alexandria.math.units import rad


class ship:

    def __init__(self,
                 lon,
                 lat,
                 cruise_speed):
        """
        :param lon: [deg] Longitude
        :param lat: [deg] Latitude
        :param cruise_speed: [kt] Ship cruise speed
        """
        self.lon = lon
        self.lat = lat
        self.crs = cruise_speed * 0.514444444

    def travel_time(self,
                    dest_lon,
                    dest_lat):
        """
        Great-circle distance from ship to destination.

            http://www.movable-type.co.uk/scripts/latlong.html

        """
        r_earth = 6371e3    # [m]

        lon0 = rad(self.lon)
        lat0 = rad(self.lat)
        lon1 = rad(dest_lon)
        lat1 = rad(dest_lat)

        delta_lon = lon1 - lon0
        delta_lat = lat1 - lat0

        a = sin(delta_lon/2) * \
            sin(delta_lat/2) + \
            cos(delta_lon)   * \
            cos(delta_lat)   * \
            sin(delta_lon/2) * \
            sin(delta_lat/2)

        a = abs(a)

        c = 2 * arctan2(sqrt(a), sqrt(1-a))

        d = r_earth * c    # [m]

        print(f"SHIP     :: Distance to LKNRC    :: [Km]")
        print(f"{d/1000:.2f}")

        t = d/self.crs     # [s]

        print("SHIP     :: Travel time to LKNRC :: [min]")
        print(f"{t/60:.2f}\n")

        return t/60
