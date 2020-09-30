import datetime

def savelog(data):
    now_time = datetime.datetime.now()
    time_str = datetime.datetime.strftime(now_time,'%Y-%m-%d %H:%M:%S')
    savelog_file = open(r'D:\Users\python\savelog.txt','a')
    savelog_file.write(time_str + '\t' + data+'\n')
    print(time_str + '\t' + data)
    savelog_file.close()
    huehdihfis

class Bulletrepository(object):
    SAVEPATH = r'D:\Users\python\savelog.txt'
    def __init__(self):
        pass











