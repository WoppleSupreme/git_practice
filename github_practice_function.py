# Databricks notebook source
# Run Multiplication File: Isaac
%run ./includes/mlt

# COMMAND ----------

# Run MDivision File: Jordan
%run ./includes/div

# COMMAND ----------

# Run Addition File: Ravi
%run ./includes/add

# COMMAND ----------

# Run Subtraction File: Mercy
%run ./includes/sub

# COMMAND ----------

# Operational function: Brian
def operational_algebra(i,j):
  multiplication = mlt(i,j)
  division       = div(i,j)
  addition       = add(i,j)
  subtraction    = sub(i,j)
  return (multiplication, division, addition, subtraction)

# COMMAND ----------


