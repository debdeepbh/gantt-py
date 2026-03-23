# This is an example of the input `gantt` expects.
# Lines starting with a '#' are ignored.
# Whitespace padding is also ignored.
# Hint: try piping this output back into `gantt` to see the visual output.

- START: 2026-03-02

#- MODULO: 7
#- MODULO_SHIFT: 3
# - DARK_CHAR: -
# - LIGHT_CHAR: +

Testing:
  # Test Live View: 15 /3
#  Test Live View: 15 /3 ^2026-03-09
  More testing: done
Attendance Blocks Tab:
  Design UX: 8   
  Implement Listings: blocked
  Implement Details: 8 -3 @red
Directory-Attendance Integration:
  Design UX: done
  Implement Viewing: 10 -3 @green
  This: 5
shift and specified start date
That: 8 /2 ^2026-03-30 @blue
  Design UX: done more
  More Viewing: 13 -1 @yellow
---
By date: ^2026-03-13 $2026-04-20 /10 @cyan
By enddate: $2026-03-14 7 @yellow


