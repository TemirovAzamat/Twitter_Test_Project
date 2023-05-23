from PIL import Image, ImageDraw, ImageFont


file_path = 'media/jelly.png'

image = Image.open(file_path)

# # Показать изображение
# image.show()


# # Обрезка изображения
# cropped_image = image.crop((0, 80, 200, 400))
# cropped_image.save('media/jelly_cropped.png')


# # Поворот изображения
# rotated_image = image.rotate(90)
# rotated_image.save('media/jelly_rotated.png')


# # Водяной знак
# img_draw = ImageDraw.Draw(image)
# watermark_text = 'This is Codify Property'
#
# font = ImageFont.truetype('arial.ttf', size=32)
#
# img_draw.text((10, 10), watermark_text, font=font)
# image.save('media/jelly_watermark.png')


# # Конвертация из PNG в JBG
# image = image.convert('RGB')
# image.save('media/jelly.jpg', 'JPEG')


# # Изменение разрешения
# image_resize = image.resize((400, 400))
# image_resize.save('media/jelly_resized.png')



# print(image.size)
#
# width, height = image.size
#
# new_height = 300
# new_width = int(width * new_height / height)
#
# image_resize = image.resize(
#     (new_width, new_height)
# )
# image_resize.save('media/jelly_correct_resize.png')



width, height = image.size

new_width = 400
new_height = int(height * new_width / width)

image_resize = image.resize(
    (new_width, new_height)
)

image_resize.save('media/jelly_new_correct_resize.png')