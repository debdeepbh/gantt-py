# This is an example of the input `gantt` expects.
# Lines starting with a '#' are ignored.
# Whitespace padding is also ignored.
# Hint: try piping this output back into `gantt` to see the visual output.
Testing:
  Test Live View: 5
  More testing: done

START 2026-05-02
Attendance Blocks Tab:
  Design UX: 3 
  Implement Listings: blocked
  Implement Details: 2
Directory-Attendance Integration:
  Design UX: done
  Implement Viewing: 8 (3)
  Design UX: done
  More Viewing: 13

+++++++++++++++++++++++++++++++++++++
Title
    A:    done
More title
    B:      -------------------------
    C:                  -----------------
    More:         ----- -----------
    This:               - 17
+++++++++++++++++++++++++++++++++++++

