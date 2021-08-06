def d_to_dms(n):
    """
    Decimal degrees to
        dd :: mm :: ss.ss
    """
    mnt, sec = divmod(n*3600, 60)
    deg, mnt = divmod(mnt, 60)
    return int(deg), int(mnt), sec
