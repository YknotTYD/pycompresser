##file_compresser

import sys
import os

#fix n possibly crashing
#fix spe chars being fucked up
#add compilement stats

class Compresser:

    offset=35

    def compress(file,chars_offset=offset):

        with open(file,"r") as file:
            script=file.readlines()

        script=[line for line in script if line[0] not in "\n#"]
        script="".join(script)

        script=list(script)

        not_in_script=0
        while chr(not_in_script) in script:
            not_in_script+=1
        not_in_script=chr(not_in_script)

        check=lambda char: char.isalnum() or char.isalpha() or char in "_"

        for i,char in enumerate(script[:-1]):
            if check(char) and not check(script[i+1]) or char in " <>()-+*/!=[]{}\'\"\\:%:.&|^@,\n":
                script[i]+=not_in_script

        script="".join(script).split(not_in_script)

        offset=0
        for i in range(len(script)):

            if len(script[i-offset])==script[i-offset].count(" ") and script[i+1-offset]==" ":

                script[i-offset]+=" "
                del script[i+1-offset]
                offset+=1

        table=sorted(set(script),key=lambda i: -script.count(i))
        indexes=[len(repr(chr(i+chars_offset))) for i in range(len(table))]

        aqua=[None]*len(table)

        for i in range(len(table)):

            index=indexes.index(min(indexes))
            aqua[index]=table[i]
            indexes[index]=float("inf")

        table=aqua
        #table=tuple(sorted(set(script),key=lambda i: -script.count(i)))

        for i in range(len(script)):
            script[i]=chr(table.index(script[i])+chars_offset)

        script="".join(script)

        return(script,table)

    def decompress(text,table,offset=offset):
        return("".join([table[ord(char)-offset] for char in text]))

    def compile(file,offset=offset):

        text,table=Compresser.compress(file,offset)

        chars=set("".join(table))
        n=0
        while chr(n) in chars or len(repr(chr(n))[1:-1])>1:
            n+=1
        n=chr(n)

        table=repr(n.join(table))

        aqua=f"text={repr(text)}\n"
        aqua+=f"table={table}.split(\"{n}\")\n"
        aqua+=f"exec(\"\".join([table[ord(char)-{offset}] for char in text]))"

        return(aqua)

    def brute_force_compile(file,iterations=2**7,offset=0,debug_info=False):

        current_best=None
        current_best_score=float("inf")

        for i in range(iterations):

            aqua=Compresser.compile(file,offset)
            offset+=1

            if (lenght:=len(aqua.encode("utf-8")))<current_best_score:

                current_best=aqua
                current_best_score=lenght

            if debug_info:
                print(f"Test {i} with size {lenght}.")

        return(current_best)

if __name__=='__main__':

    try:

        read_from,write_to=sys.argv[1:3]

        with open(write_to,"w",encoding="utf-8") as compressed:

            aqua=Compresser.brute_force_compile(read_from,iterations=64)
            compressed.write(aqua)

        old_size=os.path.getsize(read_from)
        new_size=os.path.getsize(write_to)

        print(f"\nFrom {old_size:_} B to {new_size:_} B, -{round(100-(new_size/old_size)*100,3)}%.")

    except Exception as error:
        print(error)
        print("Command use shoud be \"python pycompresser.py file_to_compress.py new_file.py\".")