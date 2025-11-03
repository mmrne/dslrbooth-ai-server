from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/newphoto")
async def new_photo(request: Request):
    data = await request.json()
    photo_url = data.get("photo_url")
    template_name = data.get("template_name")
    # tady bude logika pro AI swap
    print(f"Foto: {photo_url}, Šablona: {template_name}")
    return {"status": "received"}

