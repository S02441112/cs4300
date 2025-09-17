def words_in_file():
    f = open("task6_read_me.txt")
    return len(f.read().split())
