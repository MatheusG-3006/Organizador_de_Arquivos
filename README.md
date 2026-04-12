---

# Organizador de Arquivos

Organizador de arquivos desenvolvido em Python que lê um diretório informado pelo usuário e move automaticamente cada arquivo para uma subpasta correspondente à sua categoria, criando as pastas caso não existam.

---

## Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Como Funciona](#como-funciona)
- [Pré-requisitos](#pré-requisitos)
- [Como Executar](#como-executar)
- [Exemplo de Uso](#exemplo-de-uso)
- [Categorias Suportadas](#categorias-suportadas)
- [Conceitos Aplicados](#conceitos-aplicados)
- [Autor](#autor)

---

## Sobre o Projeto

Manter arquivos organizados manualmente é uma tarefa repetitiva e suscetível a erros. Este script resolve esse problema automatizando o processo: ele identifica a extensão de cada arquivo no diretório informado e o move para uma subpasta de categoria correspondente, criando a pasta automaticamente se ela ainda não existir. Arquivos com extensões não mapeadas são movidos para a pasta Outros.

---

## Como Funciona

O script solicita o nome do diretório, percorre todos os arquivos presentes nele, identifica a extensão de cada um e realiza a movimentação para a subpasta correta. Todo o processo é exibido no terminal em tempo real.

---

## Pré-requisitos

- Python 3.6 ou superior

Verifique sua instalação com:
```bash
python --version
```

Nenhuma biblioteca externa é necessária. O projeto utiliza apenas `os` e `shutil`, que já fazem parte da biblioteca padrão do Python.

---

## Como Executar

Clone o repositório:
```bash
git clone https://github.com/MatheusG-3006/organizador-de-arquivos.git
```

Acesse a pasta:
```bash
cd organizador-de-arquivos
```

Execute o script:
```bash
python organizador.py
```

---

## Exemplo de Uso

```
Digite o Nome da Pasta a ser Organizada: Downloads

Arquivo: foto.png, Extensão: .png, Categoria: Imagens
Arquivo: relatorio.pdf, Extensão: .pdf, Categoria: Docs
Arquivo: musica.mp3, Extensão: .mp3, Categoria: Áudios
Arquivo: filme.mp4, Extensão: .mp4, Categoria: Vídeos
Arquivo: setup.exe, Extensão: .exe, Categoria: Outros

Organizado com Sucesso!!
```

---

## Categorias Suportadas

| Categoria | Extensões |
|-----------|-----------|
| Imagens   | .jpg, .jpeg, .png, .gif, .svg, .bmp, .tiff, .tif |
| Docs      | .pdf, .doc, .docx, .txt, .odt, .xls, .xlsx, .ods, .ppt, .pptx |
| Áudios    | .mp3, .wav, .aac, .wma, .ogg |
| Vídeos    | .mp4, .avi, .mov, .wmv |
| Outros    | .zip, .rar, .exe, .html, .htm, .css, .js, .7z |

---

## Conceitos Aplicados

- **Manipulação de arquivos e diretórios** — uso dos módulos `os` e `shutil`
- **Automação de tarefas** — eliminação de processos manuais e repetitivos
- **Funções e dicionários** — mapeamento de extensões por categoria via função auxiliar
- **Validação de entrada** — verificação se o diretório informado existe antes de executar
- **Interação via terminal** — leitura do diretório e exibição de logs em tempo real

---

## Autor

Desenvolvido por **Matheus Gonçalves dos Santos**
