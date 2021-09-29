# SPDX-FileCopyrightText: © 2021 Antonio López Rivera <antonlopezr99@gmail.com>
# SPDX-License-Identifier: GPL-3.0-only

import numpy as np

from sift.utils import d_to_dms

safety_zone_inta = np.array([[-6.750, 37.150],
                             [-7.358, 37.041],
                             [-7.358, 36.333],
                             [-7.361, 35.949],
                             [-6.707, 35.856],
                             [-6.633, 36.212],
                             [-6.488, 36.855],
                             [-6.750, 37.150]])

print([(d_to_dms(d[0]), d_to_dms(d[1])) for d in safety_zone_inta])
