import os
import time
def required_packages():
    os.system("clear")
    print("[+] Checking if necessary packages are installed...")
    time.sleep(2)
    print("[+] Installing necessary packages, please wait...")
    os.system("pkg update ; pkg install x11-repo termux-x11-nightly pulseaudio xfce4 xfce4-goodies chromium code-oss")
    print("[+] All necessary packages are installed. You can now run the script")
if __name__ == '__main__':
    required_packages()
