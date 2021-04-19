# Its ok if this flows into next week

# Ping
Starting with simple ping script / interactive mode
```
import platform
import os
pingCMD = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"
os.system(pingCMD)
```

# Conditionals
Show how conditionals work (if, elif, else) and evaluations (<>=)
- Build out conditionals.py without function 1 evaluation at a time
- Debug if necessary
Add in conditionals to accomidate Windows or Linux
- Try command on a Windows machine to see how it works differntly?
- save as pinger1.py
- use debugger to walk through it

# Loops
Show how loops work
- simple FOR loop `for x in range(6):`
- If time later, come back to more loop types
Add in loop to loop through multiple IPs
- start with simple print statement to show how to loop and how it will work
- use debugger to walk through
```
startIP = "192.168.0."
for x in range(254):
ip = startIP + str(x + 1)
print(ip)
```
- extend pinger1.py into pinger2.py
- use debugger if necessary

# Functions
Show how functions work
- reusable code
- send input
- receive output
Move ping command into function
- receive IP as input, return exit_code
- save as pinger3.py
- debug if necessary

