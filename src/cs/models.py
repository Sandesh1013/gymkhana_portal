from django.db import models
import datetime
from ckeditor_uploader.fields import RichTextUploadingField


class Team(models.Model):
    TEAM_CHOICES = (
        ('UG', 'UG'),
        ('PG', "PG"),
    )
    YEAR_CHOICES = [(x, x) for x in range(int(datetime.datetime.now().year), 2007, -1)]

    year = models.CharField(max_length=10, choices=YEAR_CHOICES)
    team_type = models.CharField(max_length=4, choices=TEAM_CHOICES)
    members = models.ManyToManyField("oauth.UserProfile")

    def _str_(self):
        return self.team_type + self.year


class CsFaq(models.Model):

    CATEGORY_CHOICES = (
        ('General', 'General'),
        ('Academics', 'Academics'),
        ('Registration', 'Registration'),
        ('Hostel/Mess', 'Hostel/Mess'),
        ('Misc', 'Misc'),
    )
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)
    question = models.TextField()
    answer = RichTextUploadingField(blank=True, null=True)