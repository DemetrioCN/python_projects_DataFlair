from pytube import YouTube 
from pytube.cli import on_progress

class GoTube():
    def __init__(self):
        print("------Convertidor de Youtube------")
        self.url = input("URL: ")
        print("")

    def prepare_download(self):
        print("Preparando Descarga...")
        self.yt = YouTube(self.url, on_progress_callback=on_progress)

    def start_download(self):
        print("\nIniciando Descarga...")
        self.yt.streams.first().download()
        print("\n¡Descarga Completada ;)!")

if __name__ == '__main__':
    gt = GoTube()
    gt.prepare_download()
    gt.start_download()


