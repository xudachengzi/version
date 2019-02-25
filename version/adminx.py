import hashlib
from datetime import time

import qrcode

import xadmin
from .models import PaperlessVersion


class PaperlessVersionAdmin(object):
    list_display = [
        'name',
        'type',
        'version',
        'content',
        'file_path',
        'md5',
        'qr_code',
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
