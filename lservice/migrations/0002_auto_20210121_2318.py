# Generated by Django 3.1.4 on 2021-01-21 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lservice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=20)),
                ('item_image', models.ImageField(blank=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='SubItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_item_name', models.CharField(max_length=20)),
                ('sub_item_image', models.ImageField(blank=True, upload_to='images')),
                ('dry_wash_price', models.IntegerField()),
                ('steam_wash_price', models.IntegerField()),
                ('dry_iron_price', models.IntegerField()),
                ('steam_iron_price', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lservice.item')),
            ],
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]