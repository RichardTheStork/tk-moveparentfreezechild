# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.


import sgtk
from sgtk.platform import Application
import sys
sys.path.append (r'Z:\Shotgun_Studio\install\core\python')
import maya.cmds as cmds
from pymel.core import *
import math
import wtd.deadline as MDeadline
import os
import inspect
import MoveParentAndFreezeChild
shotName = None

class StgkMoveParentFreezeChild(Application):
	"""
	The app entry point. This class is responsible for intializing and tearing down
	the application, handle menu registration etc.
	"""


	def init_app(self):
		"""
		Called as the application is being initialized
		"""
		if self.context.entity is None:
			raise tank.TankError("Cannot load the Set Frame Range application! "
								 "Your current context does not have an entity (e.g. "
								 "a current Shot, current Asset etc). This app requires "
								 "an entity as part of the context in order to work.")
		self.engine.register_command("MoveParentFreezeChild", self.run_app)

	 
	def destroy_app(self):
		self.log_debug("Destroying StgkMoveParentFreezeChild")

	def run_app(self):
		obj = cmds.ls( selection=True )

		GetParent = cmds.listRelatives( obj, p=True )

		cmds.xform(obj, q=True ,piv=True )
		cmds.xform(GetParent,t=(test[0],test[1],test[2]) )
		cmds.xform(obj,t=(-test[0],-test[1],-test[2]) )

		cmds.makeIdentity(obj, apply=True )
		cmds.xform(obj,ztp=True )
		# present a pyside dialog
		# lazy import so that this script still loads in batch mode
		"""
		message = " Turntable sent \n"
		from tank.platform.qt import QtCore, QtGui
		QtGui.QMessageBox.information(None,"TD Message", message)
		"""