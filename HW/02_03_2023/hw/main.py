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
#
#
# a, b, c, d, e, f, g, h = 1, 2, 3, 4, 5, 6, 7, 8
#
# horse = [f, 1]
#
#
# def where_can_i_go(position):
#     # todo максимально возможные варианты 8
#
#     top_right, top_left, left_top, left_bottom, bottom_left, bottom_right, right_bottom, right_top = \
#         [position[0]+1, position[1]+2], [position[0]-1, position[1]+2], [position[0]-2, position[1]+2]