# This is an example of the input `gantt` expects.
# Lines starting with a '#' are ignored.
# Whitespace padding is also ignored.
# Hint: try piping this output back into `gantt` to see the visual output.

- START: 2026-05-02

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
  That: 8 /2 *2026-05-30
  Design UX: done
  More Viewing: 13 -1


