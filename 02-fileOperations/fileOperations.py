# fileopeations
import sys

filename = sys.argv[1]
key = sys.argv[2]
values = sys.argv[3]


def update_server_config(file_path, key, value):

    # readfile operation
    with open(file_path,"r") as file:
        lines = file.readlines()

    # writeFile opearion
    with open(file_path,"w") as mln:
        for line in lines:
            if key in line:
                mln.write(key + "=" + value + "\n")
            else:
                mln.write(line)

update_server_config(filename, key, values)
