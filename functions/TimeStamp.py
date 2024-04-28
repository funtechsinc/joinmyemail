import datetime


def Get_Time_Stamp() -> str:
    timestamp = datetime.datetime.today()
    return str(timestamp)


