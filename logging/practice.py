def mummy(msg):
    message = msg

    def papa():
        print(message)
    return papa


love = mummy('I love You!')
miss = mummy('I miss you!')

love()
miss()
