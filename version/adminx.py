from __future__ import absolute_import
from xadmin import views
import xadmin
from .models import PaperlessVersion


class BaseSetting(object):
    enable_themes = True  # 启用主题管理器
    use_bootswatch = True  # 使用主题
    # show_bookmarks = False  # 关闭标签栏


class GlobalSetting(object):
    site_title = '版本管理'  # 设置后台顶部标题
    site_footer = '浙江智加'  # 设置后台底部标题
    menu_style = "accordion"  # 使左侧菜单栏为伸缩样式


class PaperlessVersionAdmin(object):
    model_icon = 'fa fa-home'  # 设置样式
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


xadmin.site.register(views.BaseAdminView, BaseSetting)  # 注册主题设置
xadmin.site.register(views.CommAdminView, GlobalSetting)

xadmin.site.register(PaperlessVersion, PaperlessVersionAdmin)
