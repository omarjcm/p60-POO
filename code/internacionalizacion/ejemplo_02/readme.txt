Primer paso: Creacion de los archivos
> xgettext -o base.pot main.py

Segundo paso: Creacion de los directorios
> mkdir "locale/en/LC_MESSAGES" "locale/es/LC_MESSAGES"

Tercer paso: 
> cp base.pot locale\en\LC_MESSAGES\base.po
> cp base.pot locale\es\LC_MESSAGES\base.po

Cuarto paso:
> msgfmt locale\en\LC_MESSAGES\base.po -o locale\en\LC_MESSAGES\base.mo
> msgfmt locale\es\LC_MESSAGES\base.po -o locale\es\LC_MESSAGES\base.mo

Quinto paso:
> python main.py 
