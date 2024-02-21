#!/bin/sh
tidy -q -errors $1
ret=$?
echo $ret
if [ $ret -eq 0 ]; then
  echo "success no errors or warnings"
elif [ $ret -eq 1 ]; then
  echo "warnings exist"
elif [ $ret -eq 2 ]; then
  echo "errors exist"
fi
