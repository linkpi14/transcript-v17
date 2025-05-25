# Download de Vídeos do Instagram

Este módulo permite fazer o download de vídeos do Instagram e convertê-los para MP3.

## Requisitos

Certifique-se de ter o Python 3.7+ instalado e as seguintes dependências:

```bash
pip install -r requirements.txt
```

## Como usar

1. Importe a classe InstagramDownloader:

```python
from src.instagram_downloader import InstagramDownloader

# Crie uma instância do downloader
downloader = InstagramDownloader()

# Faça o download e conversão de um vídeo
result = downloader.download_and_convert("https://www.instagram.com/reel/SEU_CODIGO_AQUI")
print(result)
```

## Estrutura do Retorno

O método `download_and_convert` retorna um dicionário com:

- Em caso de sucesso:
  ```python
  {
      "success": True,
      "mp3_path": "caminho/para/arquivo.mp3",
      "message": "Download e conversão concluídos com sucesso"
  }
  ```

- Em caso de erro:
  ```python
  {
      "success": False,
      "error": "Descrição do erro",
      "message": "Erro durante o download ou conversão"
  }
  ```

## Observações

- Os arquivos são salvos na pasta `downloads` no diretório do projeto
- Cada download cria uma pasta específica com o formato `username_shortcode`
- O arquivo MP3 terá o mesmo nome do arquivo de vídeo original 