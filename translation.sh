xgettext -d base -o locale/base.pot main.py appcore/*.py services/*.py

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