#!/bin/zsh

fileCounter=0

files=(raw_data/*.csv)

newDir=latest_data
mkdir -p "$newDir"

rm latest_data/*

for ((i=0; i<${#files[@]}; i++))
do
	if [[ ${files[$i]} != '.DS_Store' ]]
	then
		cp "${files[$i]}" "${newDir}/week${fileCounter}.csv"	
		fileCounter=$((fileCounter+1)) 
	fi
done
