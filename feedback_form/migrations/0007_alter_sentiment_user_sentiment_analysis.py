# Generated by Django 4.2.1 on 2023-05-22 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback_form', '0006_sentiment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentiment',
            name='user_sentiment_analysis',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
