#take a list of arguments and make a crossproduct to get all parameter pairs

from itertools import product
from os import system
import multiprocessing as mp

para = ['a1','b1','c1']
parb = ['a2','b2','c2']
parc = ['a3','b3','c3']

#and as many as you want

argumentlist = [x for x in product(para,parb,parc)]

#commands you want to run and the outfile, caution, the outfile should be empty
#you may want to make that sure with
#system('rm '+outfile)
command = 'echo'
outfile = 'test'

def run_calculation(argument):
        argument_string = reduce(lambda x,y: x+' '+y,argument)
        print argument_string
        system(command + ' ' + argument_string + ">>" + outfile)



n_cpu = mp.cpu_count()
pool = mp.Pool(-1) #this should use all available cpus, use n_cpu/2 if you


for argument in argumentlist:
    pool.apply_async(run_calculation,args=(argument,) )

pool.close()
pool.join()
print 'done'



import MySQLdb

db = MySQLdb.connect(host='localhost',
                     user='heiko',
                     passwd='ultrasecret',
                     db = 'heikosdb')

cur = db.cursor()

for line in open(outfile):
    data = line.split()
    cur.execute("""INSERT INTO yourtable VALUES ('{0}', '{1}','youroutput','lookslike')""".format(data[0],data[1])) 

    
