from fastapi import FastAPI

print("Running project from inside the docker container")

app = FastAPI()

@app.get("/{id}")
def read_id_api(id):
    return {f"Running app ID is: {id}"}
