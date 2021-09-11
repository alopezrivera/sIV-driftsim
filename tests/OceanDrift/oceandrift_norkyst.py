# SPDX-FileCopyrightText: © 2021 Antonio López Rivera <antonlopezr99@gmail.com>
# SPDX-License-Identifier: GPL-3.0-only

from datetime import datetime, timedelta
from opendrift.models.oceandrift import OceanDrift

o = OceanDrift()
o.add_readers_from_list(
    ['https://thredds.met.no/thredds/dodsC/sea/norkyst800m/1h/aggregate_be'])
o.disable_vertical_motion()
o.seed_elements(lon=4.85, lat=60, time=datetime.now(), number=10000, radius=1000)

o.run(duration=timedelta(hours=24))
o.animation(filename='opendrift_norkyst.mp4', background=['x_sea_water_velocity', 'y_sea_water_velocity'])
