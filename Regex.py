# import re


# \d - digit
# \w - word characters
# \s - whitespace characters
# all capital letter of above is opposite to what it is mentioned
#Quantifiers
#  +  -- one or more
# {3} -exactly x times
# {3,5} - exactly three to five times
#hi{2,} - hiiii...
#? - one or more (optional)


#character classes and sets

#[aeiou] , #[a-z]
#[^k] - it won't match letter K

#anchors and boundaries
# ^ - start of line
# $ - end of line
# \b - word boundary - space at the begin and end of line


#logical or -- |    -- (mr. | mrs.)
#groups  -- ()


 
def parse_date(input):
    pattern = re.compile("^(\d\d)[,/.](\d\d)[,/.](\d{4})$")
    match = pattern.search(input)
    if match:
        return {
            "d": match.group(1),
            "m": match.group(2),
            "y": match.group(3),
        }
    return None