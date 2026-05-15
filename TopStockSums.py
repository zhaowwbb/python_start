import heapq


def calculate_top_3_sum(prices_list):
    """
    Equivalent to Java's calculateTop3SumV4.
    Uses a min-heap to keep track of the 3 largest prices efficiently.
    """
    min_heap = []
    for price in prices_list:
        heapq.heappush(min_heap, price)
        if len(min_heap) > 3:
            heapq.heappop(min_heap)  # Removes the smallest element

    return sum(min_heap)


def calculate_top_3_sumV6(prices_list):
    min_heap = []
    for price in prices_list:
        heapq.heappush(min_heap, price)
        if len(min_heap) > 3:
            heapq.heappop(min_heap)

    return sum(min_heap)


def find_top_3_by_sum(names, prices):
    """
    Processes all stocks and prints the top 3 overall.
    """
    results = []
    for i in range(len(names)):
        total_sum = calculate_top_3_sum(prices[i])
        results.append((names[i], total_sum))  # Using a tuple instead of a custom class

    # Sort stocks by total_sum in descending order (equivalent to Java's List.sort or Streams)
    results.sort(key=lambda x: x[1], reverse=True)

    # Print the top 3 results
    for i in range(min(3, len(results))):
        name, total_sum = results[i]
        print(f"{i + 1}. {name} - Total Sum: {total_sum:.2f}")


def find_top_3_by_sumV6(names, prices):
    results = []
    for i in range(len(names)):
        total_sum = calculate_top_3_sumV6(prices[i])
        results.append((names[i], total_sum))

    results.sort(key=lambda x: x[1], reverse=True)

    for i in range(min(3, len(results))):
        name, total_sum = results[i]
        print(f"{i+1}. {name} - Total Sum: {total_sum:.2f}")


def find_top_3_by_sumV7(names, prices):
    stock_map = {}
    for i in range(len(names)):
        top_3_prices = heapq.nlargest(3, prices[i])
        stock_map[names[i]] = sum(top_3_prices)

    top_3 = sorted(stock_map.items(), key=lambda item: item[1], reverse=True)[:3]

    for index, (name, total_sum) in enumerate(top_3, 1):
        print(f"{index}. {name} -Total Sum: {total_sum:.2f}")


# Equivalent to V5 (Using a dictionary / map approach)
def find_top_3_by_sum_v5_style(names, prices):
    stock_map = {}
    for i in range(len(names)):
        # Python's heapq.nlargest(3, list) is an ultra-fast way to mimic a Max-Heap poll loop
        top_3_prices = heapq.nlargest(3, prices[i])
        stock_map[names[i]] = sum(top_3_prices)

    # Equivalent to Java Stream .sorted().limit(3)
    top_3 = sorted(stock_map.items(), key=lambda item: item[1], reverse=True)[:3]

    for index, (name, total_sum) in enumerate(top_3, 1):
        print(f"{index}.  {name} - Total Sum: {total_sum:.2f}")


if __name__ == "__main__":
    stocks = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]

    prices = [
        [150.0, 160.0, 140.0, 155.0],  # AAPL: top 3 are 160, 155, 150 (Sum: 465)
        [
            2800.0,
            2900.0,
            2700.0,
            2850.0,
        ],  # GOOGL: top 3 are 2900, 2850, 2800 (Sum: 8550)
        [300.0, 310.0, 305.0, 290.0],  # MSFT: top 3 are 310, 305, 300 (Sum: 915)
        [
            3400.0,
            3300.0,
            3500.0,
            3450.0,
        ],  # AMZN: top 3 are 3500, 3450, 3400 (Sum: 10350)
        [700.0, 800.0, 750.0, 720.0],  # TSLA: top 3 are 800, 750, 720 (Sum: 2270)
    ]

    print("[4]#####################")
    find_top_3_by_sum(stocks, prices)

    # print("[5]#####################")
    # find_top_3_by_sum_v5_style(stocks, prices)

    print("[6]#####################")
    find_top_3_by_sumV6(stocks, prices)
    print("[7]#####################")
    find_top_3_by_sumV7(stocks, prices)
