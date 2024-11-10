from fastapi import FastAPI
import crud
import schema
from constants import STATUS_SUCCESS
from dependencies import SessionDependency
from lifespan import lifespan
from models import Advertisement

app = FastAPI(
    title="Advertisement Service",
    version="0.0.1",
    description="This project is about buying/selling advertisements.",
    lifespan=lifespan,
)


@app.post("/advertisement", response_model=schema.CreateAdvertisementResponse)
async def create_advertisement(advertisement: schema.CreateAdvertisementRequest, session: SessionDependency):
    ad = Advertisement(**advertisement.dict())
    ad = await crud.add_advertisement(session, ad)
    return {"id": ad.id}


@app.patch("/advertisement/{advertisement_id}", response_model=schema.CreateAdvertisementResponse)
async def update_advertisement(advertisement_id: int, advertisement: schema.UpdateAdvertisementRequest,
                               session: SessionDependency):
    ad = await crud.get_advertisement(session, advertisement_id)
    for key, value in advertisement.dict(exclude_unset=True).items():
        setattr(ad, key, value)
    await crud.update_advertisement(session, ad)
    return {"id": ad.id}


@app.delete("/advertisement/{advertisement_id}")
async def delete_advertisement(advertisement_id: int, session: SessionDependency):
    await crud.delete_advertisement(session, advertisement_id)
    return STATUS_SUCCESS


@app.get("/advertisement/{advertisement_id}", response_model=schema.GetAdvertisementResponse)
async def get_advertisement(advertisement_id: int, session: SessionDependency):
    ad = await crud.get_advertisement(session, advertisement_id)
    return ad.dict


@app.get("/advertisement", response_model=schema.SearchAdvertisementResponse)
async def search_advertisement(session: SessionDependency, title: str = None):
    query = session.query(Advertisement)
    if title:
        query = query.filter(Advertisement.title.ilike(f"%{title}%"))
    ads = await query.all()
    return {"result": [ad.dict for ad in ads]}
