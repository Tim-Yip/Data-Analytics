import random
import math
import statistics

vals_1_100 = range(1,100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k = 200)
radius = random.randint(3,10)
pi = math.pi

sample_sum = sum(vals_sample)
sample_avg = statistics.mean(vals_sample)
sample_median = statistics.median(vals_sample)

print("_Experimenting with a subset of integers 1-100:")
print(f"Sum of 75 sample values from 1 to 100: {sample_sum}")
print(f"Average of 75 sample values: {sample_avg:.2f}")
print(f"Median of 75 sample values: {sample_median}")

choices_avg = statistics.mean(vals_choices)
choices_median = statistics.median(vals_choices)
choices_mode = statistics.mode(vals_choices)
choices_stdev = statistics.stdev(vals_choices)
choices_variance = statistics.variance(vals_choices)

print("\n_Experimenting with a superset of 200 values, integers 1-100:")
print(f"Average of 200 values: {choices_avg:.2f}")
print(f"Median of 200 values: {choices_median}")
print(f"Mode of 200 values: {choices_mode}")
print(f"Standard deviation of 200 values: {choices_stdev:.2f}")
print(f"Variance of 200 values: {choices_variance:.2f}")

area = pi * radius ** 2
area_up = math.ceil(area)
area_down = math.floor(area)

print("\n_Modeling a random circle:")
print(f"Radius = {radius}, area = {area_up} (rounded up to the nearest integer)")
print(f"Radius = {radius}, area = {area_down} (rounded down to the nearest integer)")