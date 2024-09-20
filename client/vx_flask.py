from flask import Flask, request

app = Flask(__name__)

datas = []


@app.route("/vx", methods=['GET', 'POST'])
def vx():
    if request.method == "GET":
        print(datas)
        if len(datas) > 0:
            data = datas.pop()
            info = " ".join([str(i) for i in data])
            return info
        else:
            return ""
    elif request.method == "POST":
        print(datas)
        data = request.form.get("num")
        data = [float(i) for i in data.split(" ")]
        datas.append(data)
        print("收到的数据是：", data)
        return "收到的数据是：{}".format(data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000)
