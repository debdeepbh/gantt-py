
filename = 'test.g'

comment_char = '#'
break_char = ':'

box_light_char="▒"
box_dark_char="█"
# DEFAULT_GANTT_CHART_CHARACTER_TIMELINE="•"
DEFAULT_GANTT_CHART_CHARACTER_TIMELINE="-"

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
        else:
            if break_char in line:
                # line has break_char
                chunks = line.split(":")

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
                        total_val_count += val
                    else:
                        # value is not a digit
                        print('Not digit', chunks[1].strip())
                        val = chunks[1].strip()

                    keys.append(key)
                    vals.append(val)

                    max_key_len = max(max_key_len, len(key))



                # name, var = line.partition(":")[::2]
                # myvars[name.strip()] = float(var)
            else:
                print('Bad line', i+1)

# print('key_val', keys, vals)
# print('total_val_count', total_val_count)

header = ' ' * max_key_len + '-' * total_val_count
print(header)
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
        key_str = key
        val_str = ' ' * (running_count - len(key))
        if str(val).isdigit():
            val_str += box_light_char * val 
            val_str += ' ' 

            running_count += int(val)
        val_str += str(val)

    out_line = key_str + val_str
    print(out_line)


print(header)
