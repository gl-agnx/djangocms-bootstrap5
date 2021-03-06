from django.db import migrations, models

from ..constants import CAROUSEL_ASPECT_RATIO_CHOICES


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap5_carousel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bootstrap5carousel',
            name='carousel_aspect_ratio',
            field=models.CharField(default='', max_length=255, help_text='Determines width and height of the image according to the selected ratio.', verbose_name='Aspect ratio', choices=CAROUSEL_ASPECT_RATIO_CHOICES, blank=True),
        ),
    ]
