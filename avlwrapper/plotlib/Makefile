#***********************************************************************
#    Module:  Makefile
# 
#    Copyright (C) 1996 Harold Youngren, Mark Drela 
# 
#    This library is free software; you can redistribute it and/or
#    modify it under the terms of the GNU Library General Public
#    License as published by the Free Software Foundation; either
#    version 2 of the License, or (at your option) any later version.
#
#    This library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Library General Public License for more details.
#
#    You should have received a copy of the GNU Library General Public
#    License along with this library; if not, write to the Free
#    Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
# 
#    Report problems to:    guppy@maine.com 
#                        or drela@mit.edu  
#***********************************************************************


#=======================================#
# Makefile for Xplot11 library          #
#  use or edit the config.make file to  #
#  set specific options for your system #
#=======================================#

# Point to your install directory (if you have one...)
#INSTALLDIR = /home/codes/bin
#INSTALLDIR = /usr/local/lib
INSTALLDIR = .

# Use these to set default library name (overridden in config.make file) 
PLTLIB = libPlt.a
#PLTLIB = libPltDP.a

WOBJ = Xwin2.o
WSRC = xwin11
OBJMISC =
OBJ3D   =
OBJOLD  =
###--------------------------------------------------------
###  Uncomment to add the old plot compatibility routines
OBJOLD  = plt_old.o
###--------------------------------------------------------
###  Uncomment to add the primitive 3D-view routines
OBJ3D  = plt_3D.o



help:	
	@echo
	@echo "Usage:"
	@echo "  type: make <MACHINE>" 
	@echo "   where <MACHINE> is one of the following:"
	@echo "   gfortran - Linux/OSX/Cygwin using gcc toolset"
	@echo "   ifort    - Linux/OSX with ifort/gcc"
	@echo "   mingw    - Windows using MinGW"
	@echo "   gfortranDP - Linux/OSX/Cygwin using gcc toolset, dbleprecision"
	@echo "   ifortDP    - Linux/OSX with ifort/gcc, dblprecision"
	@echo "   mingwDP    - Windows using MinGW, dblprecision"
	@echo "   clean    - cleanup directory"
	@exit

###-------------------------------------------------------------------------
### Set compiler, compiler flags, name of output object library
gfortran:	
		@cp ./config.make.gfortran	./config.make
		@make -f Makefile.all lib
ifort:
		@cp ./config.make.ifort		./config.make
		@make -f Makefile.all lib
mingw:
		@cp ./config.make.mingw		./config.make
		@make -f Makefile.all lib
gfortranDP:	
		cp ./config.make.gfortranDP	./config.make
		make -f Makefile.all lib
ifortDP:
		@cp ./config.make.ifortDP	./config.make
		@make -f Makefile.all lib
mingwDP:
		@cp ./config.make.mingwDP	./config.make
		@make -f Makefile.all lib
clean:
		@cp ./config.make.gfortran	./config.make
		@make -f Makefile.all clean
		@rm W32win3.o


