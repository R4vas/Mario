import os
import hashlib

def banner():
    os.system("clear")
    print("""\033[0;31m           
        XXXXXXXXX
      XXXXXXXXXXXXX
    XXXXXXXXXXXXXXXX 
   (__________)XXXXXX 
    ( ___  ___ XXXXXX
       o/   o   XXXXX 
    (  /        XXXXX
      /___)     XXXXX
   (             XXXX
  (     ____    ) XXX
   (               XX
    (          )    X
     (       )      *
       (    )      ***
                    *        M4ri0
                                  Created by Rot13""")

def hashing():
    print("\033[0;32m[1] md5        *          [2] sha1")
    print("[\033[0;32m3] sha224     *          [4] sha256")
    print("[\033[0;32m5] sha384     *          [6] sha512")
    print("[\033[0;32m7] sha3_224   *          [8] sha3_256")
    print("[\033[0;32m9] sha3_384   *          [10] sha3_512")

    hash_type = int(input("\033[1;33mPut the number of your hash type >>"))
    wordlist = input("\033[1;33mWordlist Path >>")
    hashed = input("\033[1;33mEnter hash to crack:").lower()

    if hash_type == 1:
        print("\033[1;35mmd5 cracking >>")
        with open(wordlist, "r", encoding="latin-1") as f:
            for line in f:
                word = line.strip()
                cracked = hashlib.md5(word.encode()).hexdigest()
                if cracked == hashed:
                    print("Hash Cracked")
                    print(f"Crack :\033[0;34m{word} ")
                    break
            else:
                print("\033[1;31mHash not found in the wordlist")

    elif hash_type == 2:
        print("\033[1;35msha1 cracking >>")
        with open(wordlist, "r", encoding="latin-1") as f:
            for line in f:
                word = line.strip()
                cracked = hashlib.sha1(word.encode()).hexdigest()
                if cracked == hashed:
                    print("Hash Cracked")
                    print(f"Crack :\033[0;34m{word} ")
                    break
            else:
                print("\033[1;31mHash not found in the wordlist")

    elif hash_type == 3:
        print("\033[1;35msha224 cracking >>")
        with open(wordlist, "r", encoding="latin-1") as f:
            for line in f:
                word = line.strip()
                cracked = hashlib.sha224(word.encode()).hexdigest()
                if cracked == hashed:
                    print("Hash Cracked")
                    print(f"Crack :\033[0;34m{word} ")
                    break
            else:
                print("\033[1;31mHash not found in the wordlist")

    elif hash_type == 4:
        print("\033[1;35msha256 cracking >>")
        with open(wordlist, "r", encoding="latin-1") as f:
            for line in f:
                word = line.strip()
                cracked = hashlib.sha256(word.encode()).hexdigest()
                if cracked == hashed:
                    print("Hash Cracked")
                    print(f"Crack :\033[0;34m{word} ")
                    break
            else:
                print("\033[1;31mHash not found in the wordlist")

    elif hash_type == 5:
        print("\033[1;35msha384 cracking >>")
        with open(wordlist, "r", encoding="latin-1") as f:
            for line in f:
                word = line.strip()
                cracked = hashlib.sha384(word.encode()).hexdigest()
                if cracked == hashed:
                    print("Hash Cracked")
                    print(f"Crack :\033[0;34m{word} ")
                    break
            else:
                print("\033[1;31mHash not found in the wordlist")

    elif hash_type == 6:
        print("\033[1;35msha512 cracking >>")
        with open(wordlist, "r", encoding="latin-1") as f:
            for line in f:
                word = line.strip()
                cracked = hashlib.sha512(word.encode()).hexdigest()
                if cracked == hashed:
                    print("Hash Cracked")
                    print(f"Crack :\033[0;34m{word} ")
                    break
            else:
                print("\033[1;31mHash not found in the wordlist")

    elif hash_type == 7:
        print("\033[1;35msha3_224 cracking >>")
        with open(wordlist, "r", encoding="latin-1") as f:
            for line in f:
                word = line.strip()
                cracked = hashlib.sha3_224(word.encode()).hexdigest()
                if cracked == hashed:
                    print("Hash Cracked")
                    print(f"Crack :\033[0;34m{word} ")
                    break
            else:
                print("\033[1;31mHash not found in the wordlist")

    elif hash_type == 8:
        print("\033[1;35msha3_256 cracking >>")
        with open(wordlist, "r", encoding="latin-1") as f:
            for line in f:
                word = line.strip()
                cracked = hashlib.sha3_256(word.encode()).hexdigest()
                if cracked == hashed:
                    print("Hash Cracked")
                    print(f"Crack :\033[0;34m{word} ")
                    break
            else:
                print("\033[1;31mHash not found in the wordlist")

    elif hash_type == 9:
        print("\033[1;35msha3_384 cracking >>")
        with open(wordlist, "r", encoding="latin-1") as f:
            for line in f:
                word = line.strip()
                cracked = hashlib.sha3_384(word.encode()).hexdigest()
                if cracked == hashed:
                    print("Hash Cracked")
                    print(f"Crack :\033[0;34m{word} ")
                    break
            else:
                print("\033[1;31mHash not found in the wordlist")

    elif hash_type == 10:
        print("\033[1;35msha3_512 cracking >>")
        with open(wordlist, "r", encoding="latin-1") as f:
            for line in f:
                word = line.strip()
                cracked = hashlib.sha3_512(word.encode()).hexdigest()
                if cracked == hashed:
                    print("Hash Cracked")
                    print(f"Crack :\033[0;34m{word} ")
                    break
            else:
                print("\033[1;31mHash not found in the wordlist")

    else:
        print("\033[1;31mInvalid hash type selected.")

def main():
    banner()
    hashing()

main()

