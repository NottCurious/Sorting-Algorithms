import os
import importlib
from arrays import *
import colorama
from colorama import Fore
import time

TEN_UNSORTED = [TEN_ONE_UNSORTED, TEN_TWO_UNSORTED, TEN_THREE_UNSORTED, TEN_FOUR_UNSORTED, TEN_FOUR_UNSORTED]
HUNDRED_UNSORTED = [HUNDRED_ONE_UNSORTED, HUNDRED_TWO_UNSORTED, HUNDRED_THREE_UNSORTED, HUNDRED_FOUR_UNSORTED, HUNDRED_FIVE_UNSORTED, HUNDRED_SIX_UNSORTED, HUNDRED_SEVEN_UNSORTED, HUNDRED_EIGHT_UNSORTED, HUNDRED_NINE_UNSORTED, HUNDRED_TEN_UNSORTED]
THOUSAND_UNSORTED = [THOUSAND_ONE_UNSORTED, THOUSAND_TWO_UNSORTED, THOUSAND_THREE_UNSORTED, THOUSAND_FOUR_UNSORTED, THOUSAND_FIVE_UNSORTED, THOUSAND_SIX_UNSORTED, THOUSAND_SEVEN_UNSORTED]
TWO_THOUSAND_FIVE_HUNDRED_UNSORTED = [TWO_THOUSAND_FIVE_HUNDRED_ONE_UNSORTED, TWO_THOUSAND_FIVE_HUNDRED_TWO_UNSORTED, TWO_THOUSAND_FIVE_HUNDRED_THREE_UNSORTED, TWO_THOUSAND_FIVE_HUNDRED_FOUR_UNSORTED]
ALPHABETS_UNSORTED = [ALPHABETS_ONE_UNSORTED, ALPHABETS_TWO_UNSORTED, ALPHABETS_THREE_UNSORTED, ALPHABETS_FOUR_UNSORTED]

