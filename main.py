import time
import uuid

from collections import defaultdict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class CreateUserRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str

class User(CreateUserRequest):
    id: str

class CreateUserFileRequest(BaseModel):
    contents: str

class File(BaseModel):
    id: str
    created_at: int
    contents: str

# Map user IDs to users.
users = {
  "2b9046ac-6112-11eb-ae07-3e22fb0d93ba": {
    "id": "2b9046ac-6112-11eb-ae07-3e22fb0d93ba",
    "first_name": "Devon",
    "last_name": "Developer",
    "email": "devon@devonthedeveloper.com",

    # Tutorial: Change this to a US-formatted phone number
    #   by removing the leading "+1-".
    "phone": "+1-323-867-5309",
  },
  "38c15834-6112-11eb-86fb-3e22fb0d93ba": {
    "id": "38c15834-6112-11eb-86fb-3e22fb0d93ba",
    "first_name": "Alice",
    "last_name": "Adventurer",
    "email": "alice@adventuring.org",
    "phone": "+1-234-567-8901",
  }
}

# Map user IDs to maps of file IDs to files.
files = defaultdict(dict)

app = FastAPI()

@app.get("/users")
async def get_users():
  return { "users": list(users.values()) }

@app.post("/users")
async def create_user(user_req: CreateUserRequest):
    user = User(
      id=f'{uuid.uuid1()}',
      first_name=user_req.first_name,
      last_name=user_req.last_name,
      email=user_req.email,
      phone=user_req.phone
    )

    users[user.id] = user

    return user

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user": users[user_id]}

@app.get("/users/{user_id}/files")
async def get_user_files(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    user_files = []
    if user_id in files:
        user_files = list(files[user_id].values())

    return {"files": user_files}

@app.post ("/users/{user_id}/files")
async def create_user_file(user_id: str, file_req: CreateUserFileRequest):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    
    f = File(
      id=f'{uuid.uuid1()}',
      created_at=time.time(),
      contents=file_req.contents
    )
    files[user_id][f.id] = f

    return {"id": f.id}

@app.get("/users/{user_id}/files/{file_id}")
async def get_user_file(user_id: str, file_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    if user_id not in files or file_id not in files[user_id]:
        raise HTTPException(status_code=404, detail="File not found")
    return files[user_id][file_id]

# @app.delete("/users/{user_id}/files/{file_id}", status_code=204)
# async def delete_user_file(user_id: str, file_id: str):
#     if user_id not in users:
#         raise HTTPException(status_code=404, detail="User not found")
#     if user_id not in files or file_id not in files[user_id]:
#         raise HTTPException(status_code=404, detail="File not found")
#     del files[user_id][file_id]

