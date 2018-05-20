# tetris_ai

Tetris.py was originally developed by <me@laria.me>.
I've made some light changes and bugfixes.

##  Changes:
	- Fixed rotations so that it rotates about a point.
		(indicated by the ".5" in the tetris_shapes)
	- Made a script to find these 90degree rotations (see test folder),
	then I saved them to the file, rotations.py to pull them from memory
	instead of calculating them each time.
	- Moved this new code to rotations.py.
	- After collision, you get 3 frames to move it around.
	- Increased frame rate to 40fps
	- Calls tetris_ai.py (in progress)
