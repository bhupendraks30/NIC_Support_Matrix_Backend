from django.db import models
from django.utils import timezone



# add by anil
class User(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    ROLE_CHOICES = [
        (0, 'User'),
        (1, 'Admin'),
    ]
    uid = models.CharField(max_length=15, unique=True, null=False, editable=False)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=8, choices=GENDER_CHOICES)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField(max_length=1000)
    pin_code = models.CharField(max_length=10)
    password = models.CharField(max_length=255)
    
    image = models.ImageField(upload_to='images/profile_Images/', null=True, blank=True)
    role = models.IntegerField(choices=ROLE_CHOICES, default=0)  # Default role set to 0 (User)

    def save(self, *args, **kwargs):
        if not self.uid:
            today = timezone.now().strftime('%y%m%d')
            last_user = User.objects.last()  # Get the last user by creation order
            if last_user:
                last_uid = last_user.uid[-2:]
                new_uid = f'NIC00{today}{int(last_uid) + 1:02}'
            else:
                new_uid = f'NIC00{today}01'
            self.uid = new_uid
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name 
    
    
# add by a


# add by a


# add by a
class AddProject(models.Model):
 
    # uid = models.ForeignKey(User, on_delete=models.CASCADE)
    hod_full_name = models.CharField(max_length=255)
    how_mail = models.EmailField(max_length=100,unique=True)
    hod_contact = models.CharField(max_length=15)
    # hod_image = models.ImageField(upload_to='images/profile_Images/', null=True, blank=True)
    hod_department = models.CharField(max_length=100)
    hod_address = models.TextField(max_length=1000)
    project_tittle = models.CharField(max_length=100)
    project_duration = models.CharField(max_length=100)
    project_budget = models.CharField(max_length=100)
    description = models.TextField(verbose_name='Description')
    date_submitted = models.DateTimeField(auto_now_add=True, verbose_name='Date Submitted')
    status = models.CharField(max_length=50, default='Pending', verbose_name='Status')
     
    class Meta:
        verbose_name = 'AddProject'
        verbose_name_plural = 'AddProject'


# add by a 

# add by a  
    
    
    
    
    
    
    
    
 