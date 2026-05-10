from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import StudentProfile, FeeRecord, Batch, Attendance
from django.db.models import Sum
from datetime import date
@login_required
def admin_dashboard(request):
    # Fetch data from DB
    students = StudentProfile.objects.all()
    batches = Batch.objects.all()
    total_fees = FeeRecord.objects.aggregate(Sum('amount_paid'))['amount_paid__sum'] or 0
    # "students" here must match {% for student in students %} in HTML
    context = {
        'students': students,
        'total_students': students.count(),
        'total_batches': batches.count(),
        'total_revenue':total_fees,
        # Get today's attendance count
        'present_today': Attendance.objects.filter(date='2026-05-10', is_present=True).count()
    }
    return render(request, 'students/dashboard.html', context)


def mark_attendance(request):
    students = StudentProfile.objects.all()
    today = date.today()

    if request.method == 'POST':
        # Get the list of student IDs who were checked as present
        present_student_ids = request.POST.getlist('student_ids')
        
        for student in students:
            # Create or Update attendance record for today
            Attendance.objects.update_or_create(
                student=student,
                date=today,
                defaults={'is_present': str(student.id) in present_student_ids}
            )
        return redirect('dashboard') # Go back to dashboard after saving

    return render(request, 'students/mark_attendance.html', {'students': students, 'today': today})
def record_payment(request):
    students = StudentProfile.objects.all()
    
    if request.method == 'POST':
        student_id = request.POST.get('student')
        amount = request.POST.get('amount')
        month = request.POST.get('month')
        
        student = StudentProfile.objects.get(id=student_id)
        
        # Save the Fee Record
        FeeRecord.objects.create(
            student=student,
            amount_paid=amount,
            payment_date=date.today(),
            month_for=month
        )
        return redirect('dashboard')

    return render(request, 'students/record_payment.html', {'students': students})
