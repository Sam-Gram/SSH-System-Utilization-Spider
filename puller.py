import subprocess
import os
import random
random.seed(None)
whichComputer = random.randint(os.environ.get('DATAPULLER_LOWER_BOUND') ||  1,
                               os.environ.get('DATAPULLER_UPPER_BOUND') || 255)
p = subprocess.Popen(['ssh', (os.environ.get('DATAPULLER_BASE') || str(ARGV[1]) || 'localhost') +
                      str(whichComputer), '-p', (os.environ.get('DATAPULLER_PORT') || str(ARGV[0]) || '22'), 'uptime'],
                     stdout=subprocess.PIPE)
(output, err) = p.communicate()
with open("data.txt", "a") as myfile:
    myfile.write(str(whichComputer) + ' ' + output)
