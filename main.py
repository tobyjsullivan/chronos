import time

def main():
  custom_epoch = 532324800
  est_end = custom_epoch + 2524608000
  now = time.time()
  print("Wall time: " + time.ctime(now))

  diff_secs = int(now) - custom_epoch
  diff_hours = int(diff_secs / 3600)
  diff_days = int(diff_hours / 24)
  diff_years = int(diff_days / 365)
  print("Hours elapsed: ", diff_hours)
  print("Days elapsed: ", diff_days)
  print("Years elapsed: ", diff_years)

  rem_secs = est_end - int(now)
  rem_hours = int(rem_secs / 3600)
  rem_days = int(rem_hours / 24)
  rem_years = int(rem_days / 365)
  print("Hours remaining (est.): ", rem_hours)
  print("Days remaining (est.): ", rem_days)
  print("Years remaining (est.): ", rem_years)

main()
