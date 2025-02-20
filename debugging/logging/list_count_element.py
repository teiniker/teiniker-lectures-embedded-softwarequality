import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s : %(message)s')
log = logging.getLogger(__name__)

def list_count_element(nums:list, element:int) -> int:
    log.debug("list_count_element(%s, %d)", nums, element)
    counter = 0
    for n in nums:
        log.debug("  for-loop: n = %d", n)
        if n == element:
            log.debug("    element found, counter = %d", counter)
            # Bug: count += count + 1
            counter += 1
    return counter

numbers = [5, 2, 1, 8, 4, 3, 7, 1, 1, 4]
count = list_count_element(numbers, 1)
print(f"Count of elements = {count}")
assert count == 3
