# Copyright © 2023, Cristhian A. Gonzales Castillo. All Rights Reserved.
#
# This file is part of ShPy.
#
# ShPy is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# ShPy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with ShPy. If not, see <https://www.gnu.org/licenses/>.

from .command import Command

class Shell:
    def __init__(self):
        self.clis = {}

    def Register(self, command: Command):
        self.clis[command.name] = command
