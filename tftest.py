import tensorflow as tf
import numpy as np
node1 = tf.constant(3.0,dtype=tf.float32)
node2 = tf.constant(4.0)
node3 = tf.add(node1,node2)
sess = tf.Session()
print(sess.run([node1,node2]))
print("sess.run(node3):",sess.run(node3))