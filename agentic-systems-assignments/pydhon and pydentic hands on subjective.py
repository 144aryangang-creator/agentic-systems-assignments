from pydantic import BaseModel, Field, EmailStr, ConfigDict, ValidationError

class Address(BaseModel):
    # city: minimum length 3
    city: str = Field(..., min_length=3)
    
    # pincode: exactly 6 digits
    # Using regex (pattern) ensures it's exactly 6 digits and numeric
    pincode: str = Field(..., min_length=6, max_length=6, pattern=r"^\d{6}$")

class UserRegister(BaseModel):
    # Enable validation on assignment
    model_config = ConfigDict(validate_assignment=True)

    user_id: int
    name: str
    email: EmailStr
    
    # age: must be >= 18
    age: int = Field(..., ge=18)
    
    # Nested Address model
    address: Address
    
    # Optional boolean with default False
    is_premium: bool = False

# --- Testing the System ---

try:
    # 1. Successful Registration
    valid_user = UserRegister(
        user_id=101,
        name="Alice Smith",
        email="alice@example.com",
        age=25,
        address={
            "city": "New York",
            "pincode": "100001"
        }
    )
    print("✅ User created successfully.")

    # 2. Testing Assignment Validation
    print("Attempting to update age to 16...")
    valid_user.age = 16  # This will trigger a ValidationError!

except ValidationError as e:
    print("\n❌ Validation Error Caught:")
    for error in e.errors():
        # Cleanly print where the error happened
        location = " -> ".join(str(loc) for loc in error['loc'])
        print(f"   [{location}]: {error['msg']}")