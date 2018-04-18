"""
Mandelbrot fractal using PIL (Python)

http://code.activestate.com/recipes/577111-mandelbrot-fractal-using-pil/
"""

from PIL import Image
# drawing area (xa < xb and ya < yb)
xa, xb, ya, yb = -2.0, 1.0, -1.5, 1.5
maxIt = 256  # iterations
# image size
imgx, imgy = 512, 512
image = Image.new("RGB", (imgx, imgy))

for y in range(imgy):
    cy = y * (yb - ya) / (imgy - 1) + ya
    for x in range(imgx):
        cx = x * (xb - xa) / (imgx - 1) + xa
        c = complex(cx, cy)
        z = 0
        for i in range(maxIt):
            if abs(z) > 2.0:
                break
            z = z * z + c
        r = i % 4 * 64
        g = i % 8 * 32
        b = i % 16 * 16
        image.putpixel((x, y), b * 65536 + g * 256 + r)

image.save("mandel.png", "PNG")
