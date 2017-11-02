import datetime
from version import VERSION, TIMESTAMP


def appData(request):
    version = VERSION
    lastupdate = TIMESTAMP.split("<")[1].split()[0]
    y, m, d = lastupdate.split("-")
    return {"APP_VERSION": version,
            "APP_DATE": lastupdate,
            "APP_YEAR": y,
            "CURRENT_YEAR": datetime.datetime.now().year}
