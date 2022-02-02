import glob
import sys

path = sys.argv[1]

list = glob.glob(path + "/**", recursive=True)

for i in list:
    if i.endswith((".py",".go",".c",".java")): 
        print(i)



