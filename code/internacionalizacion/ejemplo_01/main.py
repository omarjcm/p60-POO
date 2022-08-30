import gettext
import os

os.environ['LANG'] = 'en'
print(gettext.find('base', 'locale', all=True, languages=('en', 'es')))
t = gettext.translation('base', 'locale')
_ = t.gettext
print(_('output message'))