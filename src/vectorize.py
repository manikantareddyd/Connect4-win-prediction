def vectorize():
    instances=open('data/connect-4.data','r').read().split('\n')
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
