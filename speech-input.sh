#!/bin/bash
LOCK_FILE="speech-input.lock"

if [ -e $LOCK_FILE ]; then
  echo "script is executing...end"
else
  echo $$ > $LOCK_FILE
  
  python speech-input

  rm -f $LOCK_FILE 
fi
