# This is an example of the input `gantt` expects.
# Lines starting with a '#' are ignored.
# Whitespace padding is also ignored.
# Hint: try piping this output back into `gantt` to see the visual output.

- START: 2026-03-02
#- MODULO: 7
- MODULO_SHIFT: 3
# - DARK_CHAR: -
# - LIGHT_CHAR: +

Testing:
  Test Live View: 15
  More testing: done


Attendance Blocks Tab:
  Design UX: 8   
  Implement Listings: blocked
  Implement Details: 8 -3
Directory-Attendance Integration:
  Design UX: done
  Implement Viewing: 10 -3
  This: 5
# shift and specified start date
 That: 8 /2 *2026-03-30
  Design UX: done
  More Viewing: 13 -1


