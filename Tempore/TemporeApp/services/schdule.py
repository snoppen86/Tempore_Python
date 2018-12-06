import datetime
from TemporeApp import views

def schdule_start_end_time_switcher(schduleStart:str, sceduleEnd:str):
    endtime = int(sceduleEnd)
    startime = schduleStart
    dt = datetime
    if endtime >= int(dt.time):
        return False
    elif endtime < int(dt.time):
        return True
