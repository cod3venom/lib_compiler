"""
 * Project: Table.js.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 5/2/2021
 * Time: 10:13 AM
 * Github: https://github.com/cod3venom
"""


"""
 * Project: Real-estate-Picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 4/30/2021
 * Time: 7:43 PM
 * Github: https://github.com/cod3venom
"""


class ArgParser:

    _EMPTY = ""
    __SPACE = " "
    __EQUALITY = "="
    __DOUBLE_DASH = "--"
    __args = {}

    def setARgs(self, args: dict):
        self.__args = args

    def getArgs(self) -> dict:
        return self.__args

    def __splitOnEquality(self, param: str) -> list:
        return param.split(self.__EQUALITY)

    def sysArgvTOdict(self) -> dict:
        import sys
        for param in sys.argv:
            if self.__EQUALITY in param:
                onEquality = self.__splitOnEquality(param=param)
                try:
                    self.__args[onEquality[0]] = onEquality[1]
                except IndexError:
                    print("PARAMS INDEX ERROR")
            else:
                self.__args[param] = ""
        return self.getArgs()

    def getValueOf(self, key: str):
        for _key in self.__args.keys():
            if _key == key:
                return self.__args[_key]

        return ""

    def keyEquals(self, key: str, value):
        if self.getValueOf(key=key) == value:
            return True
        return False

    def keyExists(self, key: str) -> bool:
        for _key in self.__args.keys():
            if key == _key:
                return True
        return False