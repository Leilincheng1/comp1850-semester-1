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
