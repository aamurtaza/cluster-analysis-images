
def loadData():
    if 'data' not in os.listdir(os.getcwd()):
        exit('data directory not found')

    data_dir = os.path.join(os.getcwd(), 'data')
    data_dir_content = os.listdir(data_dir)

    if 'images_patches.csv' not in data_dir_content:
        exit('required files not found')
    my_data = np.genfromtxt(data_dir+'/images_patches.csv', delimiter=',')
    return my_data