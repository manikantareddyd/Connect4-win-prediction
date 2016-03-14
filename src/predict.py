from vectorize import *
import sys
from sklearn.svm import LinearSVC

train_vectors,train_labels,test_vectors,test_labels = get_data(int(sys.argv[1]))

win=[]
draw=[]
loss=[]

for i in range(len(train_vectors)):
    if train_labels[i]==1:
        win.append(train_vectors[i])
    elif train_labels[i]==0:
        draw.append(train_vectors[i])
    else:
        loss.append(train_vectors[i])

win_l = ['1' for i in win]
draw_l = ['0' for i in draw]
loss_l = ['-1' for i in loss]

classifier_win_draw = LinearSVC()
classifier_win_draw.fit(win+draw,win_l+draw_l)

classifier_draw_loss = LinearSVC()
classifier_draw_loss.fit(draw+loss,draw_l+loss_l)

classifier_loss_win = LinearSVC()
classifier_loss_win.fit(loss+win,loss_l+win_l)

for test_vector in test_vectors:
    t_w_d   =   classifier_win_draw.predict(test_vector)
    t_d_l   =   classifier_draw_loss.predict(test_vector)
    t_l_w   =   classifier_loss_win.predict(test_vector)
    
