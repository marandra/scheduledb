import time
import os

#config schedule and contact data
day_of_week = '*'
hour = '*'
minute = '*'
second = '*/21'
person = 'Ross Mccants'
email = 'ross.mccants@unibas.ch'


def run(PATH, FLAGFINISHED):

    ### BEGINING OF DOWNLOAD SCRIPT ###
    timestr = time.strftime("%H:%M:%S", time.localtime())
    open('{}/DATABASE-{}'.format(PATH, timestr), 'w').close()
    time.sleep(5)
    ### END OF DOWNLOAD SCRIPT ###

    open('{}/{}'.format(PATH, FLAGFINISHED), 'w').close()
    return 

############################################

if __name__ == '__main__':
    run('../pending/db1', 'FINISHED_DOWNLOAD')
