import io
import subprocess
import time


def pararTreinamentoModelo():
    with open('_model/treinador.log', 'w') as f:
        f.close()

    with open('_model/treinador.log', 'w') as f:
        subprocess.Popen(['docker', 'stop', 'treinador'], stdout=f, stderr=f)

        with open('_model/treinador.log', 'r') as f2:
            while len(f2.readlines()) == 0:
                f2 = open('_model/treinador.log', 'r')
            f2.close()

        f.close()

    with open('_model/treinador.log', 'w') as f:
        f.close()

def run(diretorio):
    pararTreinamentoModelo()

    with open('_model/model.log', 'w') as f:
        subprocess.Popen(['docker', 'run', '--rm', '-it', '--name', 'treinador', '-d', '-v', '{}:/home'.format(diretorio), 'snelf-fasttext', '/bin/bash', '-c', 'fasttext supervised -input datasets/data.train.txt -output _model/model -verbose 2 > _model/model.log 2>&1'], stdout=f, stderr=f)

        while True:
            time.sleep(3)
            processo = subprocess.Popen(['docker', 'ps', '-a', '--filter', 'name=treinador'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            saida, erro = processo.communicate()
            saida_string = saida.decode('utf-8')

            if len(saida_string.split("\n")[1]) == 0:
                break