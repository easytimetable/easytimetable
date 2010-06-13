#! /bin/bash
pwd=`pwd`
for t in *;
do
    if [[ -d "$t" ]];then
        cd $t && make latex && cd _build/latex && make all-pdf 
        cd $pwd
        mv $t/_build/latex/$t.pdf .
    fi
done
