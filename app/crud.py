from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from models import Advertisement


async def add_advertisement(session: AsyncSession, advertisement: Advertisement) -> Advertisement:
    session.add(advertisement)
    await session.commit()
    await session.refresh(advertisement)
    return advertisement


async def get_advertisement(session: AsyncSession, advertisement_id: int) -> Advertisement:
    advertisement = await session.get(Advertisement, advertisement_id)
    if advertisement is None:
        raise HTTPException(status_code=404, detail="Advertisement not found")
    return advertisement


async def update_advertisement(session: AsyncSession, advertisement: Advertisement) -> Advertisement:
    await session.commit()
    return advertisement


async def delete_advertisement(session: AsyncSession, advertisement_id: int):
    advertisement = await get_advertisement(session, advertisement_id)
    await session.delete(advertisement)
    await session.commit()
