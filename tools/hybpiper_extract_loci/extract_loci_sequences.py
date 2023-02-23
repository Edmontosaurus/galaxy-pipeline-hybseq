#!/usr/bin/env python

'''
This script needs to be directed to the HybPiper output folder.
It then extracts all the fasta files from the loci that were generated by the HybPiper pipeline.

These fasta files can then be used to create several MSA's (multiple sequence alignments) for 
phylogenetic analysis.
'''
import os
import shutil
import argparse

def extract_loci(input_dir, output_dir):

    # Create the output directory if it doesn't already exist
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    # Loop through each sample directory
    for sample_dir in os.listdir(input_dir):
        # Check if the directory is a sample directory
        if not os.path.isdir(os.path.join(input_dir, sample_dir)):
            continue

        # Loop through each gene_xxx folder within the sample directory
        for gene_dir in os.listdir(os.path.join(input_dir, sample_dir)):
            if not gene_dir.startswith("gene"):
                continue
            # Navigate to the FNA folder within the gene_xxx folder
            fna_dir = os.path.join(input_dir, sample_dir, gene_dir, sample_dir,
                                   "sequences", "FNA")
            if os.path.isdir(fna_dir):
                # Loop through each FNA file within the FNA folder
                for fna_file in os.listdir(fna_dir):
                    # Check if the file is an FNA file
                    if not fna_file.endswith(".FNA"):
                        continue

                    # Create the output path for the file
                    output_file = os.path.join(output_dir,
                                               sample_dir + "_" + gene_dir + ".FNA")

                    # Copy the file to the output directory
                    shutil.copy(os.path.join(fna_dir, fna_file), output_file)
                    print("Copied {} to {}".format(os.path.join(fna_dir, fna_file),
                                                   output_file))


def parseArgvs():
    """This runs the argparse command in order to handle the input arguments
    from the command line.
    """
    parser = argparse.ArgumentParser(prog="extract_loci_sequences.py",
                                     description="Script to search the loci "
                                                 "sequences from standard "
                                                 " HybPiper output folder.")
    parser.add_argument("-v", "--version", action="version",
                        version="extract_loci_sequences.py 0.0.9")
    parser.add_argument("-f", "--hybpiperfolder", action="store", dest="input_path",
                        help="The path/location where the script should extract the loci from",
                        required=True)
    parser.add_argument("-o", "--outputfolder", action="store", dest="output_path",
                        help="The path/location where the script should extract the loci to",
                        required=True)
    argvs = parser.parse_args()
    return argvs


def main():
    argvs = parseArgvs()
    input_path = argvs.input_path
    output_path = argvs.output_path

    extract_loci(input_path, output_path)

    
if __name__ == '__main__':
    main()