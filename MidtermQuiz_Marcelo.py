class TempConversion:
    def __init__(self, temp):
        self.__temp = temp

    def __fah_to_cel(self):
        return (self.__temp - 32) * 5/9

    def __kel_to_cel(self):
        return self.__temp - 273.15

    def __cel_to_fah(self):
        return (self.__temp * 9/5) + 32

    def __kel_to_fah(self):
        return (self.__temp - 273.15) * 9/5 + 32

    def __cel_to_kel(self):
        return self.__temp + 273.15

    def __fah_to_kel(self):
        return (self.__temp - 32) * 5/9 + 273.15

    def get_conversions(self):
        print('Fahrenheit to Celsius:', self.__fah_to_cel(), '°C')
        print('Kelvin to Celsius:', self.__kel_to_cel(), '°C')
        print('Celsius to Fahrenheit:', self.__cel_to_fah(), '°F')
        print('Kelvin to Fahrenheit:', self.__kel_to_fah(), '°F')
        print('Celsius to Kelvin:', self.__cel_to_kel(), 'K')
        print('Fahrenheit to Kelvin:', self.__fah_to_kel(), 'K')

temp = float(input('Enter temperature: '))
temp_conv = TempConversion(temp)
temp_conv.get_conversions()