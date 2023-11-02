#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: Dong An
Date: 2023-11-02
Description: exlude some sequences  and trim some region to N from genome fasta file

#exclude.seq.id
Scaffold113
Scaffold42

#changeToN.id
Chr42   300-3000

usage:python 20231102-exclude-chrid-from-genome.py -i Esin.genomic.fna -o Esin.genomic.tmp1.fna -f exclude.seq.id -n changeToN.id
"""


import click
import re
from Bio import SeqIO


def rename_genome(inputfa, outputfa,exfile,nfile):
    with open(exfile,'r') as exfile, open(inputfa) as inputfa, open(outputfa,'w') as outputfa, open(nfile, "r") as nfile:
        chrdic={}
        chrlist=[]
        for chrid in exfile:
            chrlist.append(chrid.strip())
        
        for line in nfile:
            line=line.strip().split("\t")
            chrid,region=line[0],line[1]
            chrdic[chrid]=region

        records=SeqIO.parse(inputfa, 'fasta')
        for rec in records:           
            chrid = rec.description
            if chrid not in chrlist:
                if chrid in chrdic.keys():
                    region=chrdic[chrid]
                    if ',' in region:
                        splitregion=region.split(',')
                        print(splitregion)
                        for i in splitregion:
                            start=int(i.split('-')[0])
                            end=int(i.split('-')[1])
                            newseq=rec.seq[:start]+'N'*(end-start)+rec.seq[end:]
                            rec.seq=newseq
                    else:
                        start=int(region.split('-')[0])
                        end=int(region.split('-')[1])
                        newseq=rec.seq[:start]+'N'*(end-start)+rec.seq[end:]
                        rec.seq=newseq
                    SeqIO.write(rec,outputfa,"fasta") 
                else:
                    SeqIO.write(rec,outputfa,"fasta")        
 
@click.command()
@click.option('-i','--inputfa', help='请输入fasta文件')
@click.option('-o','--outputfa', help='请输入改名后fasta文件')
@click.option('-f','--exfile', help='请输入去掉染色体对应名字')
@click.option('-n','--nfile', help='请输入替换对应染色位置为N的染色体名字')


def main(inputfa, outputfa,exfile,nfile):
    rename_genome(inputfa, outputfa,exfile,nfile)

if __name__ == '__main__':
    main()
