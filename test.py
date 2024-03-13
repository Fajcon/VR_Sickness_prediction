from fastapi import FastAPI

app = FastAPI()


@app.get("/test/{seconds}")
async def test(seconds: int):
    return {"seconds": seconds}


@app.post("/vr_sickness/")
async def save_param():
    return "OK"
