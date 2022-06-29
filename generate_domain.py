#!/usr/bin/env python

""" 
    Domain Generation Algorithms (DGA)
    Used by malware like CryptoLocker, before it switched to a more sophisticated variant
    https://en.wikipedia.org/wiki/Domain_generation_algorithm
"""

import datetime


### CONFIGURE ###
# Set g_date as "YYYY-MM-DD" or set it to "" for current date
g_date = ""
# Set the chosen TLD
g_tld = ".com"


### DO NOT EDIT BELOW THIS LINE UNLESS YOU KNOW WHAT YOU ARE DOING ###


def generate_domain(year, month, day):
    """Generate a domain name for the given date."""
    global g_tld
    domain = ""
    for i in range(16):
        year = ((year ^ 8 * year) >> 11) ^ ((year & 0xFFFFFFF0) << 17)
        month = ((month ^ 4 * month) >> 25) ^ 16 * (month & 0xFFFFFFF8)
        day = ((day ^ (day << 13)) >> 19) ^ ((day & 0xFFFFFFFE) << 12)
        domain += chr(((year ^ month ^ day) % 25) + 97)
    return domain + g_tld

def set_custom_date():
    global g_date
    year, month, day = g_date.split("-")
    g_date = datetime.date(int(year), int(month), int(day))

def main():
    global g_date
    if g_date:
        set_custom_date()
    else:
        g_date = datetime.date.today()
    print (generate_domain(g_date.year, g_date.month, g_date.day))

main()
