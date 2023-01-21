from fastapi import FastAPI

print("This application is running inside docker")

app = FastAPI()

@app.get("/{id}")
def read_id_api(id):
    return {f"your input id is: {id}"}