DEFAULT_LOCALES_PATH = 'locales/'
DEFAULT_LOCALE_SUFFIX = 'locale'


class Localist:
    _locale: str
    _locales_path: str
    _locale_suffix: str
    _locale_dict: dict[str, str]

    def __init__(self, locale: str, 
                 locales_path:str = DEFAULT_LOCALES_PATH, locale_suffix: str = DEFAULT_LOCALE_SUFFIX):
        self._locale = locale
        self._locales_path = locales_path
        self._locale_suffix = locale_suffix

        self._locale_dict = self._load_locale(f'{locales_path}{locale}.{locale_suffix}')

    def _load_locale(self, filename: str) -> dict[str, str]:
        with open(filename) as f:
            lines = f.readlines()
            kvlines = [l.split('=') for l in lines] # TODO: Handle rogue lines.
            tuples = [(l[0].trim(), l[1].trim()) for l in kvlines]
            return {k: v for (k, v) in tuples}

    def get(self, key: str) -> str:
        return self._locale_dict[key]
