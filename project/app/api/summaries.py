from app.api import crud
from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def create_summary(
    payload: SummaryPayloadSchema,
) -> SummaryResponseSchema:
    summary_id = await crud.post(payload)

    response_object = {"id": summary_id, "url": payload.url}
    return response_object
