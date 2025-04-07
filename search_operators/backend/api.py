import uvicorn
from fastapi import FastAPI
from database.repository import find
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/search")
def search(query:str):
    return find(query) 
    
if __name__ == "__main__":
    uvicorn.run(app, port=8000)