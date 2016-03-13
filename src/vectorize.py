def vectorize():
    f=open('data/connect-4.data','r')
    instances=f.read().split('\n')
    f.close()
    vectors=[]
    labels =[]
    for instance in instances:
        vector=[]
        for play in instance.split(','):
            if play=='loss':
                labels.append(-1)
            elif play=='draw':
                labels.append(0)
            elif play=='win':
                labels.append(1)
            elif play=='o':
                vector.append(1)
                vector.append(0)
                vector.append(0)
            elif play=='b':
                vector.append(0)
                vector.append(1)
                vector.append(0)
            elif play=='x':
                vector.append(0)
                vector.append(0)
                vector.append(1)
        vectors.append(vector)
    return vectors[:-1],labels

def get_data(fold):
    train_vectors,train_labels = vectorize()
    test_vectors  = train_vectors[(fold-1)*13000:fold*13000]
    test_labels   = train_labels[(fold-1)*13000:fold*13000]
    del train_vectors[(fold-1)*13000:fold*13000]
    del train_labels[(fold-1)*13000:fold*13000]
    return train_vectors,train_labels,test_vectors,test_labels
