from fastapi import FastAPI

app = FastAPI()

@app.get('/api/status')
def getStatus():
    return { 'status' : 'operating' }