# agglomerative hierarchial clustering
# 5114100701
import ConfigParser
from copy import deepcopy
import math
import os

def cluster(a, n, depth):
    if n <= 1:
        global cluster_tabel
        cluster_tabel.append(a)
    else:
        for i in xrange(0,len(a)):
            cluster(a[i], n-depth, depth+1)

def update(nama, a, tabel):
    global linkage
    for i in xrange(0, len(tabel)):
        for j in xrange(0, len(tabel)):
            if i == nama.index(nama[a]) or j == nama.index(nama[a]):
                if i == j:
                    tabel[i][j] = 0
                else:
                    temp=[]
                    for k in nama[i]:
                        for l in nama[j]:
                            temp.append(main_tabel[main_nama.index(k)][main_nama.index(l)])
                    if linkage == 'single':
                        tabel[i][j] = min(temp)
                    elif linkage == 'complete':
                        tabel[i][j] = max(temp)
    return tabel

def merger(nama, a, b, tabel, tree):
    temp = []
    temp.append(tree[a])
    temp.append(tree[b])
    tree[a] = temp
    tree.remove(tree[b])

    nama[a] = nama[a] + nama[b]
    nama.remove(nama[b])

    del tabel[b]
    for i in xrange(0,len(tabel)):
        del tabel[i][b]
    tabel = update(nama, a, tabel)
    return nama, tabel, tree

def find_merge(a, minimum):
    return [(ind, a[ind].index(minimum)) for ind in xrange(len(a)) if minimum in a[ind]]

def find_minimum(tabel):
    global linkage
    temp = []
    for i in tabel:
        temp.append(min([j for j in i if j!=0]))
    return min(temp)

def distance(a, b):
    # compute euclidean
    result = 0

    if a == b:
        return 0
    else:
        for i in xrange(1, len(a)):
            result += pow(a[i] - b[i], 2)

        return float("%0.2f" % math.sqrt(result))

def create_tabel(dataset):
    table = []
    for i in dataset:
        temp = []
        for j in dataset:
            x = distance(i, j)
            temp.append(x)
        table.append(temp)
    return table

# read dataset
Config = ConfigParser.ConfigParser()
Config.read("dataset.txt")
data = int(Config.get('Configuration', 'data'))
x = int(Config.get('Configuration', 'x'))
linkage = Config.get('Configuration', 'linkage')

# introduction
print '-------------------------------------------------------'
print '         Agglomerative Hierarchial Clustering'
print '-------------------------------------------------------'
print '5114100108-5114100179-5114100701-5112100165-51112100702'
print '-------------------------------------------------------'

# create list of list in a and print dataset
dataset = []
print 'Dataset:'
for i in xrange(0, data):
    temp = []
    temp.append(Config.get('Data', str(i+1) + '.name'))
    for j in xrange(0, x):
        temp.append(float(Config.get('Data', str(i+1) + '.x' + str(j+1))))
    dataset.append(temp)
    print temp

main_nama = [i[0] for i in dataset]
nama = deepcopy(main_nama)
tree = deepcopy(main_nama)
main_tabel = create_tabel(dataset)
tabel = deepcopy(main_tabel)
while len(nama) != 1:
    print "\nTable:"
    print "\t", nama
    for i in xrange(0, len(tabel)):
        print nama[i], "\t", tabel[i]
    minimum = find_minimum(tabel)
    print "\nMinimum distance from table above is :", minimum
    merge = find_merge(tabel, minimum)
    print "\nMerge :", nama[merge[0][0]], "and", nama[merge[0][1]]
    nama, tabel, tree = merger(nama, merge[0][0], merge[0][1], tabel,tree)
    os.system("pause")

tree = tree[0]
print "\nfinal result :", tree, '\n'

# print cluster with error handling (:
n = int(Config.get('Configuration', 'cluster'))
cluster_tabel = []
cluster(tree, n, 1)

print "Result in", len(cluster_tabel), "Cluster :"
for i in cluster_tabel:
    print "Cluster :", i

# end of program
print '\nThx for using this program . . . (:\n'

os.system("pause")
