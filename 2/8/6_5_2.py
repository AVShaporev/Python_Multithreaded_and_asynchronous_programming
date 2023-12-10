'''
В реальном использовании не стараются делать синхронизацию этапов в одной целевой задаче с повтором. В действительности стараются делать простую и прозрачную реализацию без лишних усложнений. Вот несколько примеров "боевой" реализации барьера в реальных проектах:

2. PyTorch: барьер используется в PyTorch для синхронизации потоков, выполняющих обучение нейронных сетей:
'''

import torch
import threading

def train(model, optimizer, train_loader):
    num_batches = len(train_loader)
    batch_barrier = threading.Barrier(num_batches)

    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad()
        output = model(data)
        loss = loss_fn(output, target)
        loss.backward()
        optimizer.step()
        batch_barrier.wait()