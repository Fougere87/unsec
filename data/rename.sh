#!/bin/bash

for file in bioinfo*
do
mmv  "$file/*" "$file\_#1"
done
