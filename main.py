from datetime import datetime
from math import ceil
import sys
import time

def main(args):
  if len(args) > 1:
    now = int(args[1])
  else:
    now = time.time()

  dt = datetime.utcfromtimestamp(now)
  print("Wall time (UTC): " + dt.isoformat(' '))

  epoch_year = 1970
  year = dt.year - epoch_year # may be negative
  day = dt.timetuple().tm_yday
  week = ceil(day / 10.0)

  hour = dt.hour
  minute = dt.minute

  print(f'{year}.{day} pu {hour}:{minute}')


main(sys.argv)
