from flask import Flask, request

app = Flask(__name__)


@app.route("/obj", methods=['POST'])
def object():
    dir = "\project\comp\init_img\object"
    file = request.files.get('objfile')
    dstPath = dir + "\\" + file.filename
    print("dstPath：", dstPath)
    file.save(dstPath)


@app.route("/bg", methods=['POST'])
def background():
    dir = r"\project\comp\init_img\background"
    file = request.files.get('bgfile')
    dstPath = dir + "\\" + file.filename
    print("dstPath：", dstPath)
    file.save(dstPath)


@app.route("/img", methods=['POST'])
def img():
    dir = "\project\comp\gene_img\img"
    # dir ="H:\img_server"
    file = request.files.get('imgfile')
    dstPath = dir + "\\" + file.filename
    print("dstPath：", dstPath)
    file.save(dstPath)


if __name__ == '__main__':
    app.run()