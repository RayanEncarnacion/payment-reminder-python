from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

class Audit(models.Model):
    deleted = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True, db_column="created_at")
    createdBy = models.ForeignKey(User, null=True, db_column="created_by", on_delete=models.SET_NULL) 

    class Meta:
        abstract = True

class StateAudit(Audit):
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Client(StateAudit):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = "client"
    
class Project(StateAudit):
    name = models.CharField(max_length=100, unique=True)
    amount = models.FloatField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    def get_dates(self):
        return ProjectDate.get_all_project_dates(self.pk)
    class Meta:
        db_table = "project"

class ProjectDate(Audit):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="dates")
    day = models.SmallIntegerField()
    
    def __str__(self):
        return f"{self.project.name}, day {self.day}"

    @classmethod
    def get_all_project_dates(self, id):
        return self.objects.filter(project_id=id)
    
    class Meta:
        db_table = "projectDate"
   
class Payment(Audit):
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    due_date = models.DateTimeField()
    amount = models.FloatField()
    payed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.project.name}: {datetime.strptime(self.due_date, "%Y-%m-%d %H:%M:%S")}"

    class Meta:
        db_table = "payment"
