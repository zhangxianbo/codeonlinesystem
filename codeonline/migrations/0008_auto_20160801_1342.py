# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeonline', '0007_auto_20160801_1338'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='onlinerequest',
            options={'permissions': (('production_manager_permission', 'production_manager_permission'), ('develop_manager_permission', 'develop_manager_permission'), ('test_manager_permission', 'test_manager_permission'), ('maintenance_persion_permission', 'maintenance_persion_permission'), ('maintenance_manager_permission', 'maintenance_manager_permission'))},
        ),
    ]
