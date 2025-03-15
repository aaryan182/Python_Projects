# Pydantic enforces type validation like Typescript

from pydantic import BaseModel

# Define a data model

class User(BaseModel):
    name: str
    age: int  # Ensures age is an integer
    
# Valid data
user = User(name="Aaryan", age = 22)
print(user)

