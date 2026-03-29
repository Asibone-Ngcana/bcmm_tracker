# BCMM Delivery Tracker Prototype

This project is a mobile-first Django prototype created for a university interaction design assignment. It represents a conceptual community service delivery tracking system for the **Buffalo City Metropolitan Municipality (BCMM)**. 

The primary goal of this repository is to demonstrate core interaction design principles, rather than functional data storage or backend architecture, resulting in a minimalistic boilerplate-free Django application.

## Interaction Design Principles Demonstrated

- **Visibility:** The prototype utilizes a clear top navigation bar ("BCMM Delivery Tracker") and immediately displays primary context data (like the current ward and count of active faults) as vibrant text overlays directly on the map interface.
- **Feedback:** Users are given immediate context upon viewing the dashboard, confirming the region and the active number of tracked issues.
- **Affordance:** Physical-world cues are mapped to the digital interface, specifically the large dashed area in the report screen explicitly communicating that the user should "[ Tap to Open Camera ]".
- **Limitations & Constraints:** To prevent user error, the "Submit Report" button is explicitly restricted (disabled/greyed-out) with clear text that states it is awaiting a required photo upload.
- **Automation:** To reduce cognitive load and data entry error, the geographic location input is mocked as a read-only field automatically filled via GPS.

## Project Structure

- `dashboard/`: Contains the logic and mobile-first template for the main map view.
- `reporting/`: Contains the logic and mobile-first template for the smart issue logging screen.

*Note: Unnecessary Django database models, admin interfaces, and unit testing files have been removed to keep the focus purely on human-computer interaction (HCI) concepts.*

## How to Run Locally

You can run this project locally on your machine using Python and Django.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Asibone-Ngcana/bcmm_tracker.git
   cd bcmm_tracker
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   
   # Windows:
   .\venv\Scripts\activate
   
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Django:**
   ```bash
   pip install django
   ```

4. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

5. **View the prototype:**
   Open your browser and navigate to `http://127.0.0.1:8000/` to test the dashboard, and `http://127.0.0.1:8000/report/` for the reporting interface.
