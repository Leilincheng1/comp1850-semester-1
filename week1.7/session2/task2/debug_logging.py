# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 1.7, Session 2: Task 2 - logging
#
# import logging
#
# def calculate_average(scores):
    # add logging configuration    
#     logging.basicConfig(filename='log.txt', filemode='w', level=logging.DEBUG)
#     
    # you can turn the logging off
    # logging.disable(logging.CRITICAL)
#     
#     logger = logging.getLogger()
#     logger.info(f"calculate_average(): started")
#     
#     total_score = sum(scores)
#     total_assignments = len(scores)
#     
    # add debug logging here
#     
#     average = total_score // total_assignments
#     
    # add a debug logging here
#     
#     return round(average,2)
#
# print(calculate_average([85, 90, 88]))
# Expected Output: 87.67
# Actual Output:   87.0
# ============================================================================
# Completed solution
# ============================================================================
"""Log the intermediate steps while calculating a floating-point average."""
import logging

logging.basicConfig(
    filename="log.txt",
    filemode="w",
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s",
)
logger = logging.getLogger(__name__)


def calculate_average(scores):
    """Return the scores' arithmetic mean rounded to two decimal places."""
    logger.info("calculate_average(): started")
    total_score = sum(scores)
    total_assignments = len(scores)
    logger.debug("scores=%s", scores)
    logger.debug("total_score=%s", total_score)
    logger.debug("total_assignments=%s", total_assignments)

    if total_assignments == 0:
        logger.error("Cannot calculate the average of an empty list")
        raise ValueError("scores must not be empty")

    # True division is required; floor division // loses the decimal part.
    average = total_score / total_assignments
    logger.debug("average before rounding=%s", average)
    answer = round(average, 2)
    logger.info("calculate_average(): result=%s", answer)
    return answer


if __name__ == "__main__":
    print(calculate_average([85, 90, 88]))
    # Expected output: 87.67
