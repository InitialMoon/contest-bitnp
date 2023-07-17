# Generated by Django 4.2.3 on 2023-07-14 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0009_remove_response_score_squashed_0010_remove_student_final_score"),
    ]

    operations = [
        migrations.AlterField(
            model_name="answer",
            name="choice",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="quiz.choice",
                verbose_name="所选选项",
            ),
        ),
        migrations.AlterField(
            model_name="draftanswer",
            name="response",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="answer_set",
                to="quiz.draftresponse",
                verbose_name="答卷",
            ),
        ),
        migrations.AlterField(
            model_name="draftresponse",
            name="student",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="draft_response",
                to="quiz.student",
                verbose_name="作答者",
            ),
        ),
    ]
