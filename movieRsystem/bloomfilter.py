import math
import mmh3
import bitarray

class bloomfilter():
    def __init__(self, totalitems, bits=None, hashes=None):        
        # calculates the false positive probability of the program
        self.falsepositive = self.get_falsepositive()

        # calculates the size of the bit array
        self.bitsize = self.get_size(totalitems, self.falsepositive)

        # calculates the optimum number of hash functions to be used
        self.hashfunctions = self.get_hashfunctions(self.bitsize, totalitems)

        # total items added
        self.itemsadded = 0

        # give the bit array of a given size
        self.bitarray = bitarray.bitarray(self.bitsize)
 
        # this initialize all bits as 0
        self.bitarray.setall(0)

    def add(self, item):
        bits = []
        for x in range(self.hashfunctions):
 
            # adding the value in the array
            bit = mmh3.hash(item, x) % self.bitsize
            bits.append(bit)
 
            # set the bit True in bit_array
            self.bitarray[bit] = True
        self.itemsadded += 1

    def check(self, item):
        
        #checks whether an item already exists in the bloom filter
        for i in range(self.hashfunctions):
            bit = mmh3.hash(item, i) % self.bitsize
            if self.bitarray[bit] == False:
        #False suggests that the item is not present
        #In any other case, there is a probability of the existence of the item
                return False
        return True

    def get_falsepositive(self):

        #formula below to calculate the false positive probability
        #the formula was extracted from one of the research articles
        return (1- math.exp(-(self.hashfunctions * self.itemsadded) / self.bitsize)) ** self.hashfunctions

    def get_hashfunctions(self, bitsize, totalitems):

        #returns the hash functions(k) to be used
        k = (bitsize/totalitems) * math.log(2)
        return int(k)

    def get_size(self, totalitems, falsepositive):

        #returns the size of bit array(m) to used
        m = -(totalitems* math.log(falsepositive))/(math.log(2)**2)
        return int(m)

    def content_similiarity(self, new):

        # comparing the content with other content
        # a value would be obtained which would determine the similarity of the content
        similiararray = self.bit_array & new.bitarray
        return (2*(similiararray.count()))/(self.bitarray.count(1) + new.bitarray.count(1))