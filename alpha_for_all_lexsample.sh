for folder in `ls data`
do
    python projectwiseagreement.py "data/$folder/annotation/"
done