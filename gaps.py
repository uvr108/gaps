from obspy.core import read
#from obspy.core import read,Stream,UTCDateTime
#from obspy.xseed import Parser
import re
import os


year_dir = "2013"


if (os.path.exists(year_dir)):
    for net in os.listdir(year_dir):
        for st in os.listdir(year_dir + '/' + net):
            try: 
               for channel in os.listdir('/run/media/ulises/data/' + year_dir + '/' + net + '/' + st):
                   try:
                       direc = '/run/media/ulises/data/' + year_dir + '/' + net + '/' + st + '/' + channel
                   except Exception, e:
                       print e 
                       pass
                   os.chdir(direc)
                       #print os.getcwd()
                   for wavs in os.listdir(os.getcwd()):
                       match = re.search(r'BHZ',wavs)
                       if match:
                          print wavs
                          st = read(wavs)
                          st.get_gaps()
                          st.print_gaps()
            except:
                   raise
