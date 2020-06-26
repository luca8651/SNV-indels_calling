#!/usr/bin/env python3.5
import csv
import os
import re
import sys
from difflib import ndiff
from difflib import SequenceMatcher



#usage: compare_featurecounts_mouse_NMR.py  featurecounts_sp1.txt featurecounts_sp2.txt  orthologues_file.txt
#featurecounts_sp1.txt featurecounts_sp2.txt: output of featureCounts (test version: subread/1.5.1) with options "-p -t exon" for species 1 and 2, respectively. These files store the read counts for each gene   
#orthologues_file.txt: tsv file with 2 columns of gene ids, describing the orthologue relations between genes in species 1 (column1) and species 2 (column2). These ids must match the ids provided in the other 2 input files!

if len(sys.argv)==1:
	print("A script to compare gene coverage across species, using orthology information")
	print("usage: compare_featurecounts_mouse_NMR.py  featurecounts_sp1.txt featurecounts_sp2.txt  orthologues_file.txt  ")
	print(" ")
	print("featurecounts_sp1.txt featurecounts_sp2.txt: output of featureCounts (test version: subread/1.5.1)")
	print("with options \"-p -t exon\" for species 1 and 2, respectively")
	print(" ")
	print("orthologues_file.txt: tsv file with 2 columns of gene ids, describing the orthologue relations between")
	print(" genes in species 1 (column1) and species 2 (column2). These ids must match the ids provided in the other 2 input files!")
	sys.exit(1)


feature1 = sys.argv[1]
feature2 = sys.argv[2]
orthofile = sys.argv[3]


cont=0
#cont2=0

count_dict = dict([])
count_dict2 = dict([])
ortho_dict = dict([])

with open(feature1,'r') as f:
	for line in f:
		line1=line.split("\t")
#		print(line1)
		if line[0]!="#":
			gene=line1[0]
			gene=gene.strip('\n')
			count=line1[6]
			count=count.strip('\n')
			count_dict[gene]=count
#			print("count for gene "+ gene + " in file1  is "+count_dict[gene])

with open(feature2,'r') as f:
	for line in f:
		line1=line.split("\t")
		if line[0]!="#":
			gene=line1[0]
			gene=gene.strip('\n')
			count=line1[6]
			count=count.strip('\n')
			count_dict2[gene]=count
#			print("count for gene "+ gene + " in file2 is "+count_dict2[gene])


with open(orthofile,'r') as f:
	for line in f:
		line1=line.split("\t")
		geneM=line1[0]
		geneM=geneM.strip('\n')
		geneN=line1[1]
		geneN=geneN.strip('\n')
		ortho_dict[geneM]=geneN            #index is mouse id, the value is NMR id
#		print("orthologue for gene "+ geneM + " is "+ortho_dict[geneM])


for key in ortho_dict:
	geneM=key
	geneN=ortho_dict[key]
	if (key in count_dict) and (geneN in count_dict2):
#	if (key in count_dict):
#		print(key+" and "+geneN)
		print(geneM+"\t"+geneN+"\t"+count_dict[key]+"\t"+count_dict2[geneN])
#	print(geneM+"\t"+geneN+"\t"+count_dict2[geneN])
#	if (key in count_dict):
#		print(geneM+"\t"+geneN+"\t"+count_dict[key])
