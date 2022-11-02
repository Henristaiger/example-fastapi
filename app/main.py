# venv with c:/Users/Henri.Staiger/GitRepo/FastAPI/fastapi/Scripts/activate.bat
# runn with uvicorn main:app --reload
# runn with uvicorn app.main:app --reload

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from .routers import post, user, auth, vote


# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
    return {"message": "Hello World!"}
