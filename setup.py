# First boot - Base setup
# Link from MD
# wget https://raw.githubusercontent.com/cms66/rpi-homenet/main/setup.py; sudo python ./setup.py
# Assumes
# - rpi imager used to configure
#    - user/password
#    - hostname

# Imports
import subprocess, sys, os

# Run commands
print("Python setup")
subprocess.run(["wget", "https://raw.githubusercontent.com/cms66/rpi-homenet/main/base_setup.sh"]) # Download bash script
subprocess.run(["sudo", "bash", "./base_setup.sh"]) # Run Bash script (as root)
subprocess.run(["sudo", "rm", "-f", "./base_setup.sh"]) # Delete bash script (as root)
usropt=input("Base seup done, press p to poweroff or any other key to reboot: ").lower() # reboot/poweroff
os.remove(__file__) # Delete python script
if usropt == 'p':
    print ("Poweroff selected")
    subprocess.call(["shutdown", "-s", "now"])
else:
    print ("Reboot selected")
    subprocess.call(["shutdown", "-r", "now"])
