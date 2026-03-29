# BCMM Delivery Tracker

A mobile-first Django prototype for logging and tracking community service delivery issues in the Buffalo City Metropolitan Municipality (BCMM).

## Overview
This project was built for a university interaction design assignment. It focuses purely on demonstrating key UI/UX concepts rather than functioning as a complete backend system with a working database.

## Design Highlights
- **Dashboard**: Shows active faults and the current ward overlay right on the map (Visibility & Feedback).
- **Fault Reporting**: Uses a large, clickable camera prompt for easy access on mobile (Affordance).
- **Auto-filled GPS**: Location fields are locked and pre-filled to prevent manual entry errors (Automation).
- **Form Validation**: The submit button stays disabled until required actions, like a photo upload, are simulated (Constraints).

## How to Run 

1. Clone the repo:
   ```bash
   git clone https://github.com/Asibone-Ngcana/bcmm_tracker.git
   cd bcmm_tracker
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. Install Django:
   ```bash
   pip install django
   ```

4. Start the server:
   ```bash
   python manage.py runserver
   ```

5. Open your browser and go to `http://127.0.0.1:8000/`.
