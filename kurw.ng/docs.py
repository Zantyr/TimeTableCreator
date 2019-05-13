version=[0,2,0]

helpstr="""
This is CompactLisp by Zantyr
Actual version is: """+'.'.join(map(str,version))+"""
Used for computation and scripting.
Designed to use Android phone keys.
For cheatsheets type (? TOPIC)
Topics:
syntax - all non-function tokens
arithm - basic operations
lists  - operations on basic struct"""

"""
Future:
string - all needed string interface
math   - bindings to math functions
iface  - device io, files, sessions
crunch - numpy functions
"""
docstr={
	"syntax":"""
(' x)     - return x unevaluated
(# x y)   - set uneval x to y
(#! x y)  - set evalled x to y
(! x)     - execute list x, ret last
(!: ...)  - execute unpacked list
(? x y)   - if x execute y
(? x y z) - if x then y else z
Future:
($! x)    - set macrobuffer to x
$!1       - evaluates to macrobuffer
""",
  "arithm":"""
(& ...)   - sum all arguments
(- ...)   - subtract all from first
(* ...)   - multiply all
(/ ...)   - divide first by all
(-- x)    - negate logically x
(** ...)  - x**y**z...
(!** x y?)- logarithm base y
""",
  "lists":"""
(@.. ...) - list constructor
(@ x y)   - xth element of y
(@# x y)  - append y to x
(@@ x y)  - concatenate x and y
"""}

doclist=['syntax','arithm','lists']
