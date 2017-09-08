import pandas as pd
import tensorflow as tf
import numpy as np

def calculate_pcc(row, contigs):
r = tf.divide(tf.subtract(tf.multiply(tf.to_float(n), tf.reduce_sum(tf.multiply(row, contigs), 1)), tf.multiply(tf.reduce_sum(row, 1), tf.reduce_sum(contigs, 1))) , tf.multiply(tf.sqrt(tf.subtract(tf.multiply(tf.to_float(n), tf.reduce_sum(tf.square(row), 1)), tf.square(tf.reduce_sum(row, 1)))), tf.sqrt(tf.subtract(tf.multiply(tf.to_float(n), tf.reduce_sum(tf.square(contigs), 1)), tf.square(tf.reduce_sum(contigs, 1))))))
return r

