import gettext
import os

os.environ['LANG'] = 'es'
t = gettext.translation('base', 'locale')
_ = t.gettext

print(_('GESTIONAR_AGENDA'))
print( '[1].- {} {}.'.format(_('INSERTAR'), _('CONTACTO')))
print( '[2].- {} {}.'.format(_('MODIFICAR'), _('CONTACTO')))
print( '[3].- {} {}.'.format(_('ELIMINAR'), _('CONTACTO')))
print( '[4].- {} {}.'.format(_('BUSCAR'), _('CONTACTO')))
print( '[5].- {} {}.'.format(_('LISTAR'), _('CONTACTO')))
print( '[0].- {}.'.format(_('SALIR')))