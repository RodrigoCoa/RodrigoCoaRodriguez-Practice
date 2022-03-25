class Suit:
    def max(self, num):
        lst_num = list()
        if num >= 100:
            for i in str(num):
                lst_num.append(int(i))
        else:
            return False
        return max(lst_num)

    def is_vowel(self, vocal):
        vocales = ['a', 'e', 'i', 'o', 'u']
        if str(vocal).lower() in vocales:
            return 'Vowel'
        elif str(vocal).isalpha():
            return 'Consonant'
        elif not str(vocal).isnumeric():
            try:
                if vocal < 0:
                    return 'Num'
            except:
                return False
        else:
            return 'Num'

    def inverse(self, word):
        string_list_rever = list()
        cont = -1
        string = str(word)
        while cont >= -len(string):
            string_list_rever.append(string[cont])
            cont -= 1
        if string.isnumeric():
            return int("".join(string_list_rever))
        else:
            return "".join(string_list_rever)

    def palindromo(self, word):
        string_list_rever = list()
        cont = -1
        word = str(word)
        while cont >= -len(word):
            string_list_rever.append(word[cont])
            cont -= 1
        palin = "".join(string_list_rever)
        if palin == word:
            if word.isnumeric():
                return int(palin)
            return palin
        else:
            return False

    def array_max(self, array_valors):
        return max(array_valors)

    def array_min(self, array_valors):
        return min(array_valors)

    def array_avg(self, array_valors):
        return sum(array_valors)/len(array_valors)

    def country(self, countries):
        try:
            largest = None
            sec_largest = ""
            for country in countries:
                lenght = len(country)
                if largest == None:
                    largest = country
                elif len(largest) < lenght:
                    largest = country
            return largest
        except:
            return False

    def binario(self, num):
        try:
            bin_list = list()
            val = 256
            for i in range(9):
                if (num - val) >= 0:
                    num = num - val
                    bin_list.append('1')
                else:
                    bin_list.append('0')
                val = val / 2
            bin = "".join(bin_list)
            return int(bin)
        except:
            return False

    def cont_string(self, string):
        return len(string)













