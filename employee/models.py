
from django.db import models
from manager.utils import validate_non_empty_list

from myauth.models import CustomUser

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="user_id", blank=True , null = True)
    profile_pic = models.ImageField(upload_to='media/profile_pics/', blank=True, null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    main_interest = models.CharField(max_length=255, blank=True, null=True)
    cpi = models.FloatField(blank=True, null=True)
    university = models.CharField(max_length=255, blank=True, null=True)
    skills_required = models.JSONField(default=list,validators=[validate_non_empty_list])
    experience = models.IntegerField(blank=True,null=True)
    resume = models.FileField(upload_to='media/resumes/', blank=False)
    jobsApplied = models.ManyToManyField('manager.RecruitmentModel', related_name="formsApplied", blank=True)

    def __str__(self):
        return self.name
    
    def get_recruitment(self):
        from manager.models import RecruitmentModel  # 🔥 Lazy Import here
        return RecruitmentModel.objects.all()

class CandidateApplicationModel(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('REJECTED', 'Rejected'),
    ]
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE ,related_name="user")
    recruitment = models.ForeignKey('manager.RecruitmentModel', on_delete=models.CASCADE, related_name="recruitment")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile")
    # apply_date = models.DateField(default=timezone.now().date())
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING',
        null=True,
        blank=True
    )
    def __str__(self):
        return self.user.username + " " + self.recruitment.job_details
