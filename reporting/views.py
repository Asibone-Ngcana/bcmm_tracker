from django.shortcuts import render

def report_fault(request):
    return render(request, 'reporting/report_fault.html')
