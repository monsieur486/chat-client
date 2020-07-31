clear
if [ "$1" = "D" ] ; then
    rm appSettings.py
    cp appSettings.py.dist appSettings.py
    python main.py
fi

if [ "$1" = "L" ] ; then
    rm appSettings.py
    cp appSettings.py.local appSettings.py
    python main.py
fi
