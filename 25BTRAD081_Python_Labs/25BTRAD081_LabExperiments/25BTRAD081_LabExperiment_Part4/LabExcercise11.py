try:
   with open("log.txt", "r") as file:
       logs = file.readlines()
 
   error = 0
   warning = 0
   info = 0
 
   for line in logs:
       if "ERROR" in line:
           error += 1
       elif "WARNING" in line:
           warning += 1
       elif "INFO" in line:
           info += 1
 
   if not logs:
       print("Log file is empty.")
   else:
       print("Log File Summary")
       print("ERROR:", error)
       print("WARNING:", warning)
       print("INFO:", info)
 
except FileNotFoundError:
    print("Log file not found.")