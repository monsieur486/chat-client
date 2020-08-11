xgettext -d base -o locale/base.pot main.py appcore/*.py templates/*.py

list_domain='base'

for domain in $list_domain;do
    list_lang='de en es fr it nl pt'
        for lang in $list_lang;do
            FILE=locale/"$domain".pot
            if [ -f "$FILE" ]; then
                FILE2=locale/"$lang"/LC_MESSAGES/"$domain".po
                if [ ! -f "$FILE2" ]; then
                    cp locale/"$domain".pot locale/"$lang"/LC_MESSAGES/"$domain".po
                fi
            fi
            FILE=locale/"$domain".pot
            if [ -f "$FILE" ]; then
                msgmerge --update locale/"$lang"/LC_MESSAGES/"$domain".po locale/"$domain".pot
            fi
            FILE=locale/"$lang"/LC_MESSAGES/"$domain".po
            if [ -f "$FILE" ]; then
                msgfmt -o locale/"$lang"/LC_MESSAGES/"$domain".mo locale/"$lang"/LC_MESSAGES/"$domain".po
            fi
        done
done

if [ "$1" = "C" ] ; then
    rm appSettings.py
    cp appSettings.py.dist appSettings.py
    pyinstaller \
    --log-level=WARN \
    --name luncher \
    --windowed \
    --noconsole \
    --clean \
    --noconfirm \
    main.py
    cp -R public dist/luncher/public
    cp -R locale dist/luncher/locale
    mv dist/luncher/public/settings/luncher.cfg.dist dist/luncher/public/settings/luncher.cfg
    rm -rf build
fi

find . -type d -name "__pycache__" -exec rm -Rf {} \;
find . -type d -name "*.pyc" -exec rm -Rf {} \;

git add .
git commit -m "last stable compilation"
