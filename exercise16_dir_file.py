# We only need to import this module
import os.path
 
# The top argument for walk. The
# Python27/Lib/site-packages folder in my case.
topdir = '.'
 
# The arg argument for walk, and subsequently ext for step
exten = '.txt'
 
logname = 'findfiletype.log'
 
def step((ext, logpath), dirname, names):
    ext = exten.lower()
 
    for name in names:
        if name.lower().endswith(ext):
            # Instead of printing, open up the log file for appending
            with open(logpath, 'a') as logfile:
                logfile.write('%s\n' % os.path.join(dirname, name))
 
# Change the arg to a tuple containing the file
# extension and the log file name. Start the walk.
os.path.walk(topdir, step, (exten, logname))