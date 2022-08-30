import gettext
import os

class UnsupportLang(Exception):
    pass

def isSupportLang(lst, lang):
    for item in lst:
        if lang == item.split('\\')[1]:
            return lang
    return None

while True:
    data = input('Language [es-en]:')
    langs = gettext.find('base', 'locale', all=True, languages=('es', 'en'))
    
    if isSupportLang(langs, data):
        os.environ['LANG'] = data
        t = gettext.translation('base', 'locale')
        _ = t.gettext
        print(_('output message'))
    else:
        raise UnsupportLang('language not found') 