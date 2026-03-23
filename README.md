# gantt-py

Gantt chart on terminal with calendar and other stuff, written in python. Inspired by [gantt](https://github.com/andrew-ls/gantt).

## Features

- calendar support
- highlighting today's date
- shifting events left of right
- color support
- adding entry by any two of start date, end date, duration


## Demo

```bash
chmod +x gantt
./gantt test-2.g


                  0      1      2      3      4      5      6      7      8      
                  █▒▒▒▒▒▒█▒▒▒▒▒▒█▒▒▒▒▒▒█▒▒▒▒▒▒█▒▒▒▒▒▒█▒▒▒▒▒▒█▒▒▒▒▒▒█▒▒▒▒▒▒█▒
Testing
Test Live View    ████ 4
Attendance Blocks Tab
Design UX             ▒█████ 6
Implement Listings           blocked
Implement Details           ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████ 24
Directory-Attendance Integration
Design UX                                            done
Implement Viewing                                   ▒▒▒▒▒▒▒▒████████████████ 24
                  █▒▒▒▒▒▒█▒▒▒▒▒▒█▒▒▒▒▒▒█▒▒▒▒▒▒█▒▒▒▒▒▒█▒▒▒▒▒▒█▒▒▒▒▒▒█▒▒▒▒▒▒█▒
                  0      1      2      3      4      5      6      7      8      
```


```bash
./gantt test-1.g

                    Mar    Mar    Mar    Mar    Mar    Apr    Apr    
                    02     09     16     23     30     06     13     
                    MTWTFSSMTWTFSSMTWTFSS█TWTFSSMTWTFSSMTWTFSSMTWTFSS
Testing
Test Live View      ███████████████ 15
Test Live View again       ▒▒▒████████████ 15
More testing                               done
Attendance Blocks Tab
Design UX                                 ████████ 8
Implement Listings                                 blocked
Implement Details                           ████████ 8
Directory-Attendance Integration
Design UX                                               done
Implement Viewing                                ██████████ 10
This                                                          █████ 5
That                                   ▒▒██████ 8
Design UX                                                done more
More Viewing                                   █████████████ 13
                    ─────────────────────────────────────────────────
By date               ▒▒▒▒▒▒▒▒▒▒████████████████████████████ 38
By enddate      ███████ 7
                    MTWTFSSMTWTFSSMTWTFSS█TWTFSSMTWTFSSMTWTFSSMTWTFSS
                    02     09     16     23     30     06     13     
                    Mar    Mar    Mar    Mar    Mar    Apr    Apr    
```

## Installation

Move the file `gantt` to a location in your `$PATH` variable, such as `$HOME/.local/bin`. Make sure the file is executable.

## Usage

```
./gantt filename
```

## Input file format

- Lines staring with `#` is a comment
- Lines staring with `-` is an option
- Lines containing `:` is an entry

### Entries

Entry lines are specified in the `key: value` format. An empty `value` means `key` is a heading. 
Simplest way to add an event is by adding a line `Name: duration`. Subsequent events will be shifted to the right in a non-overlapping way.

#### Attributes

Values can have multiple whitespace-separated attributes. Other than the event duration, each attribute must start with a special character listed below.

- an integer without any leading special character is the duration of the event
- `+` or `-`: shift the event. For example, `+n` or `-n` shifts the event by `n` units to the right or left (e.g. `-3`)
- `^`: starting date in iso format (e.g. `^2026-03-26`)
- `$`: ending date in iso format (e.g. `$2026-03-26`)
- `@`: color: red, green, blue, yellow, cyan (e.g. `@red`)
- `/`: sub-duration, not larger that the duration, e.g. (`/3`)
- an non-integer attribute without any special leading character is a string


Special entry line:
- `---`: divider line (no options or attributes)

### Options

Option lines are specified in the `- key: value` format.

- `START`: sets the starting date of the chart. If not specified, the timeline will be generic integer units, not real dates. If omitted, error will occur if the dates are specified in some entry.
- `MODULO`: how often to print header marker (integer). Default: 7
- `MODULO_SHIFT`: how much to shift the initial marker (integer < `MODULO`). Default: 0
- `LIGHT_CHAR`: character used to denote light (highlighted) part of event bar
- `DARK_CHAR`: character used to denote dark part of event bar

## Example

- See example file `test.g` and `test2.g`. Run using

```
./gantt test.g
./gantt test2.g
```




