# SPDX-FileCopyrightText: © 2021 Antonio López Rivera <antonlopezr99@gmail.com>
# SPDX-License-Identifier: GPL-3.0-only

import datetime as dt
from numpy import sin, cos, arctan2, sqrt

from alexandria.math.units import rad


class ship:

    def __init__(self,
                 lon,
                 lat,
                 cruise_speed):
        """
        :param lon:          Longitude         [deg]
        :param lat:          Latitude          [deg]
        :param cruise_speed: Ship cruise speed [kt]
        """
        self.lon = lon
        self.lat = lat
        self.crs = cruise_speed * 0.5144444    # [m/2]

    def travel_time(self,
                    dest_lon,
                    dest_lat,
                    estimate):
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

        d = r_earth * c                   # [m]

        print("SHIP     :: Distance to target :: [Km]")
        print(f"{d/1000:.2f}")

        t = max(estimate, d/self.crs)     # [s]

        print("SHIP     :: Travel time        :: [h:mm:ss.ssssss]")
        print(f"{dt.timedelta(seconds=t)}\n")

        return t/60
