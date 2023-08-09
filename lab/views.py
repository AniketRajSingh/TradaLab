from django.shortcuts import render, get_object_or_404
from .models import LabExperiment

def lab_home(request):
    return render(request, 'lab/home.html')

def lab_page(request, standard, subject):
    subject_display = subject
    if standard == 'tenth':
         standard_display = '10th'
    elif standard == 'twelfth':
         standard_display = '12th'
    elif standard == 'engineering':
         standard_display = standard.capitalize()


    context = {'subject': subject_display, 'standard': standard_display}
    experiments = LabExperiment.objects.filter(standard=standard_display, subject=subject_display)
    return render(request, 'lab/lab_page.html', {'experiments': experiments, 'context': context})

def lab_experiment_detail(request, standard, subject, experiment_id):
    context = {'subject': subject, 'standard': standard}
    experiment = get_object_or_404(LabExperiment, id=experiment_id)
    return render(request, 'lab/lab_experiment_detail.html', {'experiment': experiment,'context': context})