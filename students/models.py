from django.db import models
from django.contrib.auth.models import User

class Batch(models.Model):
    name = models.CharField(max_length=100)
    timing = models.TimeField()
    subject = models.CharField(max_length=100)
    monthly_fees = models.DecimalField(max_digits=8, decimal_places=2)

    def __clstr__(self):
        return f"{self.name} ({self.subject})"

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=15)
    admission_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.get_full_name()
class Attendance(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.user.username} - {self.date}"

class FeeRecord(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateField()
    month_for = models.CharField(max_length=20)  # e.g., "June 2026"
    transaction_id = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.student.user.first_name} - {self.month_for}"
