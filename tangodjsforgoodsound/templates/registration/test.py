import os
for f in os.listdir("."):
    if os.path.isfile(f):
        x = f.replace(".html", "")
        x = "id=\"%s\"" % x
        if x not in open(f).read():
            print "FAIL:", f
