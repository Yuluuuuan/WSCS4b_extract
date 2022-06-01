#!/usr/bin/env python3

# Imports
import os
import sys
import yaml

# The functions

def extract() -> str:
    try:
        #print(os.listdir())
        #print(os)
        os.system("cp data/a* ../data")
        os.system("cp data/h* ../data")
        os.system("cp data/o* ../data")
        os.system("cp data/s* ../data")
        os.system("cp data/t* ../data")
        os.system("cp data/X* ../data")
        os.system("cp data/gadm36_ECU_shp/* ../data/gadm36_ECU_shp")
        return "Done"
    except IOError as e:
        return f"ERROR: {e} ({e.errno})"

# The entrypoint of the script
if __name__ == "__main__":

    command = sys.argv[1]
    if command == "extract":
        print(yaml.dump({ "contents": extract() }))
    # extract()
