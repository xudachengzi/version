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
        'md5',
        'datetime_created',
        'datetime_modified']  # 显示字段
    search_fields = ['name', ]  # 搜索框
    list_editable = ['name',
                     'version',
                     'content', ]  # 可编辑字段
    list_filter = ['type',
                   ]  # 过滤器
    date_hierarchy = 'created_time'

    ordering = ('-datetime_created', '-version')  # 以某字段排序
    list_per_page = 10  # 分页
    menu_style = "accordion"  # 使左侧菜单栏为伸缩样式
    site_title = "版本管理"  # 设置标题
    site_footer = "浙江智加"  # 设置底部文字
    # enable_themes = True  # 添加主题选择功能
    # use_bootswatch = True  # 添加多个主题到选择中
    # show_bookmarks = False  # 关闭标签栏

xadmin.site.register(PaperlessVersion, PaperlessVersionAdmin)
