def unzip_and_extract(file_name):
    '''
    Extracts and zippes a zip file.
    
    Arguments:
        file_name :(str) name of the file(.zip format) to be unzipped with the extention
                            * Might not support a path instead of a file name
                            * So,ensure that the file with filename 'file_name' (say abc.zip) is in the working directory
    
    '''
    import zipfile
    
    zipped_file = zipfile.ZipFile(file_name)
    zipped_file.extractall()
    zipped_file.close()
    
    
    
def walk_through_dir(root_folder_path):
    '''
    Extracts and zippes a zip file.
    
    Arguments:
        root_folder_path :(str) The path of the data_set inside which you have to walk through
    '''
    import os
    for (dir_path,dir_names,file_names) in os.walk(root_folder_path):
        print(f'There are {len(dir_names)} directories and {len(file_names)} images in {dir_path}')
        

def view_random_image(target_dir,target_class):
    
    '''
    View some random images of the target_class from the train/test dataset(target_dir).
    
    Arguments:
        target_dir: (str) the train_data_path or the test_data_path
        target_class: (str) the name of the class inside whoose image is to be viewed randomly
        
    '''
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    import random
    import os
    
    target_folder = target_dir + "/" + target_class
    
    #get a sample random image from the the target_folder
    random_image = random.sample(os.listdir(target_folder), 1)
    
    #plot and visualise the image
    img = mpimg.imread(target_folder + "/" + random_image[0])
    plt.imshow(img)
    plt.title(target_class)
    plt.axis("off");
    
    # show the shape of the image
    print(f"Image shape: {img.shape}") 

    
def load_and_prep_image(image_path,img_size = (224,224)):
        
    import tensorflow as tf
    import matplotlib.pyplot as plt
    
    img = tf.io.read_file(image_path)
    img = tf.image.decode_jpeg(img)
    
    #resize the image
    img = tf.image.resize(img, img_size)
    img = img/255.
    
    #plot the image
    plt.imshow(img)
    plt.axis('off')
    
    return img
        
    






