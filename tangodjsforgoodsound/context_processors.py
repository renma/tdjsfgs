import datetime
from version import VERSION, TIMESTAMP


def appVersion(request):
    version = VERSION
    lastupdate = TIMESTAMP.split("<")[1].split()[0]
    y, m, d = lastupdate.split("-")
    d = datetime.date(int(y), int(m), int(d))
    formatted = d.strftime("%B %d, %Y")
    return {"APP_VERSION": version,
            "APP_DATE": lastupdate,
            "APP_DATE_FORMATTED": formatted,
            "APP_YEAR": y,
            "CURRENT_YEAR": datetime.datetime.now().year}
