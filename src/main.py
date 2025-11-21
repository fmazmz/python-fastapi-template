from starlette.middleware.cors import CORSMiddleware

from src.api.v1.routes import router as template_router
from fastapi import FastAPI


app = FastAPI(
    title="FastAPI Template",
    version="0.0.1",
    docs_url="/docs",
    openapi_url="/openapi.json"
)

app.include_router(template_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins="",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)