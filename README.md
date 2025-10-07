# OpenPBS ifl in Python

# Prerequisites
 * Install: `libopenpbs-dev`
 * Configure: `/etc/pbs.conf`

# Compilation
 * run `make`

# Test run examples:
 * `python pbs_ifl-test.py server-name`
 * `PBS_AUTH_METHOD=resvport PBS_ENCRYPT_METHOD= python pbs_ifl-test.py server-name` 
 * `PBS_AUTH_METHOD=gss PBS_ENCRYPT_METHOD=gss python pbs_ifl-test.py server-name`

# More documentation:
 * Programming guide: https://help.altair.com/2022.1.0/PBS%20Professional/PBSProgramGuide2022.1.pdf