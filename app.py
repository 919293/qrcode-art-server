from apistar import App, Route,http
import os
from MyQR import myqr
import io

def run(request: http.Request,words,scale=1,version=1,level='L'):
    try:
        qr = myqr.run(
        	words,
            scale=int(scale),
            version=int(version),
            level=level)
        imgByteArr = io.BytesIO()
        qr.save(imgByteArr, format='PNG')
        return http.Response(imgByteArr.getvalue(), headers={
            'Content-Type': 'image/png'
        })
    except Exception as e:
        return http.JSONResponse({
            'message':e.args
        }, status_code=400)

routes = [
    Route('/', method='GET', handler=run),
]

app = App(routes=routes)


if __name__ == '__main__':
    app.serve('127.0.0.1', 5000, debug=True)
