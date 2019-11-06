#!/bin/bash

REQUIREMENTS="jupyter jupyterlab numpy pandas matplotlib django"
MINICONDA_PATH=~/goinfre/miniconda3

login=$(whoami)
curr_python=$(which python)
mini_path=/Users/$login/goinfre/miniconda3/bin/python
r_reinstall=yes

if [ $DL = yes ] >/dev/null 2>&1
then
	curl -fsSL http://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh > install-python
	exit 0  
fi  

if [ ! $1 ]
then
	echo run the script with miniconda installer as the first argument
	exit 1
fi

if [ $curr_python = $mini_path ]
then
	printf "Python is already installed, do you want to reinstall it ?
[yes|no]> "
	read r_reinstall
	if [ $r_reinstall = "yes" ] 2>/dev/null
	then
		rm -r $MINICONDA_PATH
		echo Python has been removed.
	fi
fi

if [ $r_reinstall = "no" ] 2>/dev/null
then
	echo exit.
	exit 1
fi

if [ $r_reinstall = "yes" ] 2>/dev/null
then
	sh $1 -b -p $MINICONDA_PATH >/dev/null 2>&1
	grep -q "export PATH=/Users/$login/goinfre/miniconda3/bin" ~/.zshrc
	if [ $? = 1 ]
	then
		echo "export PATH=/Users/$login/goinfre/miniconda3/bin:$PATH" >> ~/.zshrc
		source ~/.zshrc 2>/dev/null
	fi
	pip install $(echo $REQUIREMENTS) 1>/dev/null
	echo Python has been installed.
	exec zsh
fi
