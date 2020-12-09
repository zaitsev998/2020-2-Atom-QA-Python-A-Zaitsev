#!/bin/bash
echo -n > $2
if [ -d $1 ]
  then
    for file in $(find $1 -maxdepth 1 -name "*.log");
      do
          echo $file >> $2
          echo " " >> $2
          cat $file | awk '{print $1, $7, $9}' | grep "4[0-9][0-9]" | sort | uniq -c | sort -nr | head >> $2
      done
  else
    cat $1 | awk '{print $1, $7, $9}' | grep "4[0-9][0-9]" | sort | uniq -c | sort -nr | head >> $2
fi