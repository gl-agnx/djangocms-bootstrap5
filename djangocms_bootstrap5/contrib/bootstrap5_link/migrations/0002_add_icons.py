from django.db import migrations, models

import djangocms_icon.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap5_link', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bootstrap5link',
            name='icon_left',
            field=djangocms_icon.fields.Icon(default='', verbose_name='Icon left', blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='bootstrap5link',
            name='icon_right',
            field=djangocms_icon.fields.Icon(default='', verbose_name='Icon right', blank=True, max_length=255),
        ),
    ]
