from django.shortcuts import render

def home_map(request):
    context = {
        'active_faults': 15,
        'ward': 'Ward 10'
    }
    return render(request, 'dashboard/home_map.html', context)
