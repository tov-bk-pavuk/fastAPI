from enum import Enum
from fastapi import FastAPI
import random as rd
import uvicorn
from schemas import Movie

app = FastAPI()


@app.get("/")   # Роутинг находится в кавычках декоратора
                # get является методом функции и может быть POST и прочие
async def root():
    return {"message": "Hello World"}

# uvicorn main:app --reload - команда запуска сервера
# uvicorn - команда
# main - название запускаемого файла
# : - разделитель
# app - название приложения, которое нужно запустить (экземпляр класса FastAPI)
# --reload - этот флаг значит перезагружать автоматически наше приложение при изменении кода
# http://127.0.0.1:8000/docs - автоматическая генерация документации по API

dic = {''.join(rd.choice('kjsdfhwerlkdsf')): i for i in range(10)}





person = 'Vitya'


class EnumModel(str, Enum):
    petya = 'petya'
    vasya = 'vasya'
    kolya = 'kolya'


@app.get('/en/{person}')  # передача пути
async def enums(person: EnumModel):
    if person == EnumModel.petya:
        return {"person": "Petya", "greetings": "Меня зовут Петя"}


@app.get("/borya/{username}")
async def bor(username: str):
    spis = username.split('&')
    dic.update(name=spis)
    return dic


@app.get("/func/")  #
async def func_with_arguments(username: str = 'Name', age: int = 0):
    dic = {'username': username, 'age': age}
    return dic


@app.get("/func_path/user/{pk}/prem/{is_assured}")  #
async def func_path(pk: int = 0, is_assured: bool = False):
    if is_assured == True:
        return root()
    return 'У вас нет доступа'


@app.post('/new_movie/')
async def new_movie(film: Movie):
    return film


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True) #  запускаем сервер прямо из скрипта
