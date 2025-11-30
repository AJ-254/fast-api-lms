import fastapi

router = fastapi.APIRouter()


@router.get("/courses")
async def read_courses():
     return {"coureses":[]}


@router.post("/courses")
async def create_course_api():
     return {"coureses":[]}


@router.get("/courses/{:id}")
async def read_course():
     return {"coureses":[]}


@router.patch("/courses/{:id}")
async def update_course():
     return {"coureses":[]}


@router.delete("/courses/{:id}")
async def delete_course():
     return {"coureses":[]}


@router.get("/courses/{:id}/sections")
async def read_course_sections():
     return {"coureses":[]}
