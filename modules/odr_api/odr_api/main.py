from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from odr_api.api.endpoints import user_router, team_router, content_router, annotation_router, auth_router, embedding_router, health
from odr_core.config import settings
import uvicorn

app = FastAPI(title=settings.PROJECT_NAME)
# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/test")
def test_communication():
    return {"message": "Communication successful!"}


app.include_router(team_router, prefix=settings.API_V1_STR)
app.include_router(user_router, prefix=settings.API_V1_STR)
app.include_router(content_router, prefix=settings.API_V1_STR)
app.include_router(annotation_router, prefix=settings.API_V1_STR)
app.include_router(auth_router, prefix=settings.API_V1_STR)
app.include_router(embedding_router, prefix=settings.API_V1_STR)
app.include_router(health.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=31100, reload=True)
