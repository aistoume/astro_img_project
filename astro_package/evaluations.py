import tensorflow as tf
import numpy as np

# Evaluate model on the positive examples only.
def EvalPositiveExamples(model, x_test, y_test):
    probability_model = tf.keras.Sequential([
    model,
    tf.keras.layers.Softmax()
    ])
    prediction = probability_model(x_test[:])
    y_hat = np.argmax(prediction.numpy(), axis=1)
    result = abs(y_test - y_hat)
    idx = (y_test > 0)
    error = sum(result[idx])/sum(y_test)
    correctness = 1 - error
    print('error =', error)
    print('correct =', correctness)

def main():
    print("Evaluate model.")
    
if __name__ == '__main__':
    main()