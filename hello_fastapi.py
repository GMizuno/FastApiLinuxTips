from fastapi import FastAPI
from datetime import datetime
from enum import Enum

class ListOption(str, Enum):
    user = 'user'
    department = 'department'
    account = 'account'

app = FastAPI()

@app.get("/")
async def hello():
    return {"message": "Hello World"}

# Rota mais especifica vem antes
@app.get("/user/list")
async def user_list():
    return {"users": ['daniel', 'rodolfo', 'mizuno', 'patati', 'patata']}

@app.get("/user/{username}")
async def user_profile(username: str):
    return {"date": datetime.now(), "user": username}

@app.get("/{list_option}/list")
async def generic_list(list_option: ListOption):
    if list_option == ListOption.user:
        return {"users": ['daniel', 'rodolfo', 'mizuno', 'patati', 'patata']}
    elif list_option == ListOption.department:
        return {"dp": ['sales', 'it', 'data']}
    elif list_option == ListOption.account:
        return {"account": [1, 2, 3]}

@app.get("/account/{number}")
async def account_detail(number: int):
    return {"account": number}

@app.get("/import/{file_path:path}") # Passar paths na url arquivos/las/teste.csv
async def import_file(file_path: str):
    return {"importing": file_path}