import pyximport; pyximport.install()
import pebble



if __name__ == '__main__':
    G = pebble.lattice() # initialize a lattice

    # add a few bonds:

    # 1---2---3
    # : .':'.':
    # 4---5---6
    # :   :   :
    # 7---8---9
    # : .': .':
    #10--11--12

    bond = [(1,2),(2,3),(1,4),(2,5),(2,6),(3,6),(2,4),(3,5),(4,5),
            (5,6),(4,7),(5,8),(6,9),(7,8),(8,9),(7,10),
            (8,11),(9,12),(8,10),(9,11),(10,11),(11,12)]
    assert len(bond) == 22 # check bond number counting
    print '---------adding bond-----------'
    for i in bond:
        # add bond
        if G.add_bond(i[0],i[1]): # if the bond is independent, add_bond returns True, otherwise False
            print 'added bond %d --- %d, independent bond'%i
        else:
            print 'added bond %d --- %d, redundent bond'%i
    print '-------------------------------\n\n'

    # check simple statistics:
    G.stat()
    print '---------statistics-----------'
    print 'site number: %d'%G.statistics['site']
    print 'bond number: %d'%G.statistics['bond']
    print 'floppy mode count: %d'%G.statistics['floppy_mode']
    print 'state of self-stress counting: %d'%G.statistics['self_stress']
    print '------------------------------\n\n'

    # decompose into rigid components:
    G.decompose_into_cluster()
    print '---------rigid cluster-----------'
    print 'cluster number: %d'%G.cluster['count']
    for key,value in G.cluster['index'].iteritems():
        print 'cluster %d has %d bonds'%(key,len(value))
        print 'the bonds are:'
        for i in value:
            print '%d ------ %d'%i
    print '---------------------------------\n\n'


    # decompose stressed bond:
    G.decompose_stress()
    print '---------stressed bond-----------'
    print 'there are %d stressed bond,they are:'%len(G.stress)
    for i in G.stress:
        print '%d ------ %d'%i
    print '---------------------------------\n\n'

    # utilities:
    print '-----------utilities------------'
    print 'test if 2 sites are relatively rigid:'
    if G.collect_four_pebble(1,5):  # if 4 pebble can be collected, return True: the two sites are not rigid.
        print 'site 1 and 5 are relatively floppy'
    else:
        print 'site 1 and 5 are relatively rigid'
    print 'raw graph:'
    print G.graph
    print 'raw directed graph with pebble number, format: {site number:[list of connected sites, pebble number]}'
    print G.digraph
    print '--------------------------------\n\n'









