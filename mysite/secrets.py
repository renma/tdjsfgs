import os


def readSecret(n):
    home = os.path.expanduser("~")
    if home == "/home/rene":
        filename = os.path.join(home, "mysite", "tdjsfgs.topsecret")
    else:
        filename = os.path.join(home, "ALL", "mysite", "tdjsfgs.topsecret")
    if os.path.exists(filename):
        lines = []
        for line in open(filename, "r").readlines():
            if not line.startswith("#") and len(line) > 3:
                lines.append(line)
        try:
            return lines[n]
        except IndexError:
            pass
    return ""
