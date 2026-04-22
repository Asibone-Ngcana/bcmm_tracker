from django.shortcuts import render

def report_fault(request):
    return render(request, 'reporting/report_fault.html')


def track_report(request, ref_id):
    category = request.GET.get('cat', 'Electricity & Streetlights')
    location = request.GET.get('loc', 'Dorchester Heights, East London')

    category_stripped = category.strip()
    category_key = category_stripped.lower().split(' ')[0]

    category_map = {
        'electricity': 'Electricity & Streetlights',
        'water':       'Water Leaks & Outages',
        'roads':       'Potholes & Roads',
        'power':       'Electricity & Streetlights',
    }

    display_category = category_map.get(
        category_key,
        category_map.get(category_stripped.lower(), category_stripped)
    )

    context = {
        'ref_id':      ref_id,
        'status':      'In Progress',
        'category':    display_category,
        'location':    location,
        'reported_on': 'Oct 24, 2023 at 14:30',
        'assigned_to': 'Team B (Ward 10 Overhead Lines)',
    }
    return render(request, 'reporting/track_report.html', context)
