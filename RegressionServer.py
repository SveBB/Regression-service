from flask import Flask, render_template
from markupsafe import escape
import numpy as np



def text_file_handle(path):
    file = open(path, 'r')
    data = file.read()
    array = data.split(',')
    array = [float(num) for num in array]
    file.close()
    array = np.array(array).astype(np.float)
    return array

def check_shape(X, Y):
    delta = X.shape[0] - Y.shape[0]
    
    if delta > 0:
        Y = np.append(Y, [0]*delta)
    elif delta < 0:
        X = np.append(X, [0]*(abs(delta)))

    return X,Y


app = Flask(__name__)

@app.route('/')
def main():
    data1 = text_file_handle('Test1.txt')
    data2 = text_file_handle('Test2.txt')
    data1,data2 = check_shape(data1, data2)
    corr = np.corrcoef(data1, data2)[1,0]
    return render_template('index.html', test1=data1, test2=data2, corr_coef = corr)

   
if __name__ == '__main__':
    app.run()
