# Generated by Django 2.0.10 on 2019-02-25 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaperlessVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='文件名')),
                ('type', models.IntegerField(choices=[(5, '政协舟山版'), (1, '人大宁波市版'), (3, '政协宁波版'), (8, '履职宁波人大版'), (11, '智慧人大'), (7, '标准宁波市场监管局版'), (2, '人大宁波辖区版'), (10, '舟山市委'), (9, '履职宁波政协版'), (4, '人大温州平阳版'), (6, '标准宁波经信委版')], default=1, verbose_name='版本类型')),
                ('file_path', models.FileField(upload_to='media', verbose_name='上传文件')),
                ('md5', models.CharField(blank=True, max_length=100, null=True, verbose_name='文件MD5')),
                ('content', models.TextField(max_length=500, verbose_name='版本更新功能')),
                ('version', models.CharField(max_length=100, verbose_name='版本号')),
                ('test_report', models.FileField(blank=True, null=True, upload_to='report', verbose_name='测试报告')),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='二维码')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('datetime_modified', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '无纸化版本',
                'verbose_name_plural': '无纸化版本',
                'permissions': (('view_ad_campaing', 'view_ad_campaing'),),
            },
        ),
        migrations.CreateModel(
            name='TestProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(2, '市政协无纸化测试流程'), (4, '舟山人大无纸化测试流程'), (3, '市辖区人大无纸化测试流程'), (6, '智慧人大测试流程'), (1, '市人大无纸化测试流程'), (5, '舟山市府无纸化测试流程')], default=1, verbose_name='版本类型')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='版本')),
                ('version_code', models.CharField(max_length=20, verbose_name='版本号')),
                ('content', models.CharField(max_length=200, verbose_name='版本更迭新增流程')),
                ('file', models.FileField(upload_to='test_process', verbose_name='流程文件')),
            ],
            options={
                'verbose_name': '测试流程',
                'verbose_name_plural': '测试流程',
            },
        ),
    ]
