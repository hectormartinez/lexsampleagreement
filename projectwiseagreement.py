import argparse
import sys
import random
from collections import Counter
import os
import nltk

somethingwrong = False
annotationsfromeach = Counter()



def getannotations(filename,annotatorid):

    annotations = []
    fin = open(filename,mode="r")


    instanceid = ""
    for line in fin.readlines():
        #print(line)
        line = line.strip()
        if line:
            linearray = line.split("\t")
            if line.startswith("#"):
                pass
                #if line.startswith("#id="):
                #instanceid = line.strip().split("=")[1]
                if line.startswith("#id="):
                    pass
                elif line.startswith("#text="):
                    pass
            elif len(linearray) == 5:
                linearray = line.split("\t")
                if linearray[-1] == "_" or linearray[-1] == "O":
                    pass
                else:
                    #print(linearray[-1])
                    annotations.append((annotatorid,linearray[0],linearray[-1]))
                    annotationsfromeach[annotatorid]+=1
            else:
                somethingwrong = True


    return annotations
    fin.close()
    #return annotations

def main():
    parser = argparse.ArgumentParser(description="Calculates agreement for a lexical sample project in the TSV format")
    parser.add_argument("folder",   metavar="FILE", help="folder path")
    args = parser.parse_args()



    #folder = "data/lex-ansigt-komplet_2015-09-10_1012/annotation/"
    #folder = "data/lex-blik-komplet_2015-09-10_1012/annotation/"



    annotations = []


    for subdir in os.listdir(args.folder):
        for file in [file for file in os.listdir(os.path.abspath(args.folder+subdir)) if file.endswith(".tsv")]:

            #print(os.path.abspath(folder+subdir+"/"+file))
            fullpath = os.path.abspath(args.folder+subdir+"/"+file)
            annotatorname = file.replace(".tsv","")
            annotations.extend(getannotations(fullpath,annotatorid=annotatorname))

    #print(annotations)
    task = nltk.metrics.agreement.AnnotationTask()
    task.load_array(annotations)
    outname = args.folder.replace("data/","").replace("annotation/","").replace("/","")
    #print(annotations)
    outline = ("\t".join([outname,str(task.alpha()),str(annotationsfromeach)])).replace("Counter(","").replace(")","")
    print(outline)



if __name__ == "__main__":
    main()