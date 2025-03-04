from django.db import models
from django.conf import settings

class Audit(models.Model):
    deleted = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')
    createdBy = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='created_by', on_delete=models.CASCADE) 

    class Meta:
        abstract = True

class StateAudit(Audit):
    active = models.BooleanField(default=False)

    class Meta:
        abstract = True

class Client(StateAudit):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = "client"
    
class Project(StateAudit):
    name = models.CharField(max_length=100, unique=True)
    amount = models.FloatField()
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "project"
    
    def get_dates(self):
        return ProjectDate.get_all_project_dates(self.pk)

class ProjectDate(Audit):
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING, related_name="dates")
    day = models.SmallIntegerField()

    class Meta:
        db_table = "projectDate"
    
    @classmethod
    def get_all_project_dates(self, id):
        return self.objects.filter(project_id=id)
    
class Payment(Audit):
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    due_date = models.DateTimeField()
    amount = models.FloatField()
    payed = models.BooleanField(default=False)

    class Meta:
        db_table = "payment"
