# Copyright (C) 2019 Christopher Gearhart
# chris@bblanimation.com
# http://bblanimation.com/
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# System imports
import os
import subprocess

# Blender imports
import bpy
from bpy.types import Operator, Panel

# Addon imports
from ..classes.JobManager import *


class BACKGROUND_PT_interface(Panel):
    bl_space_type  = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_label       = "Background Processing"
    bl_idname      = "VIEW3D_PT_tools_background_processing"
    bl_context     = "objectmode"
    bl_category    = "BackProc"

    @classmethod
    def poll(self, context):
        return True

    def draw(self, context):
        layout = self.layout
        scn = context.scene
        manager = JobManager.get_instance()

        col = layout.column(align=True)
        row = col.row(align=True)
        row.operator("scene.add_job", text="Add Job 1").job_index = 0
        row = col.row(align=True)
        row.operator("scene.add_job", text="Add Job 2").job_index = 1
        row = col.row(align=True)
        row.operator("scene.add_job", text="Add Job 3").job_index = 2
        row = col.row(align=True)
        row.operator("scene.add_job", text="Add Job 4 (timeout)").job_index = 3
        col = layout.column(align=True)
        row = col.row(align=True)
        row.prop(scn, "backproc_max_workers")
        col = layout.column(align=True)
        col.scale_y = 0.7
        row = col.row(align=True)
        row.label(text="Pending Jobs: " + str(manager.num_pending_jobs()))
        row = col.row(align=True)
        row.label(text="Running Jobs: " + str(manager.num_running_jobs()))
        row = col.row(align=True)
        row.label(text="Completed Jobs: " + str(manager.num_completed_jobs()))
        row = col.row(align=True)
        row.label(text="Dropped Jobs: " + str(manager.num_dropped_jobs()))
        row = col.row(align=True)
        row.label(text="Available Workers: " + str(manager.num_available_workers()))
