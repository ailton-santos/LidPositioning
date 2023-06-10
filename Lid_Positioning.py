import cv2
import numpy as np

# Função para encontrar e desenhar os contornos das tampas de garrafas
def encontrar_tampas(imagem):
    # Converter a imagem para escala de cinza
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Aplicar um filtro de suavização para reduzir o ruído
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Aplicar uma transformação de canny para detecção de bordas
    edges = cv2.Canny(blurred, 50, 150)

    # Encontrar os contornos na imagem
    contornos, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Lista para armazenar os contornos das tampas
    contornos_tampas = []

    # Percorrer todos os contornos encontrados
    for contorno in contornos:
        # Calcular a área do contorno
        area = cv2.contourArea(contorno)

        # Se a área do contorno for maior que um determinado limite, consideramos como uma tampa de garrafa
        if area > 500 and area < 2000:
            # Obter o retângulo delimitador do contorno
            (x, y, w, h) = cv2.boundingRect(contorno)

            # Desenhar o retângulo delimitador na imagem original
            cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Armazenar o contorno da tampa na lista
            contornos_tampas.append(contorno)

    return imagem, contornos_tampas

# Função para calcular e desenhar os círculos que representam o posicionamento das tampas de garrafas
def calcular_posicionamento_tampas(imagem, contornos_tampas):
    # Criar uma cópia da imagem para desenhar os círculos
    imagem_circulos = np.copy(imagem)

    # Percorrer todos os contornos das tampas
    for contorno in contornos_tampas:
        # Obter as coordenadas do retângulo delimitador do contorno
        (x, y, w, h) = cv2.boundingRect(contorno)

        # Calcular o centro do retângulo delimitador
        centro_x = x + w // 2
        centro_y = y + h // 2

        # Calcular o raio do círculo
        raio = (w + h) // 4

        # Desenhar um círculo no centro da tampa na imagem dos círculos
        cv2.circle(imagem_circulos, (centro_x, centro_y), raio, (0, 0, 255), 2)

    return imagem_circulos

# Função para executar o programa
def executar_programa():
    # Carregar a imagem
    imagem = cv2.imread('C:\Users\ailto\Downloads\reference.jpg')

    # Encontrar e desenhar os contornos das tampas de garrafas na imagem
    imagem_contornos, contornos_tampas = encontrar_tampas(imagem)

    # Calcular e desenhar os círculos que representam o posicionamento das tampas de garrafas
    imagem_circulos = calcular_posicionamento_tampas(imagem, contornos_tampas)

    # Mostrar a imagem com os contornos e os círculos
    cv2.imshow('Detecção de Tampas de Garrafas', imagem_circulos)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Executar o programa
executar_programa()
