# SPDX-FileCopyrightText: © 2021 Antonio López Rivera <antonlopezr99@gmail.com>
# SPDX-License-Identifier: GPL-3.0-only


import numpy as np
from pyfiglet import Figlet

from alexandria.data_structs.array import ensure_ndarray


def d_dmdec(d):
    """
    Decimal degrees to
        dd :: mm.mm
    """
    d   = ensure_ndarray(d)
    deg = d.astype(int)
    mnt = (d % 1)*60

    return np.array((deg, mnt)).T.squeeze()


def d_dms(d):
    """
    Decimal degrees to
        dd :: mm :: ss.ss
    """
    d   = ensure_ndarray(d)
    deg = d.astype(int)
    mnt = (d % 1)   * 60
    sec = (mnt % 1) * 60

    return np.array((deg, mnt.astype(int), sec)).T


def title():
    s = Figlet()
    print("\n" + s.renderText('Sift'))
