import tensorflow as tf
import cv2

model = tf.keras.models.load_model('helmet_detection_model.h5')

vdo = cv2.VideoCapture(0)

while(True):
    ret,current_frame = vdo.read()
    
    img = tf.image.resize(current_frame, (224,224))
    img = img/255.
    prediction = model.predict(tf.expand_dims(img,axis =0))
    tf.squeeze(prediction)
    print(prediction)

    cv2.imshow('current_frame',current_frame)
    if prediction[0][0] > 0.70:
        print('Helmet FOUND')
    else:
        print('Helmet NOT FOUND')
        
    cv2.waitKey(1000)