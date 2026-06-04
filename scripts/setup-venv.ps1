# MagicSquare_xx — create .venv and install pytest
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

if (-not (Test-Path ".venv")) {
    python -m venv .venv
}

$pipArgs = @(
    "-m", "pip", "install", "-r", "requirements-dev.txt",
    "--trusted-host", "pypi.org",
    "--trusted-host", "pypi.python.org",
    "--trusted-host", "files.pythonhosted.org"
)
& ".venv\Scripts\python.exe" @pipArgs

Write-Host ""
Write-Host "Done. Activate:  .\.venv\Scripts\Activate.ps1"
Write-Host "Run tests:     .\.venv\Scripts\python.exe -m pytest tests/entity/test_d_loc_01.py -v"
