# Generated by Django 4.0.4 on 2022-05-22 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerMinor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_minor', models.TextField()),
                ('create_date_minor', models.DateTimeField()),
                ('modify_date_minor', models.DateTimeField(blank=True, null=True)),
                ('author_minor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_answer_minor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionMinor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_minor', models.CharField(max_length=200)),
                ('content_minor', models.TextField()),
                ('create_date_minor', models.DateTimeField()),
                ('modify_date_minor', models.DateTimeField(blank=True, null=True)),
                ('author_minor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_question_minor', to=settings.AUTH_USER_MODEL)),
                ('voter_minor', models.ManyToManyField(related_name='voter_question_minor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentMinor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_minor', models.TextField()),
                ('create_date_minor', models.DateTimeField()),
                ('modify_date_minor', models.DateTimeField(blank=True, null=True)),
                ('answer_minor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='minorboard.answerminor')),
                ('author_minor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('question_minor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='minorboard.questionminor')),
            ],
        ),
        migrations.AddField(
            model_name='answerminor',
            name='question_minor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minorboard.questionminor'),
        ),
        migrations.AddField(
            model_name='answerminor',
            name='voter_minor',
            field=models.ManyToManyField(related_name='voter_answer_minor', to=settings.AUTH_USER_MODEL),
        ),
    ]
