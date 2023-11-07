from django.db import models
 
# JOB_TYPE Field
JOB_TYPE=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

# Create your models here.
class Job(models.Model): # Table
    # Fields
    title=models.CharField(max_length=100)
    # location      
    job_type=models.CharField(max_length=15,choices=JOB_TYPE)
    description = models.TextField(max_length=10000)
    # Not Appeared in Admin Dashboard Why? A) auto_now is True that means it records just once
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    # We use Single Quote Because we declared 'Category' Model After Job Model, Then in this case it's not defined So we used Single Quote
    # Python is Interpretted Language
    category = models.ForeignKey('Category', on_delete=models.CASCADE)    
    
    # Table Object
    def __str__(self):      
        return self.title

# Relation Category has Many Jobs, But Job has one Category.
# One-to-Many >>>> Foreign Key
class Category(models.Model):
    # id = models.IntegerField()    
    name = models.CharField(max_length = 25) 
    def __str__(self):  
        return self.name        