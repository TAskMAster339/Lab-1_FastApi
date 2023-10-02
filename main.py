from fastapi import FastAPI

app = FastAPI()
A = []


@app.get("/")
def hello():
    return {"Calculator": "v1"}


@app.get("/calc/result")
def get_calculation():
    """Выводит последний результат"""
    return A[-1] if len(A) > 0 else None


@app.delete("/calc/clear")
def clear_list():
    """Очищает список с результатами"""
    A.clear()


@app.get("/calc/history")
def get_history():
    """Выводит историю калькулятора"""
    return A


@app.post("/calc")
def make_calculations(a: int, b: int, char: str):
    """a - первое чиcло,
       b - второе число,
       char - знак мат. операции
       ( + - * / )
    """
    if char == '+':
        A.append(a + b)
        return get_calculation()
    elif char == '-':
        A.append(a - b)
        return get_calculation()
    elif char == '*':
        A.append(a * b)
        return get_calculation()
    elif char == '/':
        if b == 0:
            return None
        A.append(a / b)
        return get_calculation()
    else:
        return {"Mistake": "404"}
