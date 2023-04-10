# fastapi--postgresql

*Activating the Python virtual environment - command for execution
   ".\venv\Scripts\activate" 

*Incase of errors while activating the Python virtual environment - command for execution
   "Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser"

*Executing the code - command for execution
   "uvicorn main:app --reload"

  ^^In case of error such as "Error loading ASGI app. Could not import module main.py"^^
  Following are the commands -
   "cd .\app\"
   "uvicorn main:app --reload"

*API will be created which can be tested on postman website 