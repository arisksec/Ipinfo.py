#!/usr/bin/env python3
# author: @xdavidhu

import requests, json, sys, socket

if len(sys.argv) > 1:
    ip = sys.argv[1]
else:
    ip = False

if not ip:
    url = "https://ipinfo.io/"
else:
    try:
        socket.inet_aton(ip)
        domain = False
    except socket.error:
        domain = True
    if domain:
        try:
            ip = socket.gethostbyname(ip)
        except:
            print("invalid domain name...")
            sys.exit()
    url = "https://ipinfo.io/" + str(ip)

try:
    r = requests.get(url)
except:
    print("error while querying info...")
    sys.exit()

data = json.loads(r.text)

text = """
      _,-===-,_       ipinfo v1.0 by @xdavidhu
    ,/ ",,/\8888.
   /    ="\V=8)88\    target:    {0}
  ,    d88boodb="V.   city:      {1}
  |   (8888888?' '|   region:    {2}
  `b   " `8sm8"   '   country:   {3}
   \      8888,' /    loc:       {4}
    `     `T/   '     org:       {5}
      ` ..... '       postal:    {6}
"""

text = text.format(data.get("ip", "[NO DATA]"), data.get("city", "[NO DATA]"), \
                            data.get("region", "[NO DATA]"), \
                            data.get("country", "[NO DATA]"), \
                            data.get("loc", "[NO DATA]"), \
                            data.get("org", "[NO DATA]"), \
                            data.get("postal", "[NO DATA]"))

print(text)
