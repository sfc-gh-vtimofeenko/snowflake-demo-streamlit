from typing import Dict, List, Callable, Union

LOCALE_OPTIONS: Dict[str, Union[List[str], Callable[[], List[str]]]] = {
    "English-speaking 🇬🇧": lambda: [
        country for country in LOCALE_OPTIONS["All"] if country.lower().startswith("en")
    ],
    "French-speaking 🇫🇷": lambda: [
        country for country in LOCALE_OPTIONS["All"] if country.lower().startswith("fr")
    ],
    "Spanish-speaking 🇪🇸": lambda: [
        country for country in LOCALE_OPTIONS["All"] if country.lower().startswith("es")
    ],
    "Chinese-speaking 🇨🇳": lambda: [
        country for country in LOCALE_OPTIONS["All"] if country.lower().startswith("zh")
    ],
    "Japanese-speaking 🇯🇵": lambda: [
        country for country in LOCALE_OPTIONS["All"] if country.lower().startswith("ja")
    ],
    "Russian-speaking 🇷🇺": lambda: [
        country for country in LOCALE_OPTIONS["All"] if country.lower().startswith("ru")
    ],
    "All": [
        "af-za",
        "af",
        "am-et",
        "am",
        "ar-ae",
        "ar-dz",
        "ar-eg",
        "ar-sa",
        "ar-us",
        "ar",
        "az-az",
        "az",
        "be-by",
        "be",
        "bg-bg",
        "bg",
        "bn-in",
        "bn",
        "c",
        "ca-ad",
        "ca-es",
        "ca",
        "cs-cz",
        "cs",
        "da-dk",
        "da",
        "de-at",
        "de-ch",
        "de-de",
        "de-ru",
        "de-us",
        "de",
        "el-gr",
        "el",
        "en-150",
        "en-ae",
        "en-ar",
        "en-as",
        "en-at",
        "en-au",
        "en-bd",
        "en-be",
        "en-bh",
        "en-br",
        "en-by",
        "en-ca",
        "en-ch",
        "en-cl",
        "en-cm",
        "en-cn",
        "en-co",
        "en-cr",
        "en-cy",
        "en-cz",
        "en-de",
        "en-dk",
        "en-dz",
        "en-eg",
        "en-es",
        "en-fi",
        "en-fr",
        "en-gb-oxendict",
        "en-gb",
        "en-gh",
        "en-hk",
        "en-hn",
        "en-hr",
        "en-hu",
        "en-id",
        "en-ie",
        "en-il",
        "en-in",
        "en-io",
        "en-iq",
        "en-ir",
        "en-it",
        "en-jo",
        "en-jp",
        "en-ke",
        "en-kr",
        "en-kz",
        "en-lk",
        "en-me",
        "en-mk",
        "en-mm",
        "en-mt",
        "en-mu",
        "en-mx",
        "en-my",
        "en-ng",
        "en-nl",
        "en-no",
        "en-np",
        "en-nz",
        "en-pe",
        "en-ph",
        "en-pk",
        "en-pl",
        "en-pt",
        "en-ro",
        "en-rs",
        "en-ru",
        "en-sa",
        "en-sd",
        "en-se",
        "en-sg",
        "en-si",
        "en-sk",
        "en-th",
        "en-tn",
        "en-tr",
        "en-tz",
        "en-ua",
        "en-ug",
        "en-us",
        "en-us@posix",
        "en-vg",
        "en-vn",
        "en-xa",
        "en-za",
        "en-zg",
        "en-zm",
        "en-zw",
        "en",
        "es-419",
        "es-ar",
        "es-bo",
        "es-br",
        "es-cl",
        "es-co",
        "es-cr",
        "es-do",
        "es-ec",
        "es-es",
        "es-gt",
        "es-hn",
        "es-ie",
        "es-mx",
        "es-ni",
        "es-pa",
        "es-pe",
        "es-py",
        "es-sv",
        "es-us",
        "es-uy",
        "es-ve",
        "es-xl",
        "es",
        "et-ee",
        "et",
        "eu-es",
        "eu",
        "fa-ir",
        "fa",
        "fi-fi",
        "fi",
        "fil",
        "fr-be",
        "fr-bj",
        "fr-ca",
        "fr-cd",
        "fr-ch",
        "fr-ci",
        "fr-cm",
        "fr-dz",
        "fr-fr",
        "fr-gn",
        "fr-ma",
        "fr-sn",
        "fr-tn",
        "fr",
        "gl-es",
        "gl",
        "gu-in",
        "gu",
        "he-il",
        "he",
        "hi-in",
        "hi",
        "hr-ba",
        "hr-hr",
        "hr",
        "hu-hu",
        "hu",
        "hy-am",
        "id-id",
        "id",
        "ig-ng",
        "is-is",
        "is",
        "it-fr",
        "it-it",
        "it-us",
        "it",
        "ja-jp",
        "ja",
        "ka-ge",
        "ka",
        "kab-dz",
        "kk",
        "km-kh",
        "ko-kr",
        "ko",
        "lg-ug",
        "lo-la",
        "lt-lt",
        "lt",
        "lv-lv",
        "lv",
        "mg-mg",
        "mk-mk",
        "mn-mn",
        "mr-in",
        "ms-my",
        "ms",
        "mt-mt",
        "my-mm",
        "nb-no",
        "nb-sj",
        "nb",
        "nl-be",
        "nl-ch",
        "nl-nl",
        "nl",
        "nn",
        "no-no",
        "no",
        "pl-gb",
        "pl-pl",
        "pl",
        "pt-ao",
        "pt-br",
        "pt-pt",
        "pt",
        "ro-md",
        "ro-ro",
        "ro",
        "ru-by",
        "ru-cn",
        "ru-gb",
        "ru-kz",
        "ru-no",
        "ru-ru",
        "ru-tr",
        "ru-ua",
        "ru-us",
        "ru",
        "sh",
        "si",
        "sk-sk",
        "sk",
        "sl-si",
        "sl",
        "so-so",
        "sr-me",
        "sr-rs",
        "sr",
        "sv-se",
        "sv-za",
        "sv",
        "sw-ke",
        "ta-in",
        "ta",
        "te-in",
        "te",
        "th-th",
        "th",
        "tl-ph",
        "tl",
        "tr-tr",
        "tr",
        "uk-ua",
        "uk-us",
        "uk",
        "und",
        "uz-uz",
        "uz",
        "vi-vn",
        "vi",
        "xh-za",
        "yo-ng",
        "zh-br",
        "zh-ca",
        "zh-cn",
        "zh-gb",
        "zh-hans-cn",
        "zh-hans-us",
        "zh-hant-hk",
        "zh-hk",
        "zh-mo",
        "zh-rcn",
        "zh-sg",
        "zh-tw",
        "zh-us",
        "zh",
        "zu-za",
    ],
    "Europe 🇪🇺": [
        "bg-bg",
        "cs-cz",
        "da-dk",
        "de-de",
        "el-gr",
        "en-gb",
        "es-es",
        "et-ee",
        "fi-fi",
        "fr-fr",
        "hr-hr",
        "hu-hu",
        "is-is",
        "it-it",
        "lt-lt",
        "lv-lv",
        "mt-mt",
        "nl-nl",
        "no-no",
        "pl-pl",
        "pt-pt",
        "ro-ro",
        "ru-ru",
        "sk-sk",
        "sl-si",
        "sv-se",
    ],
    "Americas 🌎": [
        "en-ca",
        "en-us",
        "es-ar",
        "es-bo",
        "es-cl",
        "es-co",
        "es-cr",
        "es-do",
        "es-ec",
        "es-gt",
        "es-hn",
        "es-mx",
        "es-ni",
        "es-pa",
        "es-pe",
        "es-py",
        "es-sv",
        "es-uy",
        "es-ve",
        "fr-ca",
        "pt-br",
    ],
    "Asia 🌏": [
        "ar-ae",
        "ar-sa",
        "az-az",
        "he-il",
        "hi-in",
        "id-id",
        "ja-jp",
        "ka-ge",
        "km-kh",
        "ko-kr",
        "lo-la",
        "mn-mn",
        "ms-my",
        "my-mm",
        "th-th",
        "tl-ph",
        "tr-tr",
        "uz-uz",
        "vi-vn",
        "zh-cn",
    ],
    "EMEA (Europe, Middle East, and Africa) 🌍": [
        "ar-ae",
        "ar-sa",
        "bg-bg",
        "cs-cz",
        "da-dk",
        "de-de",
        "el-gr",
        "en-gb",
        "en-za",
        "es-es",
        "et-ee",
        "fi-fi",
        "fr-fr",
        "he-il",
        "hr-hr",
        "hu-hu",
        "is-is",
        "it-it",
        "lt-lt",
        "lv-lv",
        "mt-mt",
        "nl-nl",
        "no-no",
        "pl-pl",
        "pt-pt",
        "ro-ro",
        "ru-ru",
        "sk-sk",
        "sl-si",
        "sv-se",
        "tr-tr",
    ],
    "Africa 🌍": [
        "af-za",
        "am-et",
        "ar-eg",
        "en-ng",
        "en-za",
        "fr-cm",
        "fr-dz",
        "ig-ng",
        "mg-mg",
        "pt-ao",
        "so-so",
        "sw-ke",
        "xh-za",
        "yo-ng",
        "zu-za",
    ],
}