#!/usr/bin/bash

# pulling
git pull

#####################################
clear

# add all
git status | lolcat
git add .
printf "\n\n"

# commit
git status | lolcat
git commit -m 'autoUpdate by shell script'
printf "\n\n"

# pushing
git status | lolcat
git push
printf "\n\n"
