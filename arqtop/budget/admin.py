from django.contrib import admin
from .models import DataEntry
from .models import ExecutiveProject
from .models import PreliminaryStudy
from .models import ArchitecturalNeeds
from .models import Project

# Register your models here.
DataEntry.register_admin()
ExecutiveProject.register_admin()
PreliminaryStudy.register_admin()
ArchitecturalNeeds.register_admin()
Project.register_admin()