import os
import tempfile
import sys

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
scr_dict = {}
key_mode = sys.argv[1]
key = sys.argv[2]

try:
    val_mode = sys.argv[3]
except IndexError:
    try:
        with open(storage_path, 'r') as f_in:

            for item in f_in:
                item_list = item.split()
                tmp_key = item_list[0]
                tmp_val = item_list[1:]
                scr_dict[tmp_key] = tmp_val
    except FileNotFoundError:
        print(None)
    else:
        try:
            print(', '.join(scr_dict[key]))
        except KeyError:
            print(None)
else:
    val = sys.argv[4]
    try:
        with open(storage_path, 'r') as f_in:
            scr_dict = {}
            for item in f_in:
                item_list = item.split()
                tmp_key = item_list[0]
                tmp_val = item_list[1:]
                scr_dict[tmp_key] = tmp_val
    except FileNotFoundError:
        temp = tempfile.NamedTemporaryFile(delete=False)
        temp.name = 'storage.data'
    if key_mode == '--key' and val_mode == '--val':
        scr_dict[key] = scr_dict.get(key, [])
        scr_dict[key].append(val)
        with open(storage_path, 'w') as f_out:
            for new_key in scr_dict:
                print(new_key, ' '.join(scr_dict[new_key]), file=f_out)
