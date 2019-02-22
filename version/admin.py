from django.contrib import admin

from PaperlessVersion.settings import BASE_DIR
from .models import PaperlessVersion, TestProcess
import hashlib
import qrcode
import time
import image


# admin.site.register(PaperlessVersion)


@admin.register(PaperlessVersion)
class PaperlessVersionAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'type',
                    'version',
                    'md5',
                    'qr_code',
                    'test_report',
                    'content',
                    'datetime_modified',
                    )

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-type',
                '-datetime_created',)

    # list_editable = [
    #                  'version']
    search_fields = (u'name',)

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(PaperlessVersionAdmin, self).get_search_results(request, queryset, search_term)
        try:
            search_term_as_int = int(search_term)
            queryset = (self.model.objects.filter(name=search_term_as_int))
        except:
            pass
        return queryset, use_distinct

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        with open(obj.file_path.path, 'rb') as fp:
            f_md5 = hashlib.md5(fp.read()).hexdigest()
            obj.md5 = f_md5
        create_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        path1 = '192.168.0.138:8999' + '/files/' + str(obj.file_path)
        path2 = 'files/img/' + create_time + '.png'
        img = qrcode.make(path1)
        with open(path2, 'wb') as fp:
            img.save(fp)
        obj.qr_code = '/img/' + create_time + '.png'
        obj.save()


@admin.register(TestProcess)
class TestProcessAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'version_code',
        'content',
        'file',
    )
