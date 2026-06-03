"""config/settings.py
Generated: 2026-06-03
"""
import os

CANDIDATE_NAME = "Job Seeker"
ALERT_EMAIL    = "mikehuang3334@gmail.com"

GMAIL_SENDER   = os.environ.get("GMAIL_SENDER", "")
GMAIL_APP_PASS = os.environ.get("GMAIL_APP_PASS", "")

INDUSTRIES = [
  "Technology",
  "Financial Services",
  "Consulting"
]

GEOGRAPHIES = [
  "Singapore",
  "Taiwan"
]

ROLE_KEYWORDS = [
  "Management Consulting",
  "Project Management",
  "Stakeholder Management",
  "Financial Services",
  "Digital Transformation",
  "Venture Capital"
]

TARGET_COMPANIES = [
  "Deloitte Consulting",
  "iKala Interactive Media",
  "AngelSchool.VC"
]

SENIORITY_LEVELS = [
  "Senior Manager",
  "Director"
]

WEIGHT_INDUSTRY   = 0.30
WEIGHT_GEOGRAPHY  = 0.25
WEIGHT_ROLE       = 0.30
WEIGHT_COMPANY    = 0.15

MATCH_THRESHOLD    = 60
MAX_JOBS_PER_EMAIL = 20
CRON_SCHEDULE      = "0 0 * * *"
SEEN_JOBS_DB       = "data/seen_jobs.json"
