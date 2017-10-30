import tensorflow as tf

# tmp
dir(tf)

# declare constants
a = tf.constant(120, name='a')
b = tf.constant(130, name='b')
c = tf.constant(140, name='c')

# declare variables
v = tf.Variable(0, name='v')

# define graph of data flow
calc_op = a + b + c
assign_op = tf.assign(v, calc_op)

# run session
sess = tf.Session()
sess.run(assign_op)

# print v
print(sess.run(v))
