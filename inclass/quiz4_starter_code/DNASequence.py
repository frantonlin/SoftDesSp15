class DNASequence(object):
    """ Represents a sequence of DNA """
    def __init__(self, nucleotides):
        """ constructs a DNASequence with the specified nucleotides.
             nucleotides: the nucleotides represented as a string of
                          capital letters consisting of A's, C's, G's, and T's """
        self.nucleotides = nucleotides
 
    def __str__(self):
        """ Returns a string containing the nucleotides in the DNASequence
        >>> seq = DNASequence("TTTGCC")
        >>> print seq
        TTTGCC
        """
        return self.nucleotides

    def get_reverse_complement(self):
        """ Returns the reverse complement DNA sequence represented
            as an object of type DNASequence

            >>> seq = DNASequence("ATGC")
            >>> rev = seq.get_reverse_complement()
            >>> print rev
            GCAT
            >>> print type(rev)
            <class '__main__.DNASequence'>
        """
        comps = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
        rev_comp = "".join([comps[nucleo] for nucleo in self.nucleotides])[::-1]

        return DNASequence(rev_comp)

    def get_proportion_ACGT(self):
        """ Computes the proportion of nucleotides in the DNA sequence
            that are 'A', 'C', 'G', and 'T'
            returns: a dictionary where each key is a nucleotide and the
                corresponding value is the proportion of nucleotides in the
            DNA sequence that are that nucleotide.
            (NOTE: this doctest will not necessarily always pass due to key
                    re-ordering don't worry about matching the order)
        >>> seq = DNASequence("AAGAGCGCTA")
        >>> d = seq.get_proportion_ACGT()
        >>> print (d['A'], d['C'], d['G'], d['T'])
        (0.4, 0.2, 0.3, 0.1)
        """

        #props = {'A':0, 'C':0, 'G':0, 'T':0}
        #for c in self.nucleotides:
        #    props[c] += 1
        #for nucleo in props:
        #    props[nucleo] = props[nucleo] / float(len(self.nucleotides))

        #print self.nucleotides.count('A')

        #return props
        return {nucleo:self.nucleotides.count(nucleo)/float(len(self.nucleotides)) for nucleo 
            in ['A', 'C', 'G', 'T']}


if __name__ == '__main__':
    import doctest
    doctest.testmod()
