# from django.db import models

# # Create your models here.

  
# # # declare a new model with a name "GeeksModel"
# class ForgotModel(models.Model):
#     Email = models.EmailField()
    
#     def __str__(self):
#         return self.Email


# import the standard Django Model

from django.db import models

# Create your models here.
class ForgotModel(models.Model):
   Email=models.EmailField()
 
   def __str__(self):
        return self.Email



