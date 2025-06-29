# Snowflake Guide

## Current Project Structure

```
snowflake/
├── connection.py      # Snowflake connection management
├── cortex_functions.py # Snowflake Cortex AI functions
├── test_connection.py # Connection and Cortex testing
├── lambda_function.py # Main application logic
├── .env              # Environment configuration
├── requirements.txt   # Python dependencies
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

### Testing Connection & Cortex Functions
```powershell
# From D:\Snowflake directory:
.\venv\Scripts\Activate.ps1
cd snowflake
python test_connection.py
```

### Project Structure
- `connection.py`: Handles Snowflake connection establishment
- `cortex_functions.py`: Snowflake Cortex AI function implementations
- `test_connection.py`: Connection and Cortex function testing utility
- `lambda_function.py`: Contains main application logic

## Snowflake Cortex Functions

### Available Operations
- **complete**: Text completion using AI models
- **summarize**: Text summarization
- **sentiment**: Sentiment analysis

### Usage Example
```python
from cortex_functions import CORTEX_OPERATIONS

result = CORTEX_OPERATIONS['complete']('What is AI?')
print(result)
```

## Recent Changes

- Added Snowflake Cortex AI function support (complete, summarize, sentiment)
- Created modular cortex_functions.py with dynamic operations
- Enhanced test_connection.py to test Cortex functions
