# MindSlaver - kurw.ng
This is a programmette, that interprets the scripts remotely. Currently stable, yet not very useful.
Planning to implement os calls and net functions along with computation-heavy builtIns.
Will contain a database.

Script language definitions:
  expressions as normal, although every token has to be separated by space
  flow control through "jesli"(if) and "dopoki"(while)
    enclosed by "ilsej" and "ikopod" (actually enclosings are interchangeable, this only counts occurences of them)
  "wyjeb" instance throws a variable onto a screen
  inline functions are called by ![function name]
    currently only !zapytaj is implemented, which asks for input, asking for one argument - the prompt
  operators implemented: = + - * / >> << => <= == !=
