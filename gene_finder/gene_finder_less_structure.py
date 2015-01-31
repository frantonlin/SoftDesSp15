# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Franton Lin

"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids_less_structure import aa, codons
import random
from load import load_seq

### YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###
#def test(teststring):
#    for i in range(0, len(teststring)):
#        print teststring + " " + str(i)

def get_reverse_complement(dna):
    """ Gets the reverse complement of the given DNA sequence.

        dna: a DNA sequence
        returns: the reverse complement
    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    """
    complement = ""
    length = len(dna)
    for i in range(1, length + 1):
        if dna[length - i] == 'A':
            complement += 'T'
        elif dna[length - i] == 'T':
            complement += 'A'
        elif dna[length - i] == 'G':
            complement += 'C'
        else:
            complement += 'G'
    return complement

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """

    ORFs = []
    
    split1 = " ".join([dna[i:i+3] for i in range(0, len(dna)-len(dna)%3, 3)])
    split2 = " ".join([dna[i:i+3] for i in range(1, len(dna)-1-len(dna)%3, 3)])
    split3 = " ".join([dna[i:i+3] for i in range(2, len(dna)-2-len(dna)%3, 3)])
    print split1
    print split2
    print split3

    if(split1.find('ATG') != -1 & any(stop in split1 for stop in ['TAG', 'TAA', 'TGA'])):
        ORFs.append(split1[split1.find('ATG'):min(i for i in [split1.find('TAG'), split1.find('TAA'), split1.find('TGA')] if i > 0)])
        # remove ORF from split1
        
    if(split1.find('ATG') != -1 & any(stop in split1 for stop in ['TAG', 'TAA', 'TGA'])):
        print "I've made a terrible mistake..."

    print ORFs
    pass

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """
    # TODO: implement this
    pass


def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    # TODO: implement this
    pass

def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
    """
    # TODO: implement this
    pass

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    # TODO: implement this
    pass

if __name__ == "__main__":
    #print "Reverse complement of ATGCCCGCTTT is\t" + get_reverse_complement("ATGCCCGCTTT")
    #print "Expected:\t\t\t\t\tAAAGCGGGCAT\n"
    #print "Reverse complement of CCGCGTTCA is\t\t" + get_reverse_complement("CCGCGTTCA")
    #print "Expected:\t\t\t\t\tTGAACGCGG"
    import doctest
    doctest.testmod()