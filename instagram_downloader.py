import os
import instaloader
from moviepy.editor import VideoFileClip
from pathlib import Path

class InstagramDownloader:
    def __init__(self):
        self.loader = instaloader.Instaloader()
        self.download_path = Path("downloads")
        self.download_path.mkdir(exist_ok=True)

    def download_and_convert(self, post_url):
        try:
            # Extrair o shortcode da URL
            shortcode = post_url.strip("/").split("/")[-1]
            
            # Baixar o post
            post = instaloader.Post.from_shortcode(self.loader.context, shortcode)
            
            # Criar pasta específica para este download
            post_path = self.download_path / f"{post.owner_username}_{shortcode}"
            post_path.mkdir(exist_ok=True)
            
            # Download do post
            self.loader.download_post(post, target=str(post_path))
            
            # Encontrar o arquivo de vídeo baixado
            video_file = None
            for file in post_path.glob("*.mp4"):
                video_file = file
                break
            
            if not video_file:
                raise Exception("Nenhum arquivo de vídeo encontrado após o download")
            
            # Converter para MP3
            mp3_path = post_path / f"{video_file.stem}.mp3"
            video = VideoFileClip(str(video_file))
            video.audio.write_audiofile(str(mp3_path))
            video.close()
            
            return {
                "success": True,
                "mp3_path": str(mp3_path),
                "message": "Download e conversão concluídos com sucesso"
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "message": "Erro durante o download ou conversão"
            }

# Exemplo de uso
if __name__ == "__main__":
    downloader = InstagramDownloader()
    result = downloader.download_and_convert("https://www.instagram.com/reel/DKCl8SvxMAR")
    print(result) 