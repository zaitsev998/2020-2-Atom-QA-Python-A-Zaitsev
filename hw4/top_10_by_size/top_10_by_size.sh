#!/bin/bash
echo -n > $2
if [ -d $1 ]
  then
    for file in $(find $1 -maxdepth 1 -name "*.log");
      do
          echo $file >> $2
          echo " " >> $2
          cat $file | awk '{print $7, $9, $10}' | uniq -c | sort -k4 -nr | head >> $2
      done
  else
    cat $1 | awk '{print $7, $9, $10}' | uniq -c | sort -k4 -nr | head >> $2
fi