if __name__ == '__main__':
    for file in os.listdir('./algorithms'):
        if file == '__pycache__':
            continue

        print(Fore.CYAN + f'Testing ' + Fore.LIGHTMAGENTA_EX + f'{file[:-3]}' + Fore.WHITE)

        importPath = 'algorithms.' + file[:-3]
        sortAlgo = importlib.import_module(importPath)

        print(f'Testing 10 Length Arrays for {file[:-3]}...', end='\r')
        
        skip_print = False

        for unsorted_array in TEN_UNSORTED:
            if(sortAlgo.sort(unsorted_array) != TEN_SORTED):
                print(f'Tested 10 Length Arrays for {file[:-3]}... ' + Fore.RED + 'Failed')
                print(Fore.WHITE)

                skip_print = True

        if not skip_print:
            print(f'Tested 10 Length Arrays for {file[:-3]}... ' + Fore.LIGHTGREEN_EX + 'Ok')
        print(Fore.WHITE, end='\r')

        print(f'Testing 10 Length Arrays With Duplicates for {file[:-3]}...', end='\r')

        first_ten_flag = (sortAlgo.sort(TEN_ONE_UNSORTED_DUPLICATES) == TEN_ONE_SORTED_DUPLICATES)
        second_ten_flag = (sortAlgo.sort(TEN_TWO_UNSORTED_DUPLICATES) == TEN_TWO_SORTED_DUPLICATES)
        third_ten_flag = (sortAlgo.sort(TEN_THREE_UNSORTED_DUPLICATES) == TEN_THREE_SORTED_DUPLICATES)

        if(not first_ten_flag or not second_ten_flag or not third_ten_flag):
            print(f'Tested 10 Length Arrays with Duplicates for {file[:-3]}... ' + Fore.RED + 'Failed')
            print(Fore.WHITE, end='\r')
        else:
            print(f'Tested 10 Length Arrays with Duplicates for {file[:-3]}... ' + Fore.LIGHTGREEN_EX + 'Ok')
            print(Fore.WHITE, end='\r')

        skip_print = False

        print(f'Testing 100 Length Arrays for {file[:-3]}...', end='\r')
        
        for unsorted_array in HUNDRED_UNSORTED:
            if(sortAlgo.sort(unsorted_array) != HUNDRED_SORTED):
                print(f'Tested 100 Length Arrays for {file[:-3]}... ' + Fore.RED + 'Failed')
                print(Fore.WHITE)

                skip_print = True
        
        if not skip_print:
            print(f'Tested 100 Length Arrays for {file[:-3]}... ' + Fore.LIGHTGREEN_EX + 'Ok')
        print(Fore.WHITE, end='\r\r')

        first_hundred_flag = (sortAlgo.sort(HUNDRED_ONE_UNSORTED_DUPLICATES) == HUNDRED_ONE_SORTED_DUPLICATES)
        second_hundred_flag = (sortAlgo.sort(HUNDRED_TWO_UNSORTED_DUPLICATES) == HUNDRED_TWO_SORTED_DUPLICATES)
        third_hundred_flag = (sortAlgo.sort(HUNDRED_THREE_UNSORTED_DUPLICATES) == HUNDRED_THREE_SORTED_DUPLICATES)

        if not first_hundred_flag or not second_hundred_flag or not third_hundred_flag:
            print(f'Tested 100 Length Arrays with Duplicates for {file[:-3]}... ' + Fore.RED + 'Failed')
            print(Fore.WHITE, end='\r')
        else:
            print(f'Tested 100 Length Arrays with Duplicates for {file[:-3]}... ' + Fore.LIGHTGREEN_EX + 'Ok')
            print(Fore.WHITE, end='\r')

        skip_print = False

        print(f'Testing 10000 Length Arrays for {file[:-3]}...', end='\r')
        
        for unsorted_array in THOUSAND_UNSORTED:
            if(sortAlgo.sort(unsorted_array) != THOUSAND_SORTED):
                print(f'Tested 1000 Length Arrays for {file[:-3]}... ' + Fore.RED + 'Failed')
                print(Fore.WHITE, end='\r')

                skip_print = True
        
        if not skip_print:
            print(f'Tested 1000 Length Arrays for {file[:-3]}... ' + Fore.LIGHTGREEN_EX + 'Ok')
        print(Fore.WHITE, end='\r')

        skip_print = False

        print(f'Testing 2500 Length Arrays for {file[:-3]}...', end='\r')
        
        for unsorted_array in TWO_THOUSAND_FIVE_HUNDRED_UNSORTED:
            if(sortAlgo.sort(unsorted_array) != TWO_THOUSAND_FIVE_HUNDRED_SORTED):
                print(f'Tested 2500 Length Arrays for {file[:-3]}... ' + Fore.RED + 'Failed')
                print(Fore.WHITE)

                skip_print = True
        
        if not skip_print:
            print(f'Tested 2500 Length Arrays for {file[:-3]}... ' + Fore.LIGHTGREEN_EX + 'Ok')
        print(Fore.WHITE, end='\r\r')

        skip_print = False

        print(f'Testing Alphabet Arrays for {file[:-3]}...', end='\r')
        
        for unsorted_array in ALPHABETS_UNSORTED:
            if(sortAlgo.sort(unsorted_array) != ALPHABETS_SORTED):
                print(f'Tested Alphabet Arrays for {file[:-3]}... ' + Fore.RED + 'Failed')
                print(Fore.WHITE)

                skip_print = True
        
        if not skip_print:
            print(f'Tested Alphabet Arrays for {file[:-3]}... ' + Fore.LIGHTGREEN_EX + 'Ok')
        print(Fore.WHITE, end='\r\r')

        first_alphabet_flag = (sortAlgo.sort(ALPHABETS_ONE_UNSORTED_DUPLICATES) == ALPHABETS_ONE_SORTED_DUPLICATES)
        second_alphabet_flag = (sortAlgo.sort(ALPHABETS_TWO_UNSORTED_DUPLICATES) == ALPHABETS_TWO_SORTED_DUPLICATES)

        if not first_alphabet_flag or not second_alphabet_flag:
            print(f'Tested Alphabet Arrays with Duplicates for {file[:-3]}... ' + Fore.RED + 'Failed')
            print(Fore.WHITE, end='\r')
        else:
            print(f'Tested 100 Alphabet Arrays with Duplicates for {file[:-3]}... ' + Fore.LIGHTGREEN_EX + 'Ok')
            print(Fore.WHITE, end='\r')

        print('\n')

        time.sleep(1)