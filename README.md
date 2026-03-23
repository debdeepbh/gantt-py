# gantt-py

Gantt chart with python. Inspired by [gantt](https://github.com/andrew-ls/gantt).

## Usage

```
./gantt filename
```

## Installation

Move the file `gantt` to a location in your `$PATH` variable, such as `$HOME/.local/bin`.

## Input file format

- Lines staring with `#` is a comment
- Lines staring with `-` is an option
- Lines containing `:` is an entry

### Entries

Entry lines are specified in the `key: value` format. An empty `value` means `key` is a heading. Values can have multiple whitespace-separated attributes. Other than the duration, each attribute must start with a special character.

- an integer without any leading special character is the duration of the event
- `+` or `-`: shift. Attribute starting with `+n` or `-n` shifts the event by `n` units to the right or left (e.g. `-3`)
- `^`: starting date in iso format (e.g. `^2026-03-26`)
- `$`: ending date in iso format (e.g. `$2026-03-26`)
- `@`: color: red, green, blue, yellow, cyan
- `/`: sub-duration, not larger that the duration, e.g. (`/3`)

Special line:

- `---`: divider line (no options or attributes)

### Options

Option lines are specified in the `- key: value` format.

- `START`: sets the starting date of the chart. If not specified, the timeline will be generic integer units, not real dates. If omitted, error will occur if the dates are specified in some entry.
- `MODULO`: how often to print header marker (integer). Default: 7
- `MODULO_SHIFT`: how much to shift the initial marker. Default: 0
- `LIGHT_CHAR`: character used to denote light (highlighted) part of duration
- `DARK_CHAR`: character used to denote dark part of duration




