from path_parameters_04 import Path, app

"""
This is for String path validation
Assuming you are taking a license plate based on
AB-123-CD, you can use length as a validator or Regex
"""

# Length as a validator
@app.get("/license-plates/{license}")
async def get_license_plate(license: str = Path(..., min_length=9, max_length=9)):
    return {"license": license}


# Regex as a validator
@app.get("/license-plates-re/{license}")
async def get_license_plate_re(license: str = Path(..., regex=r"^\w{2}-\d{3}-\w{2}$")):
    return {"license": license}
