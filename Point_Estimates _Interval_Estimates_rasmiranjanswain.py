#!/usr/bin/env python
# coding: utf-8

# #### Write a python program for the calculation of Point Estimates & Interval Estimates:

# In[7]:


import math
Alpha_dict = {0.025: 1.96, 0.05: 1.64}

def estimates(mean, sigma, sample_size):
  """
  Calculates the point estimate and interval estimate for a population mean.

  Args:
    mean: The sample mean.
    sigma: The sample standard deviation.
    sample_size: The sample size.

  Returns:
    A tuple of the point estimate and interval estimate.
  """

  alpha = 0.05  # Default alpha value is 5%
  z_critical = Alpha_dict[alpha]  # Get the z-critical value for the given alpha

  # Calculate the point estimate
  point_estimate = mean

  # Calculate the margin of error
  margin_of_error = z_critical * sigma / math.sqrt(sample_size)

  # Calculate the interval estimate
  lower_bound = point_estimate - margin_of_error
  upper_bound = point_estimate + margin_of_error

  return point_estimate, (lower_bound, upper_bound)


if __name__ == "__main__":
  # Set the sample mean, standard deviation, and sample size
  mean = 66
  sigma = 5
  sample_size = 100

# Calculate the point estimate and interval estimate
point_estimate, interval_estimate = estimates(mean, sigma, sample_size)

# Print the results
print("Point Estimate:", point_estimate)
print("Interval Estimate:", interval_estimate)
print(f"Point Estimate is {round(point_estimate, 2)} and the Interval Estimate is {round(interval_estimate[0], 2)} to {round(interval_estimate[1], 2)}")

