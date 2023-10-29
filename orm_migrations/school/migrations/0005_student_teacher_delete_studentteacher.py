# Generated by Django 4.2.6 on 2023-10-29 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_remove_student_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(related_name='students', to='school.teacher'),
        ),
        migrations.DeleteModel(
            name='StudentTeacher',
        ),
    ]
