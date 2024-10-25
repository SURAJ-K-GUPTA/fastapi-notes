import uvicorn
from fastapi import FastAPI

# Create FastAPI app instance
app = FastAPI()
if __name__ == "__main__":
  uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)