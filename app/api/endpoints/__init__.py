# FastAPI's APIRouter allows us to split our routes across multiple files for better organization.
from fastapi import APIRouter

# Import routers from various modules in the project.
from .questions import router as questions_router
from .visualizations import router as visualizations_router
from .metadata import router as metadata_router
from .schema import router as schema_router

# Initialize the main router.
router = APIRouter()

# Include the imported routers into the main router. 
# This essentially adds the routes defined in each module to the main application.
# Each router is also prefixed with a path and tagged for better organization and documentation.

router.include_router(questions_router, prefix="/questions", tags=["questions"])
router.include_router(visualizations_router, prefix="/visualizations", tags=["visualizations"])
router.include_router(metadata_router, prefix="/metadata", tags=["metadata"])
router.include_router(schema_router, prefix="/schema", tags=["schema"])
