import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

try:
    CREDS = Credentials.from_service_account_file('creds.json', scopes=SCOPE)
    GSPREAD_CLIENT = gspread.authorize(CREDS)
    SHEET = GSPREAD_CLIENT.open('analysis country GDP')

    # Perform some operation,like printing the title
    print("Connected to spreadsheet:", SHEET.title)

except gspread.exceptions.APIError as e:
    print("Google Sheets API Error:", str(e))

except Exception as e:
    print("Error:", str(e))




