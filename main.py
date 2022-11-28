from PIL import Image

def main():

    input_file_path = "input/input.png"

    # We open the image. The resulting variable has the type "Image" as defined by the library PIL
    image = Image.open(input_file_path)

    # TODO: Uncomment the following line to have the script to show picture "input.png"
    #image.show()

    # We extract red, green, and blue components of the image.
    # Each of these components get stored in a different variable.
    red_channel_image = image.getchannel(0)
    green_channel_image = image.getchannel(1)
    blue_channel_image = image.getchannel(2)

    # We're saving the resulting pictures to the output folder
    red_channel_image.save("output/red.png")
    green_channel_image.save("output/green.png")
    blue_channel_image.save("output/blue.png")


if __name__ == '__main__':
    main()
