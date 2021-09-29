# SPDX-FileCopyrightText: © 2021 Antonio López Rivera <antonlopezr99@gmail.com>
# SPDX-License-Identifier: GPL-3.0-only


from pyfiglet import Figlet


def d_to_dms(n):
    """
    Decimal degrees to
        dd :: mm :: ss.ss
    """
    mnt, sec = divmod(n*3600, 60)
    deg, mnt = divmod(mnt, 60)
    return int(deg), int(mnt), sec


def title():
    s = Figlet()
    print("\n" + s.renderText('Sift'))
