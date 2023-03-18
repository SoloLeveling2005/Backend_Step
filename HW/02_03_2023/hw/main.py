# todo task 6

# онлайн кинотеатр стоит s рублей, пицца – p рублей, а всего он заработал m рублей


def evening(s_: int, p_: int, m_: int):
    return_ = m_ - s_ - p_
    print("Yes") if return_ > 0 else print("No")


s = 500
p = 600
m = 2000

evening(s_=s, p_=p, m_=m)
# Yes

s = 700
p = 800
m = 1000

evening(s_=s, p_=p, m_=m)
# No


# todo task 7


