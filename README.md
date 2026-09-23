# Ethical Phishing Simulation Platform

> **AUTHORIZED SECURITY AWARENESS SIMULATION**

A small web-based cybersecurity project designed to demonstrate an ethical phishing awareness simulation in a controlled local environment.

The Ethical Phishing Simulation Platform is a Flask-based web application developed for security awareness training and educational purposes.

The platform simulates a phishing awareness campaign without sending emails to real external users or collecting real credentials. It provides a controlled workflow where a fictional test recipient interacts with a simulated security awareness message, completes training, and the resulting activities are displayed through an analytics dashboard.

## 2. Objective

The main objective of this project is to create a safe and controlled platform for demonstrating phishing awareness simulations for educational and cybersecurity training purposes.

The application demonstrates:

- Phishing awareness concepts
- Campaign management
- Simulated email interaction
- Security awareness training
- Event tracking
- Basic analytics
- Ethical and controlled simulation practices

## 3. Key Features

### Security Awareness Dashboard

Displays an overview of the simulation environment and basic activity metrics.

### Campaign Management

Allows the user to create and view authorized security awareness simulation campaigns.

### Test Recipients

Uses fictional test recipients for the simulation instead of real external users.

Example:

Name: Rafay Test  
Email: rafay@example.test

### Simulated Email

Displays a fictional security awareness email inside the local application.

### Training Page

Provides educational information about common phishing indicators and safe browsing practices.

### Education Module

Explains how users can identify suspicious messages and avoid unsafe interactions.

### Event Tracking

Records important simulation activities such as:

- EMAIL_SENT
- TRAINING_PAGE_VISITED
- LINK_CLICKED
- TRAINING_INTERACTION
- CAMPAIGN_COMPLETED

### Analytics Dashboard

Displays simulation metrics including:

- Emails Simulated
- Emails Opened
- Links Clicked
- Training Interactions
- Open Rate
- Click Rate
- Training Completion Rate

## 4. Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Application programming |
| Flask | Web application framework |
| HTML5 | Page structure |
| CSS3 | User interface and styling |
| SQLite | Local database |
| Jinja2 | Flask template rendering |
| Git | Version control |
| GitHub | Source code hosting |

## 5. Project Structure

```text
ethical-phishing-simulation/
│
├── app.py
├── database.py
├── requirements.txt
├── README.md
├── .gitignore
├── phishing_simulation.db
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── campaigns.html
│   ├── create_campaign.html
│   ├── recipients.html
│   ├── send_simulation.html
│   ├── simulated_email.html
│   ├── simulation.html
│   ├── education.html
│   └── analytics.html
│
├── static/
│   └── style.css
│
└── screenshots/
```

## 6. Installation

### Step 1: Install Python

Install Python on Windows and make sure Python is available from Command Prompt.

Check the installation:

```text
python --version
```

### Step 2: Open the Project Folder

Open Command Prompt and navigate to the project folder:

```text
cd path\to\ethical-phishing-simulation
```

### Step 3: Create a Virtual Environment

Run:

```text
python -m venv venv
```

### Step 4: Activate the Virtual Environment

On Windows Command Prompt:

```text
venv\Scripts\activate
```

After activation, the command prompt should show:

```text
(venv)
```

### Step 5: Install Dependencies

Run:

```text
pip install -r requirements.txt
```

## 7. Running the Application

Start the Flask application:

```text
python app.py
```

The application will run locally.

Open a web browser and visit:

```text
http://127.0.0.1:5000
```

The application should display the Ethical Phishing Simulation Platform dashboard.

## 8. Application Workflow

The complete demonstration workflow is:

```text
Start Flask Application
        ↓
Open Dashboard
        ↓
Create Campaign
        ↓
Select Fictional Test Recipient
        ↓
Send Simulation
        ↓
View Simulated Email
        ↓
Review Training Message
        ↓
Open Training Page
        ↓
Complete Training Interaction
        ↓
Finish Simulation
        ↓
View Analytics
```

This workflow demonstrates the complete security awareness simulation process in a controlled local environment.

## 9. Database

The application uses **SQLite** for local data storage.

The database contains three main tables.

### Campaigns Table

Stores campaign information:

```text
id
name
description
status
created_at
```

### Recipients Table

Stores fictional test recipient information:

```text
id
name
email
```

### Events Table

Stores simulation activities:

```text
id
campaign_id
recipient_id
event_type
timestamp
```

## 10. Simulation Events

The application records the following events:

### EMAIL_SENT

Records when a simulation is launched for a test recipient.

