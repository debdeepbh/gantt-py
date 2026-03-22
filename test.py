from datetime import date, timedelta, datetime
import argparse

# Instantiate the parser
parser = argparse.ArgumentParser(description='Optional app description')
parser.add_argument('--filename', type=str, help='input filename', default='test.g')
parser.add_argument('--debug', action='store_true', help='do not print diagnostics')
args = parser.parse_args()


comment_char = '#'
option_char = '-'
break_char = ':'
extra_chars = '+-/*'

box_light_char="▒"
box_dark_char="█"
# DEFAULT_GANTT_CHART_CHARACTER_TIMELINE="•"
# DEFAULT_GANTT_CHART_CHARACTER_TIMELINE="-"

f_date = None
header_modulo = 7
counter_string_modulo = True
modulo_shift = 0

gap = 0

color = {'PURPLE' : '\033[95m',
   'CYAN' : '\033[96m',
   'DARKCYAN' : '\033[36m',
   'BLUE' : '\033[94m',
   'GREEN' : '\033[92m',
   'YELLOW' : '\033[93m',
   'RED' : '\033[91m',
   'BOLD' : '\033[1m',
   'FAINT' : '\033[2m',
   'ITALIC' : '\033[3m',
   'UNDERLINE' : '\033[4m',
   'INVERSE' : '\033[7m',
   'BLINKING' : '\033[5m',
   'END' : '\033[0m'}

class entry(object):
    """Entry"""
    def __init__(self):
        self.key_string = ''
        self.type = 'data'
        self.duration = 0
        self.shift = 0
        self.highlight_len = 0
        self.value_string = ''

        self.start_date = None
        self.end_date = None

        self.start_ind = 0
        self.output_string = ''
        

def format(style, string):
   return color[style] + string + color['END']

#######################################################################
# output header

def get_header_date(f_date, total_duration, header_modulo=7, modulo_shift=0):
    """A header with month, date, and dow, given starting date and duration

    :f_date: First date
    :total_duration: integer
    :header_modulo: how often to print
    :modulo_shift: shift of starting print
    :returns: header_month, header_date
    """
    header_month = ''
    header_date = ''

    header_month += ' ' * modulo_shift
    header_date += ' ' * modulo_shift

    for i in range(total_duration):
        if i % header_modulo == modulo_shift:
            # print every modulo days
            date = f_date + timedelta(days=i)

            ## month only
            counter_str = "{:%b}".format(date)
            header_month += counter_str
            header_month += ' ' * (header_modulo - len(counter_str))

            ## date digits only
            counter_str = "{:%d}".format(date)
            header_date += counter_str
            header_date += ' ' * (header_modulo - len(counter_str))

    return header_month, header_date

def get_hline_dow(f_date, total_duration, hl_today=True):
    """A header line with day of the week string with possible highlight of today's date, given initial date and duration

    :f_date: starting date
    :total_duration: duration of header in days
    :hl_today: highlight today's day
    :returns: string

    """
    hline = ''
    for i in range(total_duration):
        date = f_date + timedelta(days=i)

        counter_str = "{:%a}".format(date)[0]

        if hl_today and (date == datetime.today().date()):
            # highlight today's date
            # hline += format('BOLD', format('INVERSE', counter_str))
            # hline += format('BOLD', format('INVERSE', box_dark_char))
            hline += format('BOLD', format('INVERSE', box_dark_char))
        else:
            if i % header_modulo == modulo_shift:
                # hline += '|'
                # hline += box_dark_char
                hline += format('INVERSE', counter_str)
            else:
                # hline += '-'
                # hline += box_light_char
                hline += format('FAINT', format('INVERSE', counter_str))
    return hline


# print(format('BOLD', 'HeLlo there!'))

def get_header_hline_num(total_duration, header_modulo=7, modulo_shift=0):
    """TODO: Docstring for get_header_hline_num.

    :total_duration: TODO
    :header_modulo: TODO
    :modulo_shift: TODO
    :returns: TODO

    """
    header = ''
    header_count = 0
    for i in range(total_duration):
        if i % header_modulo == modulo_shift:
            if counter_string_modulo:
                counter_str = str(header_count)
            else:
                counter_str = str(i)
            header += counter_str
            header += ' ' * (header_modulo - len(counter_str))

            header_count += 1

    # hline = ' ' * max_key_len + '-' * total_val_count
    hline = ''
    header_count = 0
    for i in range(total_duration):
        if i % header_modulo == modulo_shift:
            # hline += '|'
            hline += box_dark_char
        else:
            # hline += '-'
            hline += box_light_char

    return header, hline

#######################################################################
# read file

