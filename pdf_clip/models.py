from django.db import models

# Create your models here.
class File(models.Model):
    fileName = models.CharField(max_length=128)
    positionArray = models.JSONField(null=True, blank=True)
    pages=models.IntegerField()
    maxPageWidth = models.FloatField(default=0)
    maxPageHeight = models.FloatField(default=0)
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}: {self.fileName}"
    
class Clip(models.Model):
    fileId = models.ForeignKey(File, on_delete=models.CASCADE, related_name="relatedFile", default=0)
    pageNumber = models.IntegerField()
    clipNumber = models.IntegerField()
    minY = models.IntegerField()
    maxY = models.IntegerField()
    minX = models.IntegerField(null=True)
    maxX = models.IntegerField(null=True)
    note = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return f"{self.fileId.fileName}, clipNumber: {self.clipNumber}, page: {self.pageNumber}"
    
