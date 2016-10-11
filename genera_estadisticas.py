f = open('2013.txt','r')
import re

totalseg=0
totalsam=0
ant = ''

#mis_estaciones=[]

#for line in f.readlines():
#    if re.search(r'^C1\.\w{3}.+\d{3}$',line):
#        wav = line[:-1]
#        station = wav[3:7]
#        if ant == station:
#           pass
#        else:
#           if station not in mis_estaciones:
#               mis_estaciones.append(station) 
#           ant = station
#print mis_estaciones

#st_2015_01 = ['MG02', 'LL01', 'TA01', 'MG05', 'VA04', 'LL07', 'VA03', 'AC02', 'MT09', 'BI02', 'VA05', 'LL03', 'DG06', 'LC01', 'AY02', 'BO01', 'MT07', 'ML02', 'MT02', 'CO06']
#st_2015_02 = ['LC02', 'AC01', 'DG01', 'AF02', 'MT03', 'LL06', 'MG03', 'VA01', 'MG04', 'AP01', 'MG01', 'MT01', 'VA02', 'LL04', 'LL02', 'CO04', 'LL05', 'CO01', 'CO05']
#st_2015_03 = ['BO03', 'BI03', 'TA02', 'BO02', 'CO03', 'CO02', 'AC05', 'AC04', 'MT05', 'AF01']

#st_2014_01 = ['MG02', 'LL01', 'TA01', 'VA04', 'VA03', 'AC02', 'MT09', 'BI02', 'VA05', 'DG06', 'LC01', 'BO01', 'MT07', 'ML02', 'MT02', 'AC01', 'DG01', 'AC03', 'MT03', 'ME05', 'VA01']
#st_2014_02 = ['AP01', 'DG11', 'MG01', 'MT01', 'VA02', 'LL02', 'CO04', 'DG13', 'MT06', 'CO01', 'BO03', 'BI03', 'TA02', 'BO02', 'CO03', 'CO02', 'ME03', 'AC05', 'AC04', 'MT05']

st_2013_01 = ['LL01', 'TA01', 'DG06', 'DG01', 'AC03', 'ME05', 'VA01', 'AP01', 'DG11', 'MG01', 'DG05', 'VA02', 'DG13', 'AT03', 'BI03', 'MA02', 'CO02', 'ME03', 'ME06']

for line in f.readlines():
     if re.search(r'^C1\.\w{3}.+\d{3}$',line):
        wav = line[:-1]
        #print 'start',wav
     elif re.search(r'^Total.+$',line):
        arr = (line[:-1]).split()
        
        #print wav[3:7],arr[1],arr[4],totalseg,totalsam
        station = wav[3:7]
        if station in st_2013_01:
           out = "%s\t%s\t%s" % (station,wav[20:28],int(totalseg/60))
           print out
        totalseg=0
        totalsam=0
     elif re.search('(?<=C1.......BHZ)',line):
        gap = (line[:-1]).split()
        seg = gap[3]
        samp = gap[4]
        #print "gap ",wav , gap[0],seg,samp
        totalseg = totalseg + float(seg)
        totalsam = totalsam + float(samp)

f.close()



