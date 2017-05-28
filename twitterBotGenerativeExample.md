# Demonstrate Seq2Seq Wrapper with twitter chat log


```python
import tensorflow as tf
import numpy as np

# preprocessed data
from keras import datasets
#from datasets.twitter import data
import data_utils
```


```python
# load data from pickle and npy files
metadata, idx_q, idx_a = data.load_data(PATH='datasets/twitter/')
(trainX, trainY), (testX, testY), (validX, validY) = data_utils.split_dataset(idx_q, idx_a)
```


```python
# parameters 
xseq_len = trainX.shape[-1]
yseq_len = trainY.shape[-1]
batch_size = 16
xvocab_size = len(metadata['idx2w'])  
yvocab_size = xvocab_size
emb_dim = 1024
```


```python
import seq2seq_wrapper
```


```python
import importlib
importlib.reload(seq2seq_wrapper)
```




    <module 'seq2seq_wrapper' from '/home/suriya/_/tf/tf-seq2seq-wrapper/seq2seq_wrapper.py'>




```python
model = seq2seq_wrapper.Seq2Seq(xseq_len=xseq_len,
                               yseq_len=yseq_len,
                               xvocab_size=xvocab_size,
                               yvocab_size=yvocab_size,
                               ckpt_path='ckpt/twitter/',
                               emb_dim=emb_dim,
                               num_layers=3
                               )
```

    <log> Building Graph </log>


```python
val_batch_gen = data_utils.rand_batch_gen(validX, validY, 256)
test_batch_gen = data_utils.rand_batch_gen(testX, testY, 256)
train_batch_gen = data_utils.rand_batch_gen(trainX, trainY, batch_size)
```


```python
sess = model.train(train_batch_gen, val_batch_gen)
```

    
    <log> Training started </log>
    
    Model saved to disk at iteration #500
    val   loss : 3.370399
    Interrupted by user at iteration 565



```python
sess = model.restore_last_session()
```


```python
input_ = test_batch_gen.__next__()[0]
output = model.predict(sess, input_)
print(output.shape)
```

    (256, 20)



```python
replies = []
for ii, oi in zip(input_.T, output):
    q = data_utils.decode(sequence=ii, lookup=metadata['idx2w'], separator=' ')
    decoded = data_utils.decode(sequence=oi, lookup=metadata['idx2w'], separator=' ').split(' ')
    if decoded.count('unk') == 0:
        if decoded not in replies:
            print('q : [{0}]; a : [{1}]'.format(q, ' '.join(decoded)))
            replies.append(decoded)
```

    q : [go see them]; a : [i was thinking of that]
    q : [a unk of the before we say goodnight from last at unk state park in maine]; a : [this is a great idea to be a great day for a while]
    q : [unless you want this ]; a : [what is he]
    q : [my fav moment from the debate last night]; a : [wait for the first time]
    

```
