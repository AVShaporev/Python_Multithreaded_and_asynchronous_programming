'''
В реальном использовании не стараются делать синхронизацию этапов в одной целевой задаче с повтором. В действительности стараются делать простую и прозрачную реализацию без лишних усложнений. Вот несколько примеров "боевой" реализации барьера в реальных проектах:

3. Аналогичный пример в TensorFlow:
'''


import tensorflow as tf

def train(model, optimizer, train_dataset):
    num_batches = len(train_dataset)
    batch_barrier = tf.compat.v1.train.Barrier(num_batches)

    for batch_idx, (data, target) in enumerate(train_dataset):
        with tf.GradientTape() as tape:
            output = model(data)
            loss = loss_fn(output, target)
        gradients = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(gradients, model.trainable_variables))
        batch_barrier.wait()