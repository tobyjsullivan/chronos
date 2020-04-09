from datetime import datetime
import sys
import time

def main(args):
  if len(args) > 1:
    now = int(args[1])
  else:
    now = time.time()

  dt = datetime.utcfromtimestamp(now)
  print("Wall time (UTC): " + dt.isoformat(' '))

  hours = int(now / 3600)
  print("Hour: ", hours)


main(sys.argv)
