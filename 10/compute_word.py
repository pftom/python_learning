def count_words(filename):
    """count how many words in a file"""

    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except OSError:
        msg = "Sorry, the file " + filename + " does not exist."
        with open(filename, 'w') as f_obj:
            f_obj.write(msg)
    else:
        # 计算大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) +
            " words.")


filenames = ['../pcc/chapter_10/moby_dick', '../pcc/chapter_10/little_women.hhhh', 'hhhh.rxr']
for filename in filenames:
    count_words(filename)