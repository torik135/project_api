from django.db import models

class TechChoices(models.Model):
  tech_name = models.CharField(max_length=15, unique=True)
  tech_desc = models.TextField(null=True, blank=True)
  tech_slug = models.SlugField(max_length=15, primary_key=True, unique=True)

  def __str__(self):
    return self.tech_name


class ProjectList(models.Model):
  project_types = [
    ('FE', 'Front End'),
    ('BE', 'Back End'),
    ('FS', 'Full Stack'),
    ('PL', 'Plain / Native'),
  ]

  # project desc
  project_name = models.CharField(max_length=50, null=True, blank=True)
  author = models.CharField(max_length=50, default='torik135')
  project_desc = models.TextField(null=True, blank=True)
  project_img = models.URLField(max_length=255, null=True, blank=True)
  slug = models.SlugField(max_length=50, unique=True, null=True)

  # project link
  code = models.URLField(max_length=250, null=True, blank=True)
  web_link = models.URLField(null=True, blank=True)

  # tech
  tech = models.ManyToManyField(TechChoices)
  project_type = models.CharField(max_length=150, choices=project_types, null=True, blank=True)

  def __str__(self):
    return "Project {} by {}".format(self.project_name, self.author)




