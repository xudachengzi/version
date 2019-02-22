import xadmin
from .models import PaperlessVersion


class PaperlessVersionAdmin(object):
    list_display = [
        'name',
        'type',
        'file_path',
        'md5',
        'content',
        'qr_code',
        'version',
        'datetime_created',
        'datetime_modified']
    search_fields = ['name', ]
    list_editable = ['name',
                     'type',
                     'file_path', ]
    list_filter = ['name',
                   'type',
                   'file_path',
                   'content',
                   ]


xadmin.site.register(PaperlessVersion, PaperlessVersionAdmin)
