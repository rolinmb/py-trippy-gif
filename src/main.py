import numpy as np
from PIL import Image
import noise
import random
import imageio

def generate_trippy_frame(width, height, scale, octaves, persistence, lacunarity, z):
    """
    Generate a single frame of trippy Perlin noise.
    """
    img = np.zeros((height, width, 3), dtype=np.uint8)

    x_offset = random.uniform(0, 1000)
    y_offset = random.uniform(0, 1000)

    for y in range(height):
        for x in range(width):
            nx = x * scale + x_offset
            ny = y * scale + y_offset
            val = noise.pnoise3(nx, ny, z, octaves=octaves,
                                persistence=persistence,
                                lacunarity=lacunarity,
                                repeatx=1024, repeaty=1024, base=0)
            normalized = (val + 1) / 2

            # Psychedelic RGB mapping
            r = int(255 * abs(np.sin(normalized * np.pi * 2)))
            g = int(255 * abs(np.cos(normalized * np.pi * 4)))
            b = int(255 * abs(np.sin(normalized * np.pi * 6)))

            img[y, x] = (r, g, b)

    return img


def create_trippy_gif(filename="trippy.gif", width=512, height=512, frames=60):
    scale = 0.01
    octaves = 6
    persistence = 0.5
    lacunarity = 2.0

    images = []
    for i in range(frames):
        print(f"Generating frame {i+1}/{frames}...")
        frame = generate_trippy_frame(width, height, scale, octaves, persistence, lacunarity, z=i * 0.1)
        images.append(Image.fromarray(frame))

    # Save as GIF
    images[0].save(filename, save_all=True, append_images=images[1:], duration=80, loop=0)
    print(f"Animation saved as {filename}")


if __name__ == "__main__":
    create_trippy_gif("trippy_animation.gif")
