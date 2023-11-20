# codewars practice Sh.Artem
# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

def likes(names):
    names_len = len(names)
    if names_len == 0:
        return "no one likes this"
    elif names_len == 1:
        return names[0] + ' likes this'
    elif names_len == 2:
        return names[0] + ' and ' + names[1] + ' like this'
    elif names_len == 3:
        return names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'
    else:
        return names[0] + ', ' + names[1] + ' and ' + str(names_len - 2) + ' others like this'
