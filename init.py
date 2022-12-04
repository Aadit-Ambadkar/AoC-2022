import datetime

d = datetime.datetime.now()
date = int(d.strftime("%d"))+1
f = open("template.py", "r")
template = f.read()
template = template.replace("<REP>", str(date))
with open(f"day{date}.py", "w") as out:
    out.write(template)

f.close()