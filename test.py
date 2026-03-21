from datetime import date, timedelta
import re

filename = 'test.g'
# filename = 'test2.g'

comment_char = '#'
option_char = '-'
break_char = ':'

box_light_char="▒"
box_dark_char="█"
# DEFAULT_GANTT_CHART_CHARACTER_TIMELINE="•"
# DEFAULT_GANTT_CHART_CHARACTER_TIMELINE="-"

extra_chars = '+-/*'

f_date = None
header_modulo = 7
counter_string_modulo = True


color = {'PURPLE' : '\033[95m',
   'CYAN' : '\033[96m',
   'DARKCYAN' : '\033[36m',
   'BLUE' : '\033[94m',
   'GREEN' : '\033[92m',
   'YELLOW' : '\033[93m',
   'RED' : '\033[91m',
   'BOLD' : '\033[1m',
   'UNDERLINE' : '\033[4m',
   'END' : '\033[0m'}

def format(style, string):
   return color[style] + string + color['END']

print(format('BOLD', 'HeLlo there!'))

keys = []
vals = []
max_key_len = 0
total_val_count = 0
with open(filename) as file:
    for i,line in enumerate(file):
        # print('line', line)
        if line[0] == comment_char:
            pass
            # print('Comment line.')
        elif line[0] == option_char:
            # print('Comment line.')
            chunks = line[1:].strip().split(break_char)
            option = chunks[0].strip()
            val = chunks[1].strip()
            print('option:', option, val)
            if option == 'START':
                # f_date = date(2026, 5, 20)
                f_date = date.fromisoformat(val)
        else:
            if break_char in line:
                # line has break_char
                chunks = line.split(break_char)

                key = chunks[0].strip()
                # print('chunks', chunks)
                if chunks[1].strip() == '':
                    # heading line
                    # print(format('BOLD', chunks[0].strip()))
                    keys.append(key)
                    vals.append(0)
                else:
                    # non-heading line
                    if chunks[1].strip().isdigit():
                        # value is a digit
                        val = int(chunks[1])
                        # print('adding val:', val)
                        total_val_count += val
                    else:
                        # value is not a digit
                        print('Not digit', chunks[1].strip())
                        val = chunks[1].strip()

                        # # val_chunks = re.split(r'[()]', val)
                        # val_chunks = re.sub(r'[()]', "", val).split()
                        # print('val_chunks', val_chunks)

                        val_chunks = val.split(' ')
                        if all([str(ch).lstrip(extra_chars).isdigit() for ch in val_chunks]):
                            print('val_chunks', val_chunks)
                            total_val_count += int(val_chunks[0])

                    keys.append(key)
                    vals.append(val)

                    max_key_len = max(max_key_len, len(key))



                # name, var = line.partition(":")[::2]
                # myvars[name.strip()] = float(var)
            else:
                print('Bad line', i+1)

# print('key_val', keys, vals)
# print('total_val_count', total_val_count)


if f_date is not None:
    header_month = ' ' * max_key_len
    header_date = ' ' * max_key_len
    # header = ' ' * max_key_len


    header_count = 0
    for i in range(total_val_count):
        if i % header_modulo == 0:

            date = f_date + timedelta(days=i)
            date_s = "{:%b %d}".format(date)


            ## Full date
            # header += date_s
            # header += ' ' * (header_modulo - len(date_s))
            counter_str = "{:%b}".format(date)
            header_month += counter_str
            header_month += ' ' * (header_modulo - len(counter_str))

            counter_str = "{:%d}".format(date)
            header_date += counter_str
            header_date += ' ' * (header_modulo - len(counter_str))

            header_count += 1

    header = header_month  + '\n' + header_date
    # header = header_date

else:
    header = ' ' * max_key_len
    header_count = 0
    for i in range(total_val_count):
        if i % header_modulo == 0:
            if counter_string_modulo:
                counter_str = str(header_count)
            else:
                counter_str = str(i)
            header += counter_str
            header += ' ' * (header_modulo - len(counter_str))

            header_count += 1

print(header)

# hline = ' ' * max_key_len + '-' * total_val_count
hline = ' ' * max_key_len
header_count = 0
for i in range(total_val_count):
    if i % header_modulo == 0:
        # hline += '|'
        hline += box_dark_char
    else:
        # hline += '-'
        hline += box_light_char
print(hline)
# process


# print
running_count = max_key_len
# print('running_count', running_count)
for i in range(len(keys)):
    key = keys[i]
    val = vals[i]
    if val == 0:
        # heading line
        key_str = format('UNDERLINE', format('BOLD', key))
        val_str = ''
    else:
        # not a heading line
        key_str = key
        if str(val).isdigit():
            # value is a single digit
            val_str = ' ' * (running_count - len(key))
            val_str += box_dark_char * val 
            val_str += ' ' 

            running_count += int(val)

            val_str += ' ' 
            val_str += str(val)
        else:
            # value is not a single digit
            val_chunks = val.split(' ')
            # print('val_chunks', val_chunks)
            # print([str(ch).lstrip(extra_chars).isdigit() for ch in val_chunks])
            if val_chunks[0].strip().isdigit():
                # value is numbers separated by space, with extra leading chars from the second one onward
                shift = 0
                highlight_len = 0

                for ch in val_chunks:
                    if ch[0] in '+-':
                        shift = int(ch)
                    if ch[0] == '/':
                        highlight_len = int(ch[1:])
                    if ch[0] == '*':
                        start_date = date.fromisoformat(ch[1:])
                        # print('start_date', start_date)
                        # shift = ((f_date + timedelta(days=running_count)) - start_date).days
                        # print('(start_date-f_date).days', (start_date-f_date).days)
                        # print('running_count', running_count)
                        # shift = -(start_date - f_date).days
                        shift =  (start_date - f_date).days - (running_count - max_key_len)
                val_str = ' ' * (running_count - len(key) + shift)
                val_str += box_light_char * highlight_len + box_dark_char * (int(val_chunks[0]) - highlight_len) 

                running_count += int(val_chunks[0]) + shift

                val_str += ' ' 
                val_str += str(val_chunks[0])
            else:
                # pure string
                val_str = ' ' * (running_count - len(key))
                val_str += str(val)

    out_line = key_str + val_str
    print(out_line)


print(hline)
print(header)
