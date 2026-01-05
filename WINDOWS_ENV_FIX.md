# Windows Environment Variable Loading Fix

## Issue
The `activate-env.bat` script was showing comment lines and not properly filtering the `.env` file.

## Solution
The script has been updated to:
1. ✅ Properly skip comment lines (starting with `#`)
2. ✅ Handle spaces around `=` signs
3. ✅ Skip empty lines
4. ✅ Only set variables with actual values (not placeholders)

## Important Note for Batch Files

**Environment variables set in a batch file only persist if:**
- The batch file is **CALLed** (not run directly), OR
- Variables are set **before** any `setlocal` command, OR  
- You use `setx` (writes to registry, slower)

### Recommended Usage

**Option 1: Call the script (Recommended)**
```cmd
call activate-env.bat
```

**Option 2: Use PowerShell version instead**
```powershell
.\activate-env.ps1
```
The PowerShell version handles environment variables better and is recommended for Windows users.

### Alternative: Set Variables Manually

If the batch file doesn't preserve variables, you can set them manually:

```cmd
set GOOGLE_CLOUD_PROJECT=your-project-id
set GOOGLE_CLOUD_LOCATION=us-central1
```

Or edit the `.env` file and source it manually, or use the PowerShell activation script which handles this better.

