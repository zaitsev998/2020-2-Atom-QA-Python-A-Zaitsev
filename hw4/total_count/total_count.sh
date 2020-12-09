#!/bin/bash
echo -n > $2
if [ -d $1 ]
  then
    for file in $(find $1 -maxdepth 1 -name "*.log");
      do
          echo $file >> $2
          echo " " >> $2
          cat $file | wc -l >> $2
      done
  else
    cat $1 | wc -l >> $2
fi