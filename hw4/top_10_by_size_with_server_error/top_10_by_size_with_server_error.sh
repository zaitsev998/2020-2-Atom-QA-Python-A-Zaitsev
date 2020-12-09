#!/bin/bash
echo -n > $2
if [ -d $1 ]
  then
    for file in $(find $1 -maxdepth 1 -name "*.log");
      do
          echo $file >> $2
          echo " " >> $2
          cat $file | awk '{print $1, $7, $9, $10}' | grep -w "5[0-2][0-9]" | uniq | sort -k4 -nr | head >> $2
      done
  else
    cat $1 | awk '{print $1, $7, $9, $10}' | grep -w "5[0-2][0-9]" | uniq | sort -k4 -nr | head >> $2
fi