"""Create a computation graph."""

import tensorflow as tf

x = tf.Variable(3, name="x")
y = tf.Variable(4, name="y")
f = x*x*y + 2

sess = tf.Session()

sess.run(x.initializer)

sess.run(y.initializer)

result = sess.run(f)

print(result)

sess.close()

with tf.Session() as sess:
    x.initializer.run()
    y.initializer.run()
    result = f.eval()

    print("result: ", result)