entries = []
with open(args.filename) as file:
    for i,line in enumerate(file):
        if line[0] == comment_char:
            # comment line
            pass
        elif line.strip() == '':
            # empty line
            pass
        elif line[0] == option_char:
            # option line
            chunks = line[1:].strip().split(break_char)
            option = chunks[0].strip()
            val = chunks[1].strip()
            if args.debug:
                print('Option:', option, val)
            if option == 'START':
                f_date = date.fromisoformat(val)
            if option == 'MODULO':
                header_modulo = int(val)
            if option == 'LIGHT_CHAR':
                box_light_char = str(val)
            if option == 'DARK_CHAR':
                box_dark_char = str(val)
            if option == 'MODULO_SHIFT':  
                modulo_shift = int(val)
        else:
            # data line
            if break_char in line:
                # line has break_char; valid data line
                e = entry()
                chunks = line.split(break_char)
                key = chunks[0].strip()
                e.key_string = key
                if chunks[1].strip() == '':
                    # heading line
                    e.type = 'heading'
                else:
                    # non-heading line
                    val = chunks[1].strip()
                    val_chunks = val.split(' ')
                    if val_chunks[0].strip().isdigit():
                        # first () chunk is a digit; good data line
                        e.type = 'data'
                        e.duration = int(val_chunks[0])

                        if len(val_chunks) > 1:
                            # if other options specified
                            for ch in val_chunks:
                                if ch[0] in '+-':
                                    e.shift = int(ch)
                                if ch[0] == '/':
                                    e.highlight_len = int(ch[1:])
                                if ch[0] == '*':
                                    e.start_date = date.fromisoformat(ch[1:])
                    else:
                        # first entry not integer
                        if len(val_chunks) == 2 and all([ch[0] in '*$' for ch in val_chunks ]):
                            # two entries are prefixed by * and $
                            print('val_chunks', val_chunks)
                            # special data: starting and ending date
                            e.type = 'data'
                            # look for starting and ending date
                            for ch in val_chunks:
                                if ch[0] == '*':
                                    e.start_date = date.fromisoformat(ch[1:])
                                if ch[0] == '$':
                                    e.end_date = date.fromisoformat(ch[1:])
                            e.duration = int((e.end_date - e.start_date).days)
                            print('e.duration', e.duration)
                        else:
                            # treat value as pure string
                            e.type = 'text'
                            e.value_string = str(val)
                entries.append(e)
            else:
                # if args.debug:
                    print('Bad line:', i+1)

#######################################################################
# Processing

# max key string length
max_key_len = max( [len(e.key_string) for e in entries if e.type != 'heading'])

# computing starting index of each bar
total_duration = 0
running_duration = 0
for i,e in enumerate(entries):
    if e.start_date is not None:
        e.shift = (e.start_date - f_date).days - running_duration
    e.start_ind = running_duration + e.shift
    running_duration = e.start_ind + e.duration

    # need to save historical max duration
    total_duration = max(running_duration, total_duration)

if args.debug:
    for i,e in enumerate(entries):
        print('e', e.__dict__)
    print('total_duration', total_duration)


    
#######################################################################
# output string construction
for i,e in enumerate(entries):
    if e.type == 'heading':
        e.output_string = format('UNDERLINE', format('BOLD', e.key_string))
    else:
        key_str = e.key_string + ' ' * (max_key_len - len(e.key_string))
        val_str = ' ' * e.start_ind

        if e.type == 'data':
            if e.highlight_len:
                val_str += box_light_char * e.highlight_len + box_dark_char * (e.duration - e.highlight_len) 
            else:
                val_str += box_dark_char * e.duration

            val_str += ' ' + str(e.duration)
            # val_str += ' ' + str(e.duration) + ' ' + str(e.shift) + ' ' + str(e.start_ind)
            # val_str += ' ' + str(e.duration) + str(e.shift) + ' ' + str(e.start_ind)
        elif e.type == 'text':
                val_str += e.value_string
        else:
            pass

        e.output_string = key_str + ' ' * gap + val_str

#######################################################################
# Output

blank = ' ' * (max_key_len + gap)
if f_date is not None:
    header_month, header_date =  get_header_date(f_date, total_duration, header_modulo=header_modulo, modulo_shift=modulo_shift)
    hline = get_hline_dow(f_date, total_duration, hl_today=True)

    header_top = blank + header_month + '\n' + blank + header_date + '\n' + blank + hline
    header_bottom =  blank + hline + '\n' + blank + header_date + '\n' + blank + header_month

else:

    header, hline = get_header_hline_num(total_duration, header_modulo=header_modulo, modulo_shift=modulo_shift)

    header_top = blank + header + '\n' + blank + hline
    header_bottom =  blank + hline + '\n' + blank + header 



# final output
print(header_top)
for i,e in enumerate(entries):
    print(e.output_string)
print(header_bottom)


