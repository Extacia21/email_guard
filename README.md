# Email Guard

A Python Flask-based email open tracking and scam detection microservice with a lightweight dashboard.

## Overview

Email Guard helps you track email opens by embedding invisible tracking pixels in your emails. When a recipient opens an email, a request is sent to the Flask app, which logs the event in a SQLite database. You can then view email open activity through a simple, styled web dashboard.

## Features

- Track email opens via unique tracking pixels  
- Log open events with timestamp and email ID  
- Simple web dashboard to view the latest 50 email opens  
- SQLite backend for easy setup and portability  
- Lightweight and easy to integrate as a microservice  
- Ready for extension with scam detection and verification features  

## Getting Started

### Prerequisites

- Python 3.8+  
- [Flask](https://flask.palletsprojects.com/)  
- SQLite (comes bundled with Python)

### Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/your-username/email-guard.git
   cd email-guard
2. Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/macOS

3. Install dependencies:
   
pip install flask

4. Add a 1x1 transparent pixel image named pixel.png inside the project root.
   
##Running the App
python -m flask --app email_guard.tracker:create_app run
Access the dashboard at http://127.0.0.1:5000/

##Use the tracking pixel URL in emails:
http://127.0.0.1:5000/track_open?email_id=unique_email_id

##Usage
Embed the tracking pixel in your email HTML body like this:
<img src="http://your-domain-or-ngrok-url/track_open?email_id=recipient_unique_id" style="display:none;" alt="" />

##How It Works
The /track_open endpoint serves a 1x1 pixel image.

When the recipient opens the email, the image is requested and the email ID and timestamp are saved in the database.

The / endpoint shows a styled dashboard listing recent email opens.

##Future Enhancements
-Add scam detection for incoming/outgoing emails

-Support email delivery verification

-User authentication and secure dashboard access

-Pagination, filtering, and export options on dashboard

-Integrate with email sending scripts for automation

License
MIT License © 2025 Extech

##Contact
For questions or contributions, please open an issue or contact [extaciafakero@gmail.com].
Would you like me to help generate a full `.gitignore` or CI/CD config next?
