# https://www.interviewcake.com/question/python/stock-price

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
stocks_1 = [3, 1, 5, 1, 10]
stocks_2 = [0, 100, 5, 18]
stocks_3 = [1, 100, 1, 2]
stocks_4 = [100, 98, 97, 1]
stocks_5 = [1, 1, 1, 1]

def get_max_profit(lst):
  min_price = min(lst)
  min_price_index = lst.index(min_price) #Will it only ever give the first index?
  list_after_min = lst[min_price_index:]
  max_price = 0

  for price in list_after_min:
    if price > max_price:
      max_price = price

  print("min_price", min_price)
  print("min price index", min_price_index)
  print("max_price", max_price)
  print(max_price - min_price)

print("Yesterday")
get_max_profit(stock_prices_yesterday)
print("stocks_1")
get_max_profit(stocks_1)
print("stocks_3")
get_max_profit(stocks_5)
# Look into unit testing pls
