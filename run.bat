@echo off
REM Create virtual environment if it doesn't exist
IF NOT EXIST "venv" (
    python -m venv venv
)

REM Activate the virtual environment
call venv\Scripts\activate

REM Install required packages
pip install --upgrade pip
pip install -r requirements.txt

REM Run the Streamlit app
python -m streamlit run app.py

REM Keep the window open
pause