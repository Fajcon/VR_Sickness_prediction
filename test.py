from fastapi import FastAPI, Form
from pydantic import BaseModel
from csv import writer
app = FastAPI()


class VRSicknessInfo(BaseModel):
    timestamp: int
    in_game_second: int
    id: str


def save_info_to_file(vr_sickness_info: VRSicknessInfo):
    line = [vr_sickness_info.timestamp, vr_sickness_info.in_game_second]
    with open(vr_sickness_info.id + '.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(line)
        f_object.close()

@app.get("/test/{test}")
async def test(test: int):
    return {"seconds": test}


@app.post("/vr_sickness")
async def save_param(vr_sickness_info: VRSicknessInfo):
    print(vr_sickness_info)
    save_info_to_file(vr_sickness_info)
    return vr_sickness_info