import CUcourseopen
import sendAlertEmail
import sys
from datetime import datetime

loop = True
iter = 0
val = 0;
course = sys.argv[1]

while loop:
    op = CUcourseopen.getOpen(course)
    print op
    if("open" in op.values()):
        sys.stdout.write("SOMEONE DROPPED " + course + " AT " + str(datetime.now()) + "\n")
        sys.stdout.flush()
        sendAlertEmail.sendEmail("SOMEONE DROPPED " + course + "!", sys.argv[2])