### TRAINING_PAGE_VISITED

Records the first visit to the training page for the simulation.

### LINK_CLICKED

Records when the simulated email training link is selected.

### TRAINING_INTERACTION

Records completion of the training interaction.

### CAMPAIGN_COMPLETED

Records completion of the simulation workflow.

## 11. Analytics

The Analytics page displays measurable results from the authorized simulation.

### Emails Simulated

Total number of simulated emails recorded.

### Emails Opened

Number of training page visits recorded.

### Links Clicked

Number of simulated link interactions recorded.

### Training Interactions

Number of completed training interactions recorded.

### Open Rate

```text
Open Rate = Emails Opened / Emails Simulated × 100
```

### Click Rate

```text
Click Rate = Links Clicked / Emails Simulated × 100
```

### Training Completion Rate

```text
Training Completion Rate =
Campaigns Completed / Emails Simulated × 100
```

All analytics shown by this project are **simulation metrics only**.

They do not represent real-world phishing statistics.

## 12. Security and Ethical Controls

This project is designed as a controlled cybersecurity education demonstration.

The following safety controls are used:

- Local educational environment
- Fictional test recipient
- No real external email delivery
- No password collection
- No credential collection
- No banking or payment information
- No sensitive personal information
- Parameterized SQL queries
- Basic input validation
- Restricted event types
- Clear authorization warnings

The application clearly displays:

```text
AUTHORIZED SECURITY AWARENESS SIMULATION
```

## 13. Example Test Recipient

The project uses a fictional recipient for demonstration:

```text
Name: Rafay Test
Email: rafay@example.test
```

The recipient is intended only for controlled testing.

## 14. Example Campaign

Example campaign used during testing:

```text
Campaign Name:
Security Awareness Test

Description:
Authorized educational phishing simulation for security awareness training.
```

## 15. User Education

The education module focuses on recognizing common phishing indicators.

Users are encouraged to:

- Verify the sender's email address.
- Be careful with unexpected messages.
- Check links before clicking.
- Be cautious of urgent or suspicious requests.
- Never provide passwords through suspicious messages.
- Verify unusual requests through an official channel.

The main awareness principle is:

```text
Stop, Check, and Verify Before Clicking.
```

## 16. Ethical Use

This project is intended strictly for:

- Cybersecurity education
- Security awareness training
- Authorized demonstrations
- Controlled laboratory environments
- Academic projects

It must not be used to:

- Target real people without authorization
- Send unauthorized phishing messages
- Collect real credentials
- Collect passwords
- Impersonate real organizations
- Conduct fraudulent activities
- Send malicious content

## 17. Limitations

This is a small educational prototype and not a production phishing simulation system.

Current limitations include:

- Local simulation only
- Single fictional test recipient
- Basic campaign management
- Basic analytics
- No real email delivery
- No advanced authentication system
- No large-scale campaign management
- No production deployment configuration

## 18. Future Improvements

Possible future improvements include:

- Mailpit integration for local SMTP testing
- Multiple fictional test recipients
- Campaign-specific analytics
- Improved event deduplication
- CSRF protection
- User authentication
- Exportable analytics reports
- Additional training modules
- More detailed analytics visualization
- Improved database relationships and reporting

## 19. Screenshots

Project screenshots are stored in:

```text
screenshots/
```

Recommended screenshots include:

1. Dashboard
2. Campaigns
3. Create Campaign
4. Test Recipients
5. Send Simulation
6. Simulated Email
7. Security Awareness Training
8. Education
9. Analytics

## 20. GitHub

The project can be maintained using Git and uploaded to GitHub for version control and academic submission.

Basic Git commands:

```text
git init
git add .
git commit -m "Initial project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

Replace:

```text
YOUR_GITHUB_REPOSITORY_URL
```

with the URL of your GitHub repository.

## 21. Conclusion

The Ethical Phishing Simulation Platform demonstrates how a phishing awareness exercise can be implemented safely in a controlled environment.

The project combines Flask, SQLite, HTML, and CSS to provide campaign management, simulated email interaction, security awareness training, event tracking, and analytics.

The platform focuses on education and awareness while avoiding the collection of real credentials or sensitive information.

## 22. Project Status

```text
Project Type: Cybersecurity Mini Project
Purpose: Security Awareness Training
Environment: Local Educational Environment
Framework: Flask
Database: SQLite
Email Delivery: Simulated / Local Only
Recipient Type: Fictional Test Recipient
```

> **AUTHORIZED SECURITY AWARENESS SIMULATION**
>
> **No real passwords or sensitive information are collected.**