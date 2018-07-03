#import tensorflow packages
import tensorflow as tf

#define the matrixes for a , b and c
a = tf.constant([1,3,2,4], name="matrix_a",shape=[2,2])
b = tf.constant([5,6,7,8], name="matrix_b",shape=[2,2])
c = tf.constant([9,10,11,12], name="matrix_c",shape=[2,2])

#compute the power of matrix a
x = tf.pow(a,2)

#add the matrices x and b for x + b
y=tf.add(x,b)

#define the multiply operation for y * c
z=tf.matmul(y,c)

#create the session for evaluating tensor objects
with tf.Session() as s:

    #print a^2
    print(s.run(x))

    #print (a*a+b)
    print(s.run(y))

    #print (a*a+b)*c
    print(s.run(z))