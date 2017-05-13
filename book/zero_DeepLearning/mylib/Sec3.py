import numpy as np

def step_function(x):
    y = x > 0
    return y.astype(np.int)

def sigmoid(x):
    return 1/(1+np.exp(-x))

def relu(x):
    return np.maximum(0,x)

def softmax(x):
    c0 = np.max(x)
    exp_x = np.exp(x - c0)
    sum_exp_x = np.sum(exp_x)
    return exp_x / sum_exp_x

def identity_function(x):
    return x

def init_network():
    network = {}
    network['W1'] = np.array([  [0.1, 0.3, 0.5],
                                [0.2, 0.4, 0.6]])
    network['b1'] = np.array([  [0.1, 0.2, 0.3]])
    network['W2'] = np.array([  [0.1, 0.4],
                                [0.2, 0.5],
                                [0.3, 0.6]])
    network['b2'] = np.array([  [0.1, 0.2]])
    network['W3'] = np.array([  [0.1, 0.3],
                                [0.2, 0.4]])
    network['b3'] = np.array([  [0.1, 0.2]])
    return network

def forward_step(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x,W1) + b1
    z1 = step_function(a1)
    a2 = np.dot(z1,W2) + b2
    z2 = step_function(a2)
    a3 = np.dot(z2,W3) + b3
    y = identity_function(a3)
    return y

def forward_sigmoid(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x,W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1,W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2,W3) + b3
    y = identity_function(a3)
    return y

def forward_relu(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x,W1) + b1
    z1 = relu(a1)
    a2 = np.dot(z1,W2) + b2
    z2 = relu(a2)
    a3 = np.dot(z2,W3) + b3
    y = identity_function(a3)
    return y

def img_show(img):
    from PIL import Image
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

def get_data():
    from mylib.dataset.mnist import load_mnist
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize = True, flatten = True, one_hot_label = False)
    return x_test, t_test

def init_network(): # pickleファイルの読み込み
    import pickle
    with open("mylib\dataset\sample_weight.pkl", "rb") as f:
        network = pickle.load(f)
    return network

def predict(network, x):
    W1, W2, W3 = network["W1"], network["W2"], network["W3"]
    b1, b2, b3 = network["b1"], network["b2"], network["b3"]
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)
    return y
