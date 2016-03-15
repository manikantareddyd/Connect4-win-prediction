from vectorize import *
import sys
from sklearn.svm import LinearSVC
from sklearn.metrics import *

train_vectors,train_labels,test_vectors,test_labels = get_data(int(sys.argv[1]))
win=[]
draw=[]
loss=[]

# print "Data Read"
for i in range(len(train_vectors)):
    if train_labels[i]==1:
        win.append(train_vectors[i])
    elif train_labels[i]==0:
        draw.append(train_vectors[i])
    else:
        loss.append(train_vectors[i])
# print "Data Classified"
win_l = ['1' for i in win]
win_rest_l = ['0' for i in draw+loss]
draw_l = ['1' for i in draw]
draw_rest_l = ['0' for i in loss+win]
loss_l = ['1' for i in loss]
loss_rest_l = ['0' for i in win+draw]

# print "Building win draw classifier"
classifier_win_rest = LinearSVC()
classifier_win_rest.fit(win+draw+loss,win_l+win_rest_l)

# print "Building draw loss classifier"
classifier_draw_rest = LinearSVC()
classifier_draw_rest.fit(draw+loss+win,draw_l+draw_rest_l)

# print "Building loss win classifier"
classifier_loss_rest = LinearSVC()
classifier_loss_rest.fit(loss+win+draw,loss_l+loss_rest_l)

predictions=[]
for i in range(len(test_vectors)):
    t_w_r   =   int(classifier_win_rest.predict([test_vectors[i]])[0])
    t_d_r   =   int(classifier_draw_rest.predict([test_vectors[i]])[0])
    t_l_r   =   int(classifier_loss_rest.predict([test_vectors[i]])[0])
    t       =   [t_w_r,t_d_r,t_l_r]
    if t==[1,1,1] or t==[1,1,0] or t==[1,0,1] or t==[1,0,0] or t==[0,0,0]: p=1
    elif t==[0,1,1] or t==[0,0,1]: p=-1
    else: p=0
    predictions.append((p))

print "*"*80
print classification_report(test_labels,predictions)
print confusion_matrix(test_labels,predictions,labels=[1,0,-1])
print "*"*80
