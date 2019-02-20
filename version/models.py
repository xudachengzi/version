from django.db import models


# Create your models here.

class PaperlessVersion(models.Model):
    """
    无纸化版本
    """
    TYPE_CHOICE = {
        (1, "人大宁波市版"),
        (2, "人大宁波辖区版"),
        (3, "政协宁波版"),
        (4, "人大温州平阳版"),
        (5, "政协舟山版"),
        (6, "标准宁波经信委版"),
        (7, "标准宁波市场监管局版"),
        (8, "履职宁波人大版"),
        (9, "履职宁波政协版"),
        (10, "舟山市委"),
        (11, "智慧人大"),
    }
    name = models.CharField(verbose_name="文件名",
                            max_length=100,
                            )
    type = models.IntegerField(verbose_name="版本类型",
                               choices=TYPE_CHOICE,
                               default=1)
    file_path = models.FileField(verbose_name="上传文件",
                                 upload_to='media',
                                 )
    md5 = models.CharField(verbose_name="文件MD5",
                           max_length=100,
                           blank=True, null=True)
    content = models.TextField(verbose_name="版本更新功能",
                               max_length=500,
                               )
    version = models.CharField(verbose_name="版本号",
                               max_length=100,
                               )
    test_report = models.FileField(verbose_name='测试报告',
                                   upload_to='report',
                                   blank=True, null=True)
    qr_code = models.ImageField(verbose_name="二维码",
                                upload_to='img',
                                blank=True, null=True)
    datetime_created = models.DateTimeField(verbose_name="创建时间",
                                            auto_now_add=True)
    datetime_modified = models.DateTimeField(verbose_name="修改时间",
                                             auto_now=True)

    class Meta:
        verbose_name = "无纸化版本"
        verbose_name_plural = "无纸化版本"
        permissions = (
            ('view_ad_campaing', 'view_ad_campaing'),
        )

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.file_path

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        return self.save()


class TestProcess(models.Model):
    """测试流程"""
    TYPE_CHOICE = {
        (1, '市人大无纸化测试流程'),
        (2, '市政协无纸化测试流程'),
        (3, '市辖区人大无纸化测试流程'),
        (4, '舟山人大无纸化测试流程'),
        (5, '舟山市府无纸化测试流程'),
        (6, '智慧人大测试流程'),
    }

    type = models.IntegerField(verbose_name="版本类型",
                               choices=TYPE_CHOICE,
                               default=1)
    name = models.CharField(verbose_name='版本',
                            max_length=100,
                            blank=True, null=True)
    version_code = models.CharField(verbose_name='版本号',
                                    max_length=20
                                    )
    content = models.CharField(verbose_name='版本更迭新增流程',
                               max_length=200)
    file = models.FileField(verbose_name='流程文件',
                            upload_to='test_process')


    class Meta:
        verbose_name = "测试流程"
        verbose_name_plural = "测试流程"

    def __str__(self):
        return self.name

