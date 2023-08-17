import numpy as np
import tensorflow as tf
from keras.utils import img_to_array, load_img
import suggestions as sugg

def Model_Kidney(img_path):
    interpreter = tf.lite.Interpreter(model_path="../Training/Kidney Disease/Training_data_Kidney_lite.tflite")
    interpreter.allocate_tensors()
    input_index = interpreter.get_input_details()[0]["index"]
    output_index = interpreter.get_output_details()[0]["index"]
    diseases_labels = ['Cyst', 'Normal', 'Stone', 'Tumor']
    image = load_img(img_path, color_mode="grayscale", target_size=(500,500), interpolation="nearest")
    test_image = img_to_array(image)
    test_image = np.array([test_image])
    interpreter.set_tensor(input_index, test_image)
    interpreter.invoke()
    output = interpreter.tensor(output_index)
    pred = list(output()[0])
    mx = max(pred)
    if int(mx) == 1:    
        dis = diseases_labels[pred.index(mx)]
        result = sugg.Kidney_Sug(dis)
    else:
        result = sugg.Kidney_Sug("None")
    return [result,dis]

def Model_Brain(img_path):
    interpreter = tf.lite.Interpreter(model_path="../Training/Brain Disease/Training_data_Brain-Tumor_lite.tflite")
    interpreter.allocate_tensors()
    input_index = interpreter.get_input_details()[0]["index"]
    output_index = interpreter.get_output_details()[0]["index"]
    diseases_labels = ['Glioma', 'Meningioma', 'Notumor', 'Pituitary']
    image = load_img(img_path, color_mode="grayscale", target_size=(500,500), interpolation="nearest")
    test_image = img_to_array(image)
    test_image = np.array([test_image])
    interpreter.set_tensor(input_index, test_image)
    interpreter.invoke()
    output = interpreter.tensor(output_index)
    pred = list(output()[0])
    mx = max(pred)
    if int(mx) == 1:    
        dis = diseases_labels[pred.index(mx)]
        result = sugg.Brain_Sug(dis)
    else:
        result = sugg.Brain_Sug("None")
    return [result,dis]

def Model_Lungs(img_path):
    interpreter = tf.lite.Interpreter(model_path="../Training/Lung Disease/Training_data_Lung_lite.tflite")
    interpreter.allocate_tensors()
    input_index = interpreter.get_input_details()[0]["index"]
    output_index = interpreter.get_output_details()[0]["index"]
    diseases_labels = ['Covid', 'Lung_Opacity', 'Normal', 'Viral_Pneumonia']
    image = load_img(img_path, color_mode="grayscale", target_size=(500,500), interpolation="nearest")
    test_image = img_to_array(image)
    test_image = np.array([test_image])
    interpreter.set_tensor(input_index, test_image)
    interpreter.invoke()
    output = interpreter.tensor(output_index)
    pred = list(output()[0])
    mx = max(pred)
    if int(mx) == 1:    
        dis = diseases_labels[pred.index(mx)]
        result = sugg.Lungs_Sug(dis)
    else:
        result = sugg.Lungs_Sug("None")
    return [result,dis]

def Model_Tuber(img_path):
    interpreter = tf.lite.Interpreter(model_path="Model_TB_lite.tflite")
    interpreter.allocate_tensors()
    input_index = interpreter.get_input_details()[0]["index"]
    output_index = interpreter.get_output_details()[0]["index"]
    diseases_labels = ['Infected','Normal']
    image = load_img(img_path, target_size=(224,224), interpolation="nearest")
    test_image = img_to_array(image)
    test_image = np.array([test_image])
    interpreter.set_tensor(input_index, test_image)
    interpreter.invoke()
    output = interpreter.tensor(output_index)
    pred = list(output()[0])
    mx = max(pred)
    if int(mx) == 1:    
        dis = diseases_labels[pred.index(mx)]
        result = sugg.Tuber_Sug(dis)
    else:
        result = sugg.Tuber_Sug("None")
    return [result,dis]