import subprocess
import os
from Bio import SeqIO

def DownloadingSequences(bacteriaPath,archeaPath,outputPath):
	print("Downloading Bacteria Files")
	subprocess.run("ncbi-genome-download --genera \'"+bacteriaPath+"\' bacteria -F protein-fasta,fasta -o "+outputPath,shell=True)
	
	print("Downloading Archaea Files")
	subprocess.run("ncbi-genome-download --genera \'"+archeaPath+"\' archaea -F protein-fasta,fasta -o "+outputPath,shell=True)
	
	CleaningFolder(outputPath)	

def CleaningFolder(path):
	for root, dirs, files in os.walk(path):
		for file in files:
			if file.endswith('.gz'):
				subprocess.run("gunzip "+root+"/"+file,shell=True)
			#if file=="MD5SUMS":
			#	subprocess.run("rm "+root+"/"+file,shell=True)

def ParsingSequences(path):
	listePhylums=os.listdir(path)
	DictMain={*listePhylums}
	for phylum in listePhylums:
		for root,dirs,files in os.walk(path+'/'+phylum):
			if dirs:
				organismsList=dirs
			for file in files:
				seq=SeqIO.parse(root+'/'+file,"fasta")
				for ieq in seq:
				
					print(ieq.id)
		print((organismsList))

DownloadingSequences('../../data/Bacteria.list','../../data/Archea.list','../../data/')
#ParsingSequences('../../data/refseq')
