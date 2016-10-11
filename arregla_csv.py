import collections

f = open('st_2013_01.csv','r')

#m_2015_est_01 = collections.OrderedDict({'MG02':1, 'LL01':2, 'TA01':3, 'MG05':4, 'VA04':5, 'LL07':6, 'VA03':7, 'AC02':8, 'MT09':9, 'BI02':10, 'VA05':11, 'LL03':12, 'DG06':13, 'LC01':14, 'AY02':15, 'BO01':16, 'MT07':17, 'ML02':18, 'MT02':19, 'CO06':20})

#m_2015_est_02 = collections.OrderedDict({'LC02':1, 'AC01':2, 'DG01':3, 'AF02':4, 'MT03':5, 'LL06':6, 'MG03':7, 'VA01':8, 'MG04' :9, 'AP01':10, 'MG01':11, 'MT01':12, 'VA02':13, 'LL04':14, 'LL02':15, 'CO04':16, 'LL05':17, 'CO01':18, 'CO05':19})

#m_2015_est_03 = collections.OrderedDict({'BO03':1, 'BI03':2, 'TA02':3, 'BO02':4, 'CO03':5, 'CO02':6, 'AC05':7, 'AC04':8, 'MT05':9, 'AF01':10 })


#m_2014_est_01 = collections.OrderedDict({'MG02':1, 'LL01':2, 'TA01':3, 'VA04':4, 'VA03':5, 'AC02':6, 'MT09':7, 'BI02':8, 'VA05':9, 'DG06':10, 'LC01':11, 'BO01':12, 'MT07':13, 'ML02':14, 'MT02':15, 'AC01':16, 'DG01':17, 'AC03':18, 'MT03':19, 'ME05':20, 'VA01':21})
#m_2014_est_02 = collections.OrderedDict({'AP01':1, 'DG11':2, 'MG01':3, 'MT01':4, 'VA02':5, 'LL02':6, 'CO04':7, 'DG13':8, 'MT06':9, 'CO01':10, 'BO03':11, 'BI03':12, 'TA02':13, 'BO02':14, 'CO03':15, 'CO02':16, 'ME03':17, 'AC05':18, 'AC04':19, 'MT05':20})


m_2013_est_01 = collections.OrderedDict({'LL01':1, 'TA01':2, 'DG06':3, 'DG01':4, 'AC03':5, 'ME05':6, 'VA01':7, 'AP01':8, 'DG11':9, 'MG01':10, 'DG05':11, 'VA02':12, 'DG13':13, 'AT03':14, 'BI03':15, 'MA02':16, 'CO02':17, 'ME03':18,'ME06':19})

h, w = 366 , len(m_2013_est_01) + 1

print h, w

Matrix = [[0 for x in range(w)] for y in range(h)]

col = 0
anterior = ''

for line in f.readlines():

    array = line.split()
    station =  array[0]

    if station != anterior:
       Matrix[0][col]=station
       anterior = station
       col += 1

    juliand =  int(array[1])


    gaps =  array[2]
    est =  int(m_2013_est_01[station])
    
    #print juliand,gaps,est 
    #try:
    Matrix[juliand][est] = gaps
    #except Exception, e:
    #    print 'error',juliand,gaps,est
    #    pass
    
f.close()
   

for i in range(h):
    if i == 0:
       fil = 'jul'
    else:
       fil = i
    #out = "[%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s]," % (fil, Matrix[i][0], Matrix[i][1], Matrix[i][2], Matrix[i][3], Matrix[i][4], Matrix[i][5], Matrix[i][6], Matrix[i][7], Matrix[i][8],Matrix[i][9])
    out = "[%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s]," % (fil, Matrix[i][0], Matrix[i][1], Matrix[i][2], Matrix[i][3], Matrix[i][4], Matrix[i][5], Matrix[i][6], Matrix[i][7], Matrix[i][8],Matrix[i][9],
Matrix[i][10],Matrix[i][11],Matrix[i][12],Matrix[i][13],Matrix[i][14],Matrix[i][15],Matrix[i][16],Matrix[i][17],Matrix[i][18])

    print out
