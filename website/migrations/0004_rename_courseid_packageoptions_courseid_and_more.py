# Generated by Django 5.0.2 on 2024-03-06 17:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_packageoptions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='packageoptions',
            old_name='CourseID',
            new_name='courseid',
        ),
        migrations.RenameField(
            model_name='packageoptions',
            old_name='PackageID',
            new_name='packageid',
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('SubscriptionID', models.AutoField(primary_key=True, serialize=False)),
                ('PaymentDate', models.DateField()),
                ('ExpiryDate', models.DateField()),
                ('packageid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.package')),
                ('recordid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.record')),
            ],
        ),
    ]
