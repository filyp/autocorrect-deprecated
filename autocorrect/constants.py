# -*- coding: utf-8 -*-

word_regexes = {
    'en': r'[A-Za-z]+',
    'pl': r'[A-Za-zęóąśłżźćń]+',
    'ru': r'[АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя]+',
    'uk': r'[АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬЮюЯя]+',
    'tr': r'[a-zA-ZçÇğĞüÜöÖşŞıİ]+',
    'es': r'[A-Za-záéíóúüñ]+',
}

alphabets = {
    'en': 'abcdefghijklmnopqrstuvwxyz',
    'pl': 'abcdefghijklmnopqrstuvwxyzęóąśłżźćń',
    'ru': 'шиюынжсяплзухтвкйеобмцьёгдщэарчфъ',
    'uk': 'фагксщроємшплуьцнжхїйювязтибґідеч',
    'tr': 'abcçdefgğhıijklmnoöprsştuüvyzqwxÇĞİÜÖ',
    'es': 'abcdefghijklmnñopqrstuvwxyzáéíóúü',
}
