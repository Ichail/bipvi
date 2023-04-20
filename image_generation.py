import numpy as np
import matplotlib.pyplot as plt


def get_fourier(byte_string, numb_name) -> None:
    pass_to_image_dir = "./images/"
    x = np.frombuffer(byte_string, dtype=np.uint8)  # преобразуем байт-строку в числовой массив
    fourier = np.fft.fft(x)  # вычисляем ряд Фурье
    freq = np.fft.fftfreq(len(x))  # вычисляем дискретные частоты преобразования Фурье
    plt.plot(freq, fourier)
    plt.savefig(pass_to_image_dir + numb_name + ".png")
    plt.close()


def get_bytes_matrix(filename) -> None:
    counter = 1 
    with open(filename, 'rb') as f:
        while True:
            data = f.read(100)
            if not data:
                break
            f.seek(-99, 1)
            counter += 1
            # print(data, end="\n\n")
            get_fourier(data, str(counter))


filename = input("Filename: ")
get_bytes_matrix(filename)
