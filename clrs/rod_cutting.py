def bottom_up(price_list):
    for i in range(len(price_list)):
        for j in range(i):
            new_price = price_list[j] + price_list[i-j]
            if new_price > price_list[i]:
                price_list[i] = new_price


def top_down(rod_length, price_list):
    if price_list[rod_length] > 0:
        return price_list[rod_length]
    for i in range(1, rod_length):
        new_price = top_down(i, price_list) + top_down(rod_length-i, price_list)
        if new_price > price_list[rod_length]:
            price_list[rod_length] = new_price
    return price_list[rod_length]
