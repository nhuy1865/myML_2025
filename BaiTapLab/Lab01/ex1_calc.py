
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Lỗi: chia cho 0!"
    return a / b

if __name__ == "__main__":
    x = float(input("Nhập số thứ nhất: "))
    y = float(input("Nhập số thứ hai: "))
    op = input("Chọn phép (+, -, *, /): ")

    if op == '+':
        print("Kết quả:", add(x, y))
    elif op == '-':
        print("Kết quả:", subtract(x, y))
    elif op == '*':
        print("Kết quả:", multiply(x, y))
    elif op == '/':
        print("Kết quả:", divide(x, y))
    else:
        print("Phép tính không hợp lệ!")
