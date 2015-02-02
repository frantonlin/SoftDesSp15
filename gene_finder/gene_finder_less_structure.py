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

    comps = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    rev_comp = "".join([comps[nucleo] for nucleo in dna])[::-1]

    return rev_comp

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """

    # initialize variables
    ORFs = []
    frames = [[], [], [], [], [], []]

    # get reverse complement
    rdna = get_reverse_complement(dna)

    # split all six frames into lists of length-3 strings
    for i in range(0, len(dna)):
        if i+3 <= len(dna):
            if i%3 == 0:    # first frames
                frames[0].append(dna[i:i+3])
                frames[1].append(rdna[i:i+3])
            elif i%3 == 1:  # second frames
                frames[2].append(dna[i:i+3])
                frames[3].append(rdna[i:i+3])
            elif i%3 == 2:  # third frames
                frames[4].append(dna[i:i+3])
                frames[5].append(rdna[i:i+3])

    # iterate through each frame looking for ORFs
    for frame in frames:
        ind = -1    # the index of the current ORF (-1 if searching)
        for i in range(0, len(frame)):
            if frame[i] == 'ATG' and ind == -1:             # found a start
                ORFs.append(frame[i])
                ind = len(ORFs) - 1
            elif ind != -1:
                if frame[i] != 'TAG' and 'TAA' and 'TGA':   # not end yet
                    ORFs[ind] += frame[i]
                else:                                       # found an end
                    ind = -1

    return ORFs

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