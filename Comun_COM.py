import serial
import time


def enviar_codigo_g_via_serial(arquivo_gcode, porta_com='COM3', baudrate=115200):
    # Abre a conexão serial com a máquina
    try:
        with serial.Serial(porta_com, baudrate, timeout=1) as ser:
            print(f"Conectado à {porta_com} com baudrate {baudrate}")

            # Abre o arquivo .gcode
            with open(arquivo_gcode, 'r') as arquivo:
                for linha in arquivo:
                    # Enviar cada linha de G-code para a máquina
                    ser.write(linha.encode('utf-8'))  # Envia a linha codificada como bytes
                    print(f"Enviado: {linha.strip()}")

                    # Aguarda um tempo para garantir que o comando seja processado
                    time.sleep(0.1)  # Ajuste conforme necessário

            print("Código G enviado com sucesso!")

    except serial.SerialException as e:
        print(f"Erro de conexão serial: {e}")
    except FileNotFoundError:
        print(f"Arquivo {arquivo_gcode} não encontrado.")


# Exemplo de uso
arquivo_gcode = 'hello_texto.gcode'  # O arquivo G-code gerado anteriormente
enviar_codigo_g_via_serial(arquivo_gcode, porta_com='COM3', baudrate=115200)
