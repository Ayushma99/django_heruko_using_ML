# Generated by Django 3.0.8 on 2020-07-29 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Myapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='approval',
            old_name='applicantincome',
            new_name='ApplicantIncome',
        ),
        migrations.RenameField(
            model_name='approval',
            old_name='coapplicantincome',
            new_name='CoapplicantIncome',
        ),
        migrations.RenameField(
            model_name='approval',
            old_name='credithistory',
            new_name='Credit_History',
        ),
        migrations.RenameField(
            model_name='approval',
            old_name='dependants',
            new_name='Dependants',
        ),
        migrations.RenameField(
            model_name='approval',
            old_name='graduatededucation',
            new_name='Education',
        ),
        migrations.RenameField(
            model_name='approval',
            old_name='firstname',
            new_name='Firstname',
        ),
        migrations.RenameField(
            model_name='approval',
            old_name='gender',
            new_name='Gender',
        ),
        migrations.RenameField(
            model_name='approval',
            old_name='lastname',
            new_name='Lastname',
        ),
        migrations.RenameField(
            model_name='approval',
            old_name='loanamt',
            new_name='LoanAmount',
        ),
        migrations.RenameField(
            model_name='approval',
            old_name='loanterm',
            new_name='Loan_Amount_Term',
        ),
        migrations.RenameField(
            model_name='approval',
            old_name='married',
            new_name='Married',
        ),
        migrations.RenameField(
            model_name='approval',
            old_name='area',
            new_name='Property_Area',
        ),
        migrations.RenameField(
            model_name='approval',
            old_name='selfemployed',
            new_name='Self_Employed',
        ),
    ]
