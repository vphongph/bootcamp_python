function set_conda {
    REQUIREMENTS="jupyter jupyterlab numpy pandas matplotlib django psycopg2"

    MINICONDA_PATH=~/goinfre/miniconda3
    export PATH="$MINICONDA_PATH/bin:$PATH"

    login=$(whoami)
    curr_python=$(which python)
    mini_path=/Users/$login/goinfre/miniconda3/bin/python

    if [ $curr_python = $mini_path ];
    then
        echo "good python version :)"
    else
        MINICONDA_PATH=~/goinfre/miniconda3
        SCRIPT=Miniconda3-latest-MacOSX-x86_64.sh

        curl -LO http://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
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

}
