import time

def main():
  now = time.time()
  print("Wall time: " + time.ctime(now))

  hours = int(now / 3600)
  print("Hour: ", hours)

main()
