# Snowflake Guide

## Current Project Structure

```
Snowflake_Guide/
├── connection.py      # Snowflake connection management
├── lambda_function.py # Main application logic
├── .env              # Environment configuration
└── README.md         # Project documentation
```

## Installation

### Prerequisites
- Python 3.7+
- Virtual environment (venv)

### Setup
1. **Activate virtual environment:**
   ```powershell
   # PowerShell
   .\venv\Scripts\Activate.ps1
   
   # Command Prompt
   venv\Scripts\activate.bat
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Update the `.env` file with your Snowflake credentials:
   - `SNOWSQL_USER`: Snowflake username
   - `SNOWSQL_PWD`: Snowflake password
   - `SNOWFLAKE_ACCOUNT`: Snowflake account identifier
   - `WAREHOUSE`: Warehouse name
   - `DATABASE`: Database name
   - `SCHEMA`: Schema name

## Usage

### Testing Connection
```powershell
# From D:\Snowflake directory:
.\venv\Scripts\Activate.ps1
cd Snowflake_Guide
python test_connection.py
```

### Project Structure
- `connection.py`: Handles Snowflake connection establishment
- `lambda_function.py`: Contains main application logic
- `test_connection.py`: Connection testing utility

## Recent Changes

- Initial project setup with connection management
- Added environment variable configuration
- Created basic Lambda function structure