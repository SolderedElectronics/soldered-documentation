@echo off
echo Installing IOPaint for Python 3.14 (bypassing Pillow version conflict)...
echo.

REM Step 1: install IOPaint package itself without pulling its pinned Pillow==9.5.0
"C:\Users\borna\AppData\Local\Python\bin\python.exe" -m pip install iopaint --no-deps

REM Step 2: install all remaining IOPaint dependencies (excluding Pillow - already installed)
"C:\Users\borna\AppData\Local\Python\bin\python.exe" -m pip install ^
    torch ^
    "diffusers==0.27.2" ^
    "huggingface-hub==0.25.2" ^
    accelerate ^
    "peft==0.7.1" ^
    "transformers>=4.39.1" ^
    safetensors ^
    "controlnet-aux==0.0.3" ^
    "fastapi==0.108.0" ^
    uvicorn ^
    python-multipart ^
    "python-socketio==5.7.2" ^
    typer ^
    "pydantic>=2.5.2" ^
    rich ^
    loguru ^
    yacs ^
    "piexif==1.1.3" ^
    omegaconf ^
    easydict ^
    "gradio==4.21.0" ^
    "typer-config==1.4.0"

echo.
echo Done! IOPaint is installed.
echo The LaMa model (~200 MB) will download automatically on first use.
pause
