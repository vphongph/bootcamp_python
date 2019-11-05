MINICONDA_PATH=~/goinfre/miniconda3
export PATH="$MINICONDA_PATH/bin:$PATH"

login=$(whoami)
curr_python=$(which python)
mini_path=/Users/$login/goinfre/miniconda3/bin/python

if [ $DL = yes ] 2>/dev/null
then
	curl -fsSL http://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh > install-python
	exit 0	
fi	

if [ $curr_python = $mini_path ];
then
	printf "Python is already installed, do you want to reinstall it ?
[yes|no]> "
	read r_reinstall
else
	MINICONDA_PATH=~/goinfre/miniconda3
	SCRIPT=Miniconda3-latest-MacOSX-x86_64.sh

	sh $SCRIPT -b -p $MINICONDA_PATH
	rm $SCRIPT

	export PATH="$MINICONDA_PATH/bin:$PATH"
	pip install $REQUIREMENTS
	clear
	echo "Which python:"
	which python
	if grep -q "export PATH=/Users/$login/goinfre/miniconda3/bin" ~/.zshrc
	then
	   echo "export already in .zshrc";
	else
	   echo "adding export to .zshrc ...";
	   echo "export PATH=/Users/$login/goinfre/miniconda3/bin" ~/.zshrc
	fi
	source ~/.zshrc
fi