@echo off
echo Installing core dependencies...
pip install rawpy numpy opencv-python Pillow tifffile

echo.
echo Installing IOPaint (AI dust removal - LaMa model)...
pip install iopaint

echo.
echo Done! Run main.py to start the app.
echo Note: IOPaint will download the LaMa model (~200 MB) on first use.
pause
