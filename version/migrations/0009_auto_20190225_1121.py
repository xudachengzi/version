# Generated by Django 2.0.10 on 2019-02-25 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('version', '0008_auto_20190225_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paperlessversion',
            name='file_path',
            field=models.FileField(upload_to='media', verbose_name='文件'),
        ),
        migrations.AlterField(
            model_name='paperlessversion',
            name='type',
            field=models.IntegerField(choices=[(5, '履职宁波人大版'), (3, '人大温州平阳版'), (8, '政协舟山版'), (7, '政协宁波版'), (6, '履职宁波政协版'), (9, '市委舟山版'), (1, '智慧人大版'), (2, '人大宁波市辖区版'), (10, '标准宁波经信委版'), (4, '人大宁波市版'), (11, '标准宁波市场监管局版')], default=1, verbose_name='版本类型'),
        ),
        migrations.AlterField(
            model_name='testprocess',
            name='type',
            field=models.IntegerField(choices=[(4, '舟山人大无纸化测试流程'), (1, '市人大无纸化测试流程'), (3, '市辖区人大无纸化测试流程'), (6, '智慧人大测试流程'), (5, '舟山市府无纸化测试流程'), (2, '市政协无纸化测试流程')], default=1, verbose_name='版本类型'),
        ),
    ]