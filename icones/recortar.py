import argparse
import os
from PIL import Image

def split_grid_image(image_path, rows=4, cols=7, output_dir="icones_cortados"):
    if not os.path.exists(image_path):
        print(f"Erro: O arquivo '{image_path}' não foi encontrado.")
        return

    try:
        with Image.open(image_path) as img:
            width, height = img.size
            
            # Calcula a dimensão exata de cada ícone (4 linhas x 7 colunas)
            tile_width = width // cols
            tile_height = height // rows

            os.makedirs(output_dir, exist_ok=True)
            
            count = 1
            for row in range(rows):
                for col in range(cols):
                    left = col * tile_width
                    upper = row * tile_height
                    right = left + tile_width
                    lower = upper + tile_height

                    # Recorta e salva: 01-07 na linha 1, 08-14 na linha 2, etc.
                    icon = img.crop((left, upper, right, lower))
                    filename = os.path.join(output_dir, f"{count:02d}.png")
                    icon.save(filename, "PNG")
                    
                    count += 1

            print(f"Sucesso! {count - 1} ícones foram salvos no diretório '{output_dir}'.")

    except Exception as e:
        print(f"Ocorreu um erro ao processar a imagem: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Corta uma imagem em grid de 4 linhas x 7 colunas em ícones numerados (01 a 28)."
    )
    parser.add_argument("path", type=str, help="Caminho para o arquivo PNG de entrada")
    parser.add_argument(
        "--rows", type=int, default=4, help="Número de linhas no grid (padrão: 4)"
    )
    parser.add_argument(
        "--cols", type=int, default=7, help="Número de colunas no grid (padrão: 7)"
    )
    parser.add_argument(
        "--out", type=str, default="icones_cortados", help="Pasta de destino das imagens"
    )

    args = parser.parse_args()
    split_grid_image(args.path, rows=args.rows, cols=args.cols, output_dir=args.out)
