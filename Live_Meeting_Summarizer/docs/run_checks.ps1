$ErrorActionPreference = "Stop"

Write-Host "[1/3] Running compile check..."
python docs/health_check.py

Write-Host "[2/3] Running unit tests..."
python -m unittest discover -s tests -p "test_*.py" -v

Write-Host "[3/3] Validation complete."
