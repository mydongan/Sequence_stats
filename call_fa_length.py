# -*- coding: utf-8 -*-

import re
import os
import sys
from Bio import SeqIO
from Bio.Seq import Seq
import click

  
def call_fasta_length(infile,outfile):
    with open(infile) as fastafile,open (outfile,'w') as out:
        records = SeqIO.parse(fastafile,"fasta")
        for rec in records:
            length=len(rec)
            out.write(rec.description+'\t'+str(length)+'\n') 
                

@click.command()
@click.option('-i','--infile', help='请输入fasta文件,统计fasta的基本信息，包括长度，GC含量，gap数，ScaffoldN50，ContigN50, 输出文件为gap和contig的bed文件')
@click.option('-o','--outfile', help='输出每条序列的长度')

def main(infile,outfile):    
    call_fasta_length(infile,outfile)
    
if __name__ == '__main__':
    main()  

 
