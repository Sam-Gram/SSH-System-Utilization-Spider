# SSH-System-Utilization-Spider
Grabs info on uptime from BYU-Idaho's Linux Lab
This was super hacky and used cron.d to poll the Linux Lab at random every 15 minutes.

## File info: 
### puller.py:
Does the work of going out and grabbing the info by executing an ssh connectinon to the linux lab.
This requires the use of setting up a Linux Lab account using `ssh-copy`.

### puller.sh
Runs puller.py
Note that this weird hack was run on a Raspberry Pi and that the absolute path is still in the project.

### data.txt
Sample data from the Linux lab.
You should see some failed SSH connections in the form of multiple IP suffixes being used on one line.
