import joblib
 

knn_from_joblib = joblib.load('xg_boost_recomondation.pkl')
 


def recondation_fn(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10):

					features_list=[float(p1),float(p2),float(p3),float(p4), float(p5), float(p6), float(p7),float(p8),float(p9),float(p10)]

					print(features_list)

					import numpy as np


					int_features2 = np.array(features_list)

					int_features1 = int_features2.reshape(1, -1)


					tested1=knn_from_joblib.predict(int_features1)



					print(tested1)

					return(tested1)




