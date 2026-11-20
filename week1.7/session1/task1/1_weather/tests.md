# Week 1.7, Session 1: Task 1

Equivalence classes and boundary checks for `comfort_level(temperature)`:

| Comfort level | Values |
| --- | --- |
| COLD (`temperature <= 15.0`) | -10, 0, 14.9, **15.0** |
| OK (`15.0 < temperature <= 25.0`) | **15.1**, 20, **25.0** |
| HOT (`temperature > 25.0`) | **25.1**, 30, 40 |

The bold values exercise the thresholds and their neighbouring classes.
