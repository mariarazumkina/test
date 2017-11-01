def count_lines(data):
    return(len(data.readlines()))

def count_words(data):
    c = []
    for line in data:
        words = line.split(" ")
        c.append(len(words))
    return (sum(c))

def count_chars (data):
    cc = []
    for line in data:
        chars = list(line)
        cc.append(len(chars))
    return (sum(cc